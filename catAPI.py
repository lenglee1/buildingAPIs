import flask
from flask import request, jsonify
import requests
import webbrowser
from wand.image import Image
from wand.display import display
import os

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
	return "<h1>API 2: Return of the CATS</h1><p>This is yet another site is a JC inspired project for LL learning</p>"

#Choose a number from 1-7 for the category of cat you want
#Output can be json, open or save
#Obviously change the path to save it where you want

@app.route('/category/<int:number>/<string:output>/', methods=['GET'])
def category(number,output):
	request_string = 'https://api.thecatapi.com/v1/images/search?category_ids=' + str(number)
	r = requests.get(request_string)
	r_json = r.json()
	categorycatImageURL = r_json[0]['url']
	response = requests.get(categorycatImageURL)
	
	if output == "json":
		return jsonify(r_json)
	elif output == "open":
		webbrowser.open(categorycatImageURL, new=2)
		return "file opened"		
	elif output == "save":
		path = "/Users/lenglee/Documents/python_playfiles/projectEuler/catimages"
		os.chdir(path)
		cwd = os.getcwd()
		
		image = open("saved_cat_category.jpg","wb")
		image.write(response.content)
		image.close()
		return "cat from your chosen category is now saved"
		
#Filetype names can be gif, jpg, png
#Output can be json, open or save
#Obviously change the path to save it where you want

@app.route('/filetype/<string:name>/<string:output>/', methods=['GET'])
def filetype(name, output):
	request_string = 'https://api.thecatapi.com/v1/images/search?mime_types=' + name
	r = requests.get(request_string)
	r_json = r.json()
	filetypecatImageURL = r_json[0]['url']
	response = requests.get(filetypecatImageURL)

	if output == "json":
		return jsonify(r_json)
	elif output == "open":
		webbrowser.open(filetypecatImageURL, new=2)
		return "file opened"		
	elif output == "save":
		path = "/Users/lenglee/Documents/python_playfiles/projectEuler/catimages"
		os.chdir(path)
		cwd = os.getcwd()
		if name == "gif":
			image = open("saved_cat.gif","wb")
			image.write(response.content)
			image.close()
			return "gif file saved you mad gif loving animal"
		else:
			image = open("saved_cat.jpg","wb")
			image.write(response.content)
			image.close()
			return "jpg file saved. but why go for the static when you can have the movings?"

	
#Choose a number from 1-7 for the category of cat you want

@app.route('/category/<int:number>/transformimage/', methods=['GET'])
def transformimage(number):
	request_string = 'https://api.thecatapi.com/v1/images/search?category_ids=' + str(number)
	r = requests.get(request_string)
	r_json = r.json()
	blurredcatImageUrl = r_json[0]['url']
	response = requests.get(blurredcatImageUrl)

	image = open("cat_image.jpg","wb")
	image.write(response.content)

	with Image(filename='cat_image.jpg') as img:
		display(img)

	with Image(filename='cat_image.jpg') as img:
		img.blur(radius=0, sigma=4)
		display(img)


	with Image(filename="cat_image.jpg") as img:
		img.shade(gray=True,
			azimuth=286.0,
			elevation=45.0)
		display(img)
	
	with Image(filename="cat_image.jpg") as img:
		img.transform_colorspace('gray')
		img.edge(radius=1)
		display(img)

	with Image(filename="cat_image.jpg") as img:
		img.spread(radius=8.0)
		display(img)

	return "successfully transformed a cat image with specific category"


app.run()
