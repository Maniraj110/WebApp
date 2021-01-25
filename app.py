import urllib
import pytesseract
from flask import Flask, render_template, request
from binascii import a2b_base64
from PIL import Image



app = Flask(__name__) 


@app.route('/') 
def hello_world(): 
	return render_template("index.html")

@app.route('/translate', methods = ['GET', 'POST'])
def translate():
	if(request.method == 'POST'):
	
	    pytesseract.pytesseract.tesseract_cmd = ‘/app/.apt/usr/bin/tesseract’

		data = request.form['data']
		response = urllib.request.urlopen(data)
		with open('./static/image.jpg', 'wb') as f:
			f.write(response.file.read())

		img = Image.open("./static/image.jpg")

		text = pytesseract.image_to_string(img).strip()

		return render_template("index.html", text = text)

if __name__ == '__main__':  
	app.run(debug=True) 
