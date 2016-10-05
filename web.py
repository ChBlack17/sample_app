from flask import Flask 
app = Flask(__name__)

@app.route('/') # / is the homepage route of website
def index():
	return "Hey world!"

app.run(debug=True)
