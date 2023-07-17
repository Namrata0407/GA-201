from flask import Flask

app = Flask(__name__)

@app.route('/')
def get_dummy_data():
    dummy_data = {
        'message': 'Hello, this is a dummy response!',
        'data': [1, 2, 3, 4, 5]
    }
    return dummy_data

if __name__ == '__main__':
    app.run(debug=True)
