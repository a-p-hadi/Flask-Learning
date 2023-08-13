from flask import Flask, url_for, request, jsonify
from math import sin, cos

app = Flask(__name__)

@app.route('/math', methods=['GET', 'POST'])
def project():
    if request.method == 'GET':
        NoStr1 = request.args.get('num1')
        NoStr2 = request.args.get('num2')
        No1 = int(NoStr1)
        No2 = int(NoStr2)
        data = {
            'sum': No1 + No2,
            'multiply': No1 * No2
        }
        return jsonify(data)
    elif request.method == 'POST':
        param = request.json
        NoStr1 = param.get('num1', 0)
        NoStr2 = param.get('num2', 0)
        No1 = int(NoStr1)
        No2 = int(NoStr2)
        data = {
            'sin': sin(No1 + No2),
            'cos': cos(No1 + No2)
        }
        return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)