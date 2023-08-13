from flask import Flask, url_for, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/fruitcode/<string:fruitcode>')
def foodcode(fruitcode):
    _code = 0
    match fruitcode:
        case 'apple':
            _code = 1001
        case 'orange':
            _code = 1002
        case 'banana':
            _code = 1003
        case _:
            _code = -1
    response = f"{fruitcode}'s Code: {_code}"
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)