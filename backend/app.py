from flask import Flask
from flask_restx import Resource
from googlecloud import *
import database as db

app = Flask(__name__)

@app.route('/flask')
def hello_world():
    return 'Hello World from Flask!'


""" GCP API's """

# called directly by upload pdf
@app.route('/pdftotext/<file>')
def pdftotext(file):
    return async_detect_document(file)

@app.route('/uploadblob/<file>')
def uploadblob(file):
    return upload_blob(file)

@app.route('/getpdftext/<file>')
def getpdftext(file):
    return get_pdf_text(file)

""" Database API's """

@app.route('/createUser/<string:username>/<string:password>')
def create_user(username, password):
    return db.create_user(username, password)

@app.route('/checkUser/<string:username>/<string:password>')
def check_user(username, password):
    return db.check_user(username, password)

@app.route('/createDoc/<string:name>/<string:path_to_pdf>/<string:path_to_text>/<string:user_id>')
def create_doc(name, path_to_pdf, path_to_text, user_id):
    return db.create_document(name, path_to_pdf, path_to_text, user_id)

@app.route('/deleteDoc/<string:id>')
def delete_doc(id):
    return db.delete_document(id)

@app.route('/getDocs')
def get_doc():
    return db.get_documents()

@app.route('/totalDocs')
def count_docs():
    return db.total_documents()


if __name__ == '__main__':
    app.run(debug=True)
