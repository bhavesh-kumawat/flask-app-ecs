from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, This is my homepage!'

@app.route('/health')
def health():
    return 'Server is up and running on healthy state.'