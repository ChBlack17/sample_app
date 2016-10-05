from flask import Flask, render_template
app = Flask(__name__)

@app.route('/') # / is the homepage route of website
def index():
	return render_template('index.html')

@app.route('/about') # This is for different page "About"
def about:
	return render_template('about.html')

app.run(debug=True)
