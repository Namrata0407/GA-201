from flask import Flask, render_template, request, redirect
import uuid

app = Flask(__name__)

menu = [
    {'id': 1, 'name': 'Pizza', 'price': 10, 'availability': True},
    {'id': 2, 'name': 'Burger', 'price': 8, 'availability': True},
    {'id': 3, 'name': 'Pasta', 'price': 12, 'availability': False}
]

orders = []

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/menu')
def display_menu():
    return render_template('menu.html', menu=menu)

@app.route('/add_dish', methods=['GET', 'POST'])
def add_dish():
    if request.method == 'POST':
        dish_id = len(menu) + 1
        dish_name = request.form['name']
        dish_price = float(request.form['price'])
        dish_availability = True if request.form.get('availability') else False
        menu.append({'id': dish_id, 'name': dish_name, 'price': dish_price, 'availability': dish_availability})
        return redirect('/menu')
    return render_template('add_dish.html')

@app.route('/remove_dish/<int:dish_id>')
def remove_dish(dish_id):
    for dish in menu:
        if dish['id'] == dish_id:
            menu.remove(dish)
            break
    return redirect('/menu')

@app.route('/update_availability/<int:dish_id>', methods=['GET', 'POST'])
def update_availability(dish_id):
    for dish in menu:
        if dish['id'] == dish_id:
            if request.method == 'POST':
                dish['availability'] = True if request.form.get('availability') else False
                return redirect('/menu')
            return render_template('update_availability.html', dish=dish)
    return 'Dish not found!'

@app.route('/take_order', methods=['GET', 'POST'])
def take_order():
    if request.method == 'POST':
        customer_name = request.form['customer_name']
        dish_ids = [int(dish_id) for dish_id in request.form.getlist('dish_ids')]
        order_id = str(uuid.uuid4())  # Generate a unique order ID
        order = {'order_id': order_id, 'customer_name': customer_name, 'dish_ids': dish_ids, 'status': 'received'}
        orders.append(order)
        return redirect('/orders')
    return render_template('take_order.html', menu=menu, orders=orders)


@app.route('/update_status/<string:order_id>', methods=['GET', 'POST'])
def update_status(order_id):
    for order in orders:
        if order['order_id'] == order_id:
            if request.method == 'POST':
                order['status'] = request.form['status']
                return redirect('/orders')
            return render_template('update_status.html', order=order)
    return 'Order not found!'

@app.route('/orders')
def display_orders():
    return render_template('orders.html', orders=orders)

@app.route('/exit')
def exit_app():
    return 'Thank you for using Zesty Zomato!'

if __name__ == '__main__':
    app.run(debug=True)
