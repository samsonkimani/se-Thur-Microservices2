from flask import Flask, request, jsonify

app = Flask(__name__)

accounts = {}

@app.route('/create_account', methods=['POST'])
def create_account():
    data = request.json
    username = data.get('username')
   
    accounts[username] = {'username': username, 'balance': 0}
    return jsonify({'message': 'Account created successfully'})


@app.route('/retrieve_account/<username>', methods=['GET'])
def retrieve_account(username):
    
    account = accounts.get(username)
    if account:
        return jsonify(account)
    else:
        return jsonify({'message': 'Account not found'}), 404

@app.route('/user_registered', methods=['POST'])
def user_registered():
    data = request.json
    username = data.get('username')
    # Perform logic when a user is registered
    # For example, you might send a welcome email or perform additional setup

    print("user registered")
    return jsonify({'message': f'User {username} registered successfully'})

@app.route('/user_logged_in', methods=['POST'])
def user_logged_in():
    data = request.json
    username = data.get('username')
    # Perform logic when a user logs in
    # For example, you might track login attempts or perform authentication checks
    return jsonify({'message': f'User {username} logged in successfully'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
