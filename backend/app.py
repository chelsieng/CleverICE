from flask import Flask
from .googlecloud import *

app = Flask(__name__)


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

@app.route('/getpdftext/<file>')
def getpdftext(file):
    return get_pdf_text(file)

# if __name__ == '__main__':
#     app.run(debug=True)
