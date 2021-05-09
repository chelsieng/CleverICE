from flask import Flask, request
from flask_restx import Resource
from PIL import Image
from .services.googlecloud import *

app = Flask(__name__, static_folder='../frontend/dist', static_url_path='/')
UPLOAD_FOLDER = '/data'

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/flask')
def hello_world():
    return 'Hello World from Flask!'

# called directly by upload pdf
@app.route('/pdftotext/<file>')
def pdftotext(file):
    return async_detect_document(file)

@app.route('/uploadblob/<file>')
def uploadblob(file):
    return upload_blob(file)

@app.route('/uploadImage')
def upload_image(Resource):
    def post(self):
        if 'file' not in request.files:
            return 'Please upload file', 400

        file = request.files['file']
        if file.filename == '':
            return 'No selected file', 400

        print("file: " + file)
        print("filename: " + file.filename)
        # root_dir = os.getcwd()
        # img = Image.open(file)

        return upload_blob(file)

@app.route('/getpdftext/<file>')
def getpdftext(file):
    return get_pdf_text(file)

# if __name__ == '__main__':
#     app.run(debug=True)
