from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route('/get', methods=['GET'])
def read():
    # Load data from data.json
    with open('data.json', 'r') as file:
        data = json.load(file)

    response = jsonify({'data': data})
    response.status_code = 200
    return response

@app.route('/add', methods=['POST'])
def create():
    new_dish = request.json

    # Load existing data from data.json
    with open('data.json', 'r') as file:
        existing_data = json.load(file)
     

    # Append the new dish to the existing data
    existing_data.append(new_dish)

    # Save the updated data back to data.json
    with open('data.json', 'w') as file:
        json.dump(existing_data, file)

    response = jsonify({'message': 'New Dish added successfully'})
    response.status_code = 200
    return response
import json

@app.route('/update/<int:index>', methods=['PUT'])
def update(index):
    updated_dish = request.json

    # Load existing data from data.json
    with open('data.json', 'r') as file:
        existing_data = json.load(file)

    # Update the dish at the specified index
    if len(existing_data) > 0:
        for i in range(0,len(existing_data)) :
            if existing_data[i]["id"] == index:
                print(existing_data[i])
                existing_data[i] = updated_dish

        with open('data.json', 'w') as file:
            json.dump(existing_data, file)

        response = jsonify({'message': 'Dish updated successfully'})
        response.status_code = 200
    else:
        response = jsonify({'message': 'Data does not index'})
        response.status_code = 400

    return response


@app.route('/delete/<int:index>', methods=['DELETE'])
def delete(index):

    print(index)
    # Load existing data from data.json
    with open('data.json', 'r') as file:
        existing_data = json.load(file)

    # Delete the dish at the specified index
    if len(existing_data) > 0:
        for i in range(0,len(existing_data)) :
            if existing_data[i]["id"] == index:
                print(existing_data[i])
                del existing_data[i]
        # Save the updated data back to data.json
        with open('data.json', 'w') as file:
            json.dump(existing_data, file)

        response = jsonify({'message': 'Dish deleted successfully'})
        response.status_code = 200
    else:
        response = jsonify({'message': 'Invalid index'})
        response.status_code = 400

    return response


if __name__ == '__main__':
    app.run()