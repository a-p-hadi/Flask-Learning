from flask import Flask, url_for, request, jsonify
import Database as db

app = Flask(__name__)

@app.route('/Purchasing.Vendor', methods=['GET'])
def Vendors():
    rows = db.get_data_from_database()
    return jsonify(rows)

@app.route('/rfm', methods=['GET'])
def rfm():
    custIDstr = request.args.get('customer_id', 0)
    custID = int(custIDstr)
    if custID:
        res = db.get_RFM(custID)
    else:
        res = db.get_Total_RFM()
    return jsonify(res)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
