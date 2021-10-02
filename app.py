from flask import Flask, request, jsonify
import pandas as pd
app = Flask(__name__)

@app.route('/a/', methods=['GET'])
def respond():
    response = {}
    data = pd.read_csv('data/quotes.csv')
    data = data.to_dict()
    response["Data"] = "data"
    response["Code"] = 200

    # Return the response in json format
    return jsonify(response)

# A welcome message to test our server
@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)