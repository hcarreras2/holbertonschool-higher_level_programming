#!/usr/bin/python3


from flask import Flask, jsonify, request

app = Flask(__name__)

# Initialize a dictionary to store users

users = {}

# Define a route for the root URL

@app.route('/')
def home():
    return "Welcome to the Flask API!"

# Define a route to serve JSON data

@app.route('/data')
def get_data():
    return jsonify(list(users.keys()))

# Define a route to check the status

@app.route('/status')
def get_status():
    return "OK"

# Define a route to get a user by username

@app.route('/users/<username>')
def get_user(username):
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"})

# Define a route to add a new user

@app.route('/add_user', methods=['POST']), 404
def add_user():
    data = request.get_json()
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201

if __name__ == "__main__":
    app.run(debug=True)