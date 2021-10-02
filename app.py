from flask import Flask, render_template, redirect, request, jsonify
import pandas as pd
import random
import requests
import ast

app = Flask(__name__)

@app.route('/')
def index():
    #rand_quote = requests.request("GET", 'https://parks-and-rec-quotes-api.herokuapp.com/r', headers=headers).json()
    #q = rand_quote.get("quote").get("quote")
    #s = rand_quote.get("quote").get("speaker")
    return render_template('index.html', quote="q", speaker="s")


@app.route('/r/', methods=['GET'])
def randomQuote():
    response = {}

    response["MESSAGE"] = "RANDOM"

    return jsonify

@app.route('/a/', methods=['GET'])
def allQuotes():
    response = {}

    response["MESSAGE"] = "ALL"

    return jsonify

# API Endpoints

'''class AllQuotes(Resource):
    def get(self):
        data = pd.read_csv('data/quotes.csv')
        data = data.to_dict()
        return {'data': data}, 200

class RandomQuote(Resource):
    def get(self):
        data = pd.read_csv('data/quotes.csv')
        data = data.to_dict()
        speakers = data.get('speaker')
        quotes = data.get('quote')
        index = random.randint(0,len(speakers) - 1)
        return {'quote': {'speaker': speakers.get(index), 'quote': quotes.get(index)}}, 200

api.add_resource(RandomQuote, '/r') # Get one random quote
api.add_resource(AllQuotes, '/a') # Get all quotes '''

if __name__ == '__main__':
    app.run(threaded=True, port=5000)