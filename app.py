from flask import Flask, request, jsonify, render_template
import pandas as pd
import random
import requests

app = Flask(__name__)

@app.route('/a/', methods=['GET'])
def allQuotes():
    response = {}
    data = pd.read_csv('data/quotes.csv')
    data = data.to_dict()
    response["Data"] = data
    response["Code"] = 200
    return jsonify(response)

@app.route('/r/', methods=['GET'])
def randomQuote():
    response = {}
    data = pd.read_csv('data/quotes.csv')
    data = data.to_dict()
    speaker = data.get('speaker')
    quote = data.get('quote')
    index = random.randint(0,len(speaker) - 1)
    response["Speaker"] = speaker.get(index)
    response["Quote"] = quote.get(index)
    response["Code"] = 200
    return jsonify(response)

@app.route('/')
def index():
    #rand_quote = requests.get('https://parks-and-rec-quotes.herokuapp.com/r').json()
    #print(type(rand_quote))
    #q = rand_quote.get("Quote")
    #s = rand_quote.get("Speaker")
    return render_template('index.html', quote="q", speaker="s")

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)