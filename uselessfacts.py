import flask
from flask import request, jsonify
import requests



app = flask.Flask(__name__)
app.config["DEBUG"] = True


def returnfact():
	request_string = 'https://uselessfacts.jsph.pl/random.json?language=en'
	r = requests.get(request_string)
	uselessfacts = r.json()
	fact = {'fact': uselessfacts['text']}

	return fact


def listToDict(lst):
    op = { i : lst[i] for i in range(0, len(lst) ) }
    return op


@app.route('/', methods=['GET'])
def home():
	return "<h1>hOw tO BuILd aPiS</h1><p>This site is a prototype API accessing text and images. A JC inspired project for LL learning</p>"


@app.route('/singlefact', methods=['GET'])
def api_singlefact():
	return returnfact()


@app.route('/fivefacts', methods=['GET'])
def api_fivefact():
	fact_list = []
	for i in range(5):
		print(i)

		a = returnfact()
		print(a)
		fact_list.append(a)

	return jsonify(fact_list)


app.run()
