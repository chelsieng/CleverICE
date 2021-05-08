from flask import Flask

app = Flask(__name__)


@app.route('/flask')
def hello_world():
    return 'Hello World from Flask!'


if __name__ == '__main__':
    app.run(debug=True)
