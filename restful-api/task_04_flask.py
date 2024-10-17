#!/usr/bin/python3


from flask import Flask, jsonify, request

app = Flask(__name__)

# Initialize a dictionary to store users
users = {}
users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}

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
    data = request.json
    if 'username' not in data:
        return jsonify({"error": "Username is required"}), 400
    username = data['username']
    if username in users:
        return jsonify({"error": "User already exists"}), 400
    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201

if __name__ == "__main__":
    app.run(debug=True)