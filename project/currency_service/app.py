import requests
import time
from flask import Flask

app = Flask(__name__)

# Account Service URL
account_service_url = "http://account-service:5000"

@app.route('/start_trading')
def start_trading():
    # Retrieve account information
    response = requests.get(f"{account_service_url}/retrieve_account/<username>")
    if response.status_code == 200:
        account_data = response.json()
        # Start sending currency prices to the API gateway
        while True:
            # Simulate fetching currency prices (replace with actual logic)
            currency_prices = fetch_currency_prices()
            # Send currency prices to API gateway
            send_currency_prices_to_api_gateway(currency_prices)
            # Sleep for some time before fetching prices again
            time.sleep(5)  # Example: Fetch prices every 5 seconds
        return "Trading started successfully"
    else:
        return "Unable to start trading: User does not have an account", 400

def fetch_currency_prices():
    # Simulate fetching currency prices (replace with actual logic)
    # This function should return a dictionary of currency prices
    currency_prices = {
        'USD': 1.23,
        'EUR': 1.10,
        'GBP': 1.40
    }
    return currency_prices

def send_currency_prices_to_api_gateway(currency_prices):
    # Send currency prices to API gateway
    # This function should make an HTTP POST request to the API gateway
    # with the currency prices data
    requests.post('http://api-gateway:80/receive_currency_prices', json=currency_prices)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
