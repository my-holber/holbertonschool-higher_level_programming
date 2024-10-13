#!/usr/bin/python3


from flask import Flask, jsonify, request

app = Flask(__name__)

users = {"jane": {"username": "Jane", "age": 28, "city": "Los Angeles"}}


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
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No input data provided"}), 400

    if "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]

    if username in users:
        return jsonify({"error": "User already exists"}), 400

    users[username] = {
        "username": username,
        "age": data.get("age"),
        "city": data.get("city")
    }

    return jsonify({"message": "User added successfully", "user":
                    users[username]}), 201


if __name__ == '__main__':
    app.run()
