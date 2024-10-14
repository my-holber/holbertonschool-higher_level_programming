from os import error
from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

users = {}


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route('/data')
def get_users():
    return jsonify(list(users.keys()))


@app.route('/status')
def get_status():
    return 'OK'


@app.route('/users/<username>')
def get_user(username):
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error":"User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()

    if data['username'] in users:
        return jsonify({'error": "Username is required'}), 400

    users[data['username']] = {
        'username': data['username'],
        'name':data.get('name'),
        'age': data.get('age'),
        'city': data.get("city")
    }

    return jsonify({f'User added {data["username"]}'}), 201


if __name__ == '__main__':
    app.run()