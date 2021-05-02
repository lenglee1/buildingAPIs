# Documentation

**1. catAPI.py**

A. /category/<insert number>

Then choose the number you want and add it to the route.

1 - cats with hats
2 - cats in space
3 - funny
4 - cats with sunglasses
5 - cats in boxes
6 - caturday
7 - cats wearing ties


B. /filetype/<insert filetype>

File types available. Choose the file type you want and add it to the route
gif
jpg
png

If you want any of the three: gif,jpg,png


C. For the filetype and category routes, can also choose how you want the file returned. There are three choices

a. json - returns data in json format
b. open - opens image in diff browser tab
c. save - saved locally

eg.
/filetype/gif/open
/category/3/json
/category/2/save

D. /category/<int:number>/transform

This route will take the image and transform it. There is no choice. It will:

a. blur it
b. shade it
c. transform color spaced
d. spread it




**2. uselessfactsAPI.py**

a. API homepage
http://127.0.0.1:5000

Code attached for you to run. It is a REST API

b. Single fact

This returns one fact as a JSON object.  

The route is /singlefact

c. Five facts

This returns five facts as a JSON object.  
The route is /fivefacts 
