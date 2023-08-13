from flask import Flask, url_for, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/math', methods=['POST'])
def math():
    param = request.json
    NoStr1 = param.get('num1', 0)
    NoStr2 = param.get('num2', 0)
    No1 = int(NoStr1)
    No2 = int(NoStr2)
    data = {
        'sum': No1 + No2,
        'multiply': No1 * No2
    }
    return jsonify(data)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)