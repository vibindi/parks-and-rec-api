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
    speakers = data.get("speaker")
    quotes = data.get("quote")

    # quotes data
    qd = {speakers.get(i):quotes.get(i) for i in range(len(speakers))}

    response["Quotes"] = qd
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
    rand_quote = requests.get('https://parks-and-rec-quotes.herokuapp.com/r').json()
    q = rand_quote.get("Quote")
    s = rand_quote.get("Speaker")
    return render_template('index.html', quote=q, speaker=s)

@app.route('/api')
def api_info():
    return render_template('api-info.html')

if __name__ == '__main__':
    app.run(threaded=True, port=5000)