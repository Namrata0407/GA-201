from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome to the Flask application!'

@app.route('/greet/<username>')
def greet_user(username):
    return f'Hello, {username}!'

@app.route('/farewell/<username>')
def farewell_user(username):
    return f'Goodbye, {username}!'

if __name__ == '__main__':
    app.run()