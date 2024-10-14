from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

users = {}


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route('/data')
def add_users():
    return jsonify(list(users.values()))


@app.route('/status')
def get_status():
    return 'ok'


@app.route('/users/<username>')
def get_user(username):
    if username in users:
        return jsonify(users[username])
    else:
        return "User not found"


@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()

    if data['username'] in users:
        return 'error": "Username is required', 400

    users[data['username']] = {
        'username': data['username'],
        'age': data.get('age'),
        'city': data.get("city")
    }

    return f'JSON received! {data["username"]}', 201


if __name__ == '__main__':
    app.run()