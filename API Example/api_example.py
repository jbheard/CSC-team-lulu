import flask
import os
from flask import send_from_directory
from werkzeug.utils import secure_filename
from functions import get_random_image

app = flask.Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'img'

# This just serves the main HTML file when you go to the root page
# of the site. This is NOT how you would normally do this, but it's
# the easiest way for the sake of example.
# If you are interested in creating your own website with flask, see
# here: https://flask.palletsprojects.com/en/2.2.x/tutorial/templates/
# and/or here: https://pythonbasics.org/flask-tutorial-templates/
@app.route('/', methods=['GET'])
def route_main():
	return send_from_directory('.', 'index.html')

# Example endpoint to serve an image file
# "/image?img={filename}" will serve the specified image
# "/image" by itself will serve a random image
#
# GET requests are the requests sent by your browser by default, 
# usually to "get" resources (webpages, images, files) from a server
@app.route('/image', methods=['GET'])
def route_get_image():
	img_file = flask.request.args.get('img')
	if not img_file:
		img_file = get_random_image()
	if not os.path.isfile(os.path.join('img', img_file)):
		return f'file {img_file} does not exist', 400
	return send_from_directory('img', img_file)

# Example endpoint to upload a file
# More info here: https://flask.palletsprojects.com/en/2.2.x/patterns/fileuploads/
#
# POST requests are used to "post" data to a server, this is useful when
# you have to send more data than just a URL to the server. In this case
# a file. It is also useful for sending secure (encrypted) data, since
# GET requests don't guarantee security (never send your password in a URL :P)
@app.route('/upload', methods=['POST'])
def route_upload_image():
	# check if the post request has the file part
	if 'file' not in flask.request.files:
		return 'No file part', 400

	file = flask.request.files['file']
	# If the user does not select a file, the browser submits an
	# empty file without a filename.
	if file.filename == '':
		return 'No file provided', 400

	if file:
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		return 'Upload successful!'

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80)
