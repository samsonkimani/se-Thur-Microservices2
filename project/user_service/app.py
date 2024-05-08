from flask import Flask, request, jsonify
import requests

app = Flask(__name__)


users = {}

account_service_url = "http://account-service:5000"

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    users[username] = {'password': password}
    
    requests.post(f"{account_service_url}/user_registered", json={'username': username})
    return jsonify({'message': 'User registered successfully'})

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    if username in users and users[username]['password'] == password:
       
        requests.post(f"{account_service_url}/user_logged_in", json={'username': username})
        return jsonify({'message': 'Login successful'})
    else:
        return jsonify({'message': 'Invalid username or password'}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
