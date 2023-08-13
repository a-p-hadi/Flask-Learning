from flask import Flask, url_for, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/math', methods=['GET'])
def math():
    NoStr1 = request.args.get('num1')
    NoStr2 = request.args.get('num2')
    No1 = int(NoStr1)
    No2 = int(NoStr2)
    data = {
        'sum': No1 + No2,
        'multiply': No1 * No2
    }
    return jsonify(data)

@app.route('/hi', methods=['POST'])
def hi():
    return "hi"
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)