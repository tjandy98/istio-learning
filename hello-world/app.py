from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/mars')
def hello_mars():
    return 'Hello, Mars!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8008)