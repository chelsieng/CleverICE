from flask import Flask
from pdftotext import async_detect_document

app = Flask(__name__)


@app.route('/flask')
def hello_world():
    return 'Hello World from Flask!'

@app.route('/pdftotext/<file>')
def pdftotext(file):
    return async_detect_document(file)

if __name__ == '__main__':
    app.run(debug=True)
