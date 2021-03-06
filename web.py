import os
from flask import Flask, render_template, request
from googlefinance import getQuotes
app = Flask(__name__)

def get_stock_price(ticker):
	quotes = getQuotes(ticker)
	price = quotes[0]['LastTradePrice']
	return "The price of {} is{}".format(ticker, price)

@app.route('/') # / is the homepage route of website
def index():
	name = request.values.get('name')
	greeting = "Hello {}".format(name)
	return render_template('index.html', greeting=greeting)

@app.route('/about') # This is for different page "About"
def about():
	return render_template('about.html')

@app.route('/results') 
def results():
	stock = request.values.get('stock')
	price = get_stock_price(stock)
	return render_template('results.html', price=price)


port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)
