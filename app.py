from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/a/', methods=['GET'])
def respond():
    response = {}
    response["Quote"] = f"Welcome {name} to our awesome platform!!"

    # Return the response in json format
    return jsonify(response)

# A welcome message to test our server
@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)