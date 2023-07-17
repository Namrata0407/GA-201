from flask import request, jsonify
from werkzeug.exceptions import BadRequest
from flask import Flask

app = Flask(__name__)

weather_data = {
    'San Francisco': {'temperature': 14, 'weather': 'Cloudy'},
    'New York': {'temperature': 20, 'weather': 'Sunny'},
    'Los Angeles': {'temperature': 24, 'weather': 'Sunny'},
    'Seattle': {'temperature': 10, 'weather': 'Rainy'},
    'Austin': {'temperature': 32, 'weather': 'Hot'},
}

@app.route('/weather', methods=['POST'])
def create_weather():
    try:
        data = request.get_json()
        city = data['city']
        temperature = data['temperature']
        weather = data['weather']
    except (KeyError, TypeError, BadRequest):
        return 'Invalid request data', 400

    weather_data[city] = {'temperature': temperature, 'weather': weather}
    return 'Weather data created successfully', 201

@app.route('/weather/<string:city>', methods=['PUT'])
def update_weather(city):
    if city not in weather_data:
        return f'Weather data not found for {city}', 404

    try:
        data = request.get_json()
        temperature = data.get('temperature')
        weather = data.get('weather')
    except BadRequest:
        return 'Invalid request data', 400

    if temperature:
        weather_data[city]['temperature'] = temperature
    if weather:
        weather_data[city]['weather'] = weather

    return 'Weather data updated successfully', 200

@app.route('/weather/<string:city>', methods=['DELETE'])
def delete_weather(city):
    if city not in weather_data:
        return f'Weather data not found for {city}', 404

    del weather_data[city]
    return 'Weather data deleted successfully', 200

@app.route('/weather/<string:city>', methods=['GET'])
def get_weather(city):
    if city in weather_data:
        return jsonify(weather_data[city])
    else:
        return jsonify({'error': f'Weather data not found for {city}'}), 404




if __name__ == '__main__':
    app.run()