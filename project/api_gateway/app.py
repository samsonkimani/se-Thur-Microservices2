from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

user_service_url = "http://user-service:5000"
account_service_url = "http://account-service:5000"
currency_service_url = "http://currency-service:5000"

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    response = requests.post(f"{user_service_url}/register", json=data)
    return response.content, response.status_code

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    response = requests.post(f"{user_service_url}/login", json=data)
    return response.content, response.status_code

@app.route('/create_account', methods=['POST'])
def create_account():
    data = request.json
    response = requests.post(f"{account_service_url}/create_account", json=data)
    return response.content, response.status_code

@app.route('/retrieve_account/<username>', methods=['GET'])
def retrieve_account(username):
    response = requests.get(f"{account_service_url}/retrieve_account/{username}")
    return response.content, response.status_code

@app.route('/start_trading', methods=['GET'])
def start_trading():
    response = requests.get(f"{currency_service_url}/start_trading")
    return response.content, response.status_code

@app.route('/receive_currency_prices', methods=['POST'])
def receive_currency_prices():
    data = request.json
    return jsonify(data), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
