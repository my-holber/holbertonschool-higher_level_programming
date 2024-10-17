#!/usr/bin/python3

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import create_access_token, JWTManager, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()


app.config['JWT_SECRET_KEY'] = 'supersecretkey'

jwt = JWTManager(app)

users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}

# Basic Auth защищённый маршрут
@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    return 'Basic Auth: Access Granted'


# Маршрут для логина и генерации токена
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    post_username = data.get("username")
    post_password = data.get("password")

    user = users.get(post_username)

    if user and check_password_hash(user["password"], post_password):
        # Создание токена для аутентификации
        access_token = create_access_token(identity=post_username)
        return jsonify(access_token=access_token), 200

    return jsonify(message="Invalid username or password"), 401


@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    return 'JWT Auth: Access Granted'



@app.route('/admin-only', methods=['GET'])
def admin_only():
    identity_admin = get_jwt_identity()
    if identity_admin['role'] == 'admin':
        return 'Admin Access: Granted'
    return jsonify({"error": "Admin access required"}), 403


if __name__ == '__main__':
    app.run()
