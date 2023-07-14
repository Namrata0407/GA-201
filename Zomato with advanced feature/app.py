from flask import Flask, request, jsonify
import json
from flask_cors import CORS
import uuid
# import websockets
import asyncio

app = Flask(__name__)
CORS(app) 
connected_clients = set()

# Set up initial data structures
menu = []
orders = {}
order_id_counter = 1

# Read initial data from JSON files
def read_initial_data():
    global menu, orders, order_id_counter
    with open('menu.json') as file:
        menu = json.load(file)
    with open('orders.json') as file:
        orders = {int(key): value for key, value in json.load(file).items()}  # Parse keys as integers
    order_id_counter = max(orders.keys()) + 1 if orders else 1

# Write data to JSON files
def write_data_to_files():
    with open('menu.json', 'w') as file:
        json.dump(menu, file, indent=4)
    with open('orders.json', 'w') as file:
        json.dump(orders, file, indent=4)

# Route to get the menu
@app.route('/menu', methods=['GET'])
def get_menu():
    with open('menu.json', 'r') as file:
        existing_data = json.load(file)
        return existing_data
    return []

# Route to add a dish to the menu
@app.route('/menu', methods=['POST'])
def add_dish():
    data = request.get_json()
    dish_name = data['dish_name']
    dish_id = len(menu) + 1  # Generate unique ID based on the number of existing dishes
    new_dish = {
        'dish_id': dish_id,
        'dish_name': dish_name,
        'price': data['price'],
        'availability': data['availability']
    }
    menu.append(new_dish)
    write_data_to_files()
    return f"{dish_name} has been added to the menu."


# Route to remove a dish from the menu
@app.route('/menu/<dish_id>', methods=['DELETE'])
def remove_dish(dish_id):
    for dish in menu:
        if dish["dish_id"] == int(dish_id):
            menu.remove(dish)
            write_data_to_files()
            return f"Dish with ID {dish_id} has been removed from the menu."
    return f"No dish found with ID {dish_id}."

# Route to update the availability of a dish
@app.route('/menu/<dish_id>', methods=['PUT'])
def update_availability(dish_id):
    availability = request.json["availability"]

    print(availability)

    for dish in menu:
        if dish["dish_id"] == int(dish_id):
            dish["availability"] = availability
            write_data_to_files()
            return f"Availability for dish with ID {dish_id} has been updated."
    return f"No dish found with ID {dish_id}."

# Route to take a new order
@app.route('/orders', methods=['POST'])
def take_order():
    global order_id_counter
    data = request.get_json()
    customer_name = data['customer_name']
    order = {"order_id": order_id_counter, "customer_name": customer_name, "status": "received", "dishes": []}
    
    for dish_id in data['dishes']:
        dish = find_dish(dish_id) 
        if dish is None:
            return f"No dish found with ID {dish_id}.", 400
        elif dish["availability"] == "yes":
            order["dishes"].append(dish)
        else:
            return f"{dish['dish_name']} is not available.", 400
    
    if len(order["dishes"]) > 0:
        orders[order_id_counter] = order
        order_id_counter += 1 
        # str(uuid.uuid4())
        write_data_to_files()
        return "Order placed successfully.", 201
    else:
        return "No dishes added to the order.", 400



# Helper function to find a dish by ID
def find_dish(dish_id):
    for dish in menu:
        if dish["dish_id"] == dish_id:
            return dish
    return None

# Route to update the status of an order
@app.route('/orders/<order_id>', methods=['PUT'])
def update_order_status(order_id):
    if order_id in orders:
        status = request.get_json()['status']
        orders[order_id]["status"] = status
        write_data_to_files()
        return f"Order {order_id} status updated to {status}."
    else:
        return f"No order found with ID {order_id}.", 404
    

async def handle_websocket(websocket, path):
    connected_clients.add(websocket)
    
    try:
        while True:
            message = await websocket.recv()
            # Process WebSocket messages if required
            for client in connected_clients:
                await client.send(message)
    finally:
        connected_clients.remove(websocket)

def broadcast(message):
    for client in connected_clients:
        asyncio.ensure_future(client.send(message))

# start_server = websockets.serve(handle_websocket, 'localhost', 8000)

# Route to review all orders
@app.route('/orders', methods=['GET'])
def review_orders():
    return jsonify(orders)

# Route to handle invalid requests
@app.route('/error', methods=['GET'])
def handle_error():
    return "Invalid request."

# Main program loop
if __name__ == '__main__':
    # asyncio.get_event_loop().run_until_complete(start_server)
    read_initial_data()
    app.run(debug=True)