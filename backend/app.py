from flask import Flask, request
from flask_restx import Resource
from PIL import Image
from .services.googlecloud import *
from .database import *
from .openai_request import openAI

app = Flask(__name__, static_folder='../frontend/dist', static_url_path='/')
UPLOAD_FOLDER = '/data'

@app.route('/flask')
def hello_world():
    return 'Hello World from Flask!'

""" GCP API's for converting pdf to text and storing pdf files on the cloud """

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

""" CockroachDB API's for storing account information """

@app.route('/createUser/<string:username>/<string:password>')
def create_new_user(username, password):
    return create_user(username, password)

@app.route('/checkUser/<string:username>/<string:password>')
def check_user_info(username, password):
    return check_user(username, password)

@app.route('/createDoc/<string:name>/<string:path_to_pdf>/<string:path_to_text>/<string:user_id>')
def create_doc(name, path_to_pdf, path_to_text, user_id):
    return create_document(name, path_to_pdf, path_to_text, user_id)

@app.route('/deleteDoc/<string:id>')
def delete_doc(id):
    return delete_document(id)

@app.route('/getDocs')
def get_doc():
    return get_documents()

@app.route('/totalDocs')
def count_docs():
    return total_documents()

@app.route('/pdfPath/<string:docID>')
def pdf_path(docID):
    return get_pdf_path(docID)


@app.route('/textPath/<string:docID>')
def text_path(docID):
    return get_text_path(docID)


""" OpenAI API's for chatbot and extract information """

@app.route('/scan/<string:docID>')
def scan_doc(docID):
    text = get_pdf_text(get_text_path(docID))
    model = openAI()
    return model.scan(prompt = text)

@app.route('/ask/<string:question>/<string:docID>')
def ask(question, docID):
    text = get_pdf_text(get_text_path(docID))
    model = openAI()
    return model.ask(content = text, question = question)


if __name__ == '__main__':
    app.run(debug=True)
