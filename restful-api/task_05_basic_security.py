#!/usr/bin/python3
"""Module that define differents endpoints, manage users roles, permissions,
autorizations"""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from flask_jwt_extended import get_jwt

app = Flask(__name__)

auth = HTTPBasicAuth()
app.config['JWT_SECRET_KEY'] = "signed_token"
jwt = JWTManager(app)

users = {}


@app.route("/basic-protected", methods=['GET'])
@auth.login_required
def protected_route():
    '''Endpoint protected by a security'''
    return "Basic Auth: Access Granted", 200


@app.route("/login", methods=['POST'])
def login():
    '''Endpoint that verify username and password'''
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    user = users.get(username)
    if user is not None and check_password_hash(user['password'], password):
        access_token = create_access_token(
            identity=user["username"],
            additional_claims={"role": user['role']})
        return jsonify({"access_token": access_token}), 200
    else:
        return "Error", 400


@app.route("/jwt-protected", methods=['GET'])
@jwt_required()
def jwt_protected_route():
    '''Endpoint that is protected by a token'''
    return "JWT Auth: Access Granted", 200


@app.route("/admin-only", methods=['GET'])
@jwt_required()
def role_access():
    '''Secure this endpoint by accessing it, only if you have the correct
    role'''
    token = get_jwt()
    if token['role'] != "admin":
        return jsonify({"error": "Admin access required"}), 403
    else:
        return "Admin Access: Granted", 200


if __name__ == "__main__":
    app.run(debug=True)
