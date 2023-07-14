from flask import Flask, jsonify, request
# from pymongo import MongoClient
from pymongo import MongoClient
from bson import ObjectId
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# MongoDB Atlas connection configuration
client = MongoClient('mongodb+srv://namrataawasthi077:angular_zomato@cluster0.9949csp.mongodb.net/mydatabase?retryWrites=true&w=majority')
db = client['mydatabase']
collection = db['dish']
orderCollection = db['order']

# Route for retrieving data
@app.route('/data', methods=['GET'])
def get_data():
    data = list(collection.find())

    # Convert data to a list of dictionaries
    result = []
    for document in data:
        result.append({
            'id': str(document['_id']),
            'dish_name': document['dish_name'],
            'price': document['price'],
            'availability': document['availability']
            # Add more fields as needed
        })
    
    return jsonify(result)

# Route for adding data
@app.route('/data', methods=['POST'])
def add_data():
    data = request.get_json()
    document = data

    result = collection.insert_one(document)

    return jsonify({'id': str(result.inserted_id)})

# Route for updating data
@app.route('/data/<id>', methods=['PUT'])
def update_data(id):
    data = request.get_json()
    update_fields = {}

    for key, value in data.items():
        update_fields[key] = value

    result = collection.update_one({'_id': ObjectId(id)}, {'$set': update_fields})

    if result.modified_count > 0:
        return jsonify({'message': 'Document updated successfully'})
    else:
        return jsonify({'message': 'No document found with the provided ID'})

# Route for deleting data
@app.route('/data/<id>', methods=['DELETE'])
def delete_data(id):
    result = collection.delete_one({'_id': ObjectId(id)})

    if result.deleted_count > 0:
        return jsonify({'message': 'Document deleted successfully'})
    else:
        return jsonify({'message': 'No document found with the provided ID'})

# Route for adding orders
@app.route('/order', methods=['POST'])
def order_data():
    data = request.get_json()
    document = data
    result = orderCollection.insert_one(document)

    return jsonify({'id': str(result.inserted_id)})

# Route for retrieving data
@app.route('/order', methods=['GET'])
def get_order():
    data = list(orderCollection.find())

    # Convert data to a list of dictionaries
    result = []
    for document in data:
        result.append({
            'id': str(document['_id']),
            'dish_name': document['dish_name'],
            'price': document['price'],
            'username':document['username']
            # Add more fields as needed
        })
    
    return jsonify(result)

if __name__ == '__main__':
    app.run()