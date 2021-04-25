import flask
from flask import request, jsonify
import requests
import webbrowser
from flask import send_file

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
	return "<h1>API 2: Return of the CATS</h1><p>This is yet another site is a JC inspired project for LL learning</p>"

@app.route('/category/<int:number>/', methods=['GET'])
def category(number):
	request_string = 'https://api.thecatapi.com/v1/images/search?category_ids=' + str(number)
	print(request_string)
	r = requests.get(request_string)
	r_json = r.json()
	categorycatImageURL = r_json[0]['url']

	return webbrowser.open(categorycatImageURL, new=2)


@app.route('/filetype/<string:name>/', methods=['GET'])
def filetype(name):
	request_string = 'https://api.thecatapi.com/v1/images/search?mime_types=' + name
	print(request_string)
	r = requests.get(request_string)
	r_json = r.json()
	categorycatImageURL = r_json[0]['url']

	return webbrowser.open(categorycatImageURL, new=2)


app.run()
