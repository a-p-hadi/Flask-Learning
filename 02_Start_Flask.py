from flask import Flask, url_for, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
