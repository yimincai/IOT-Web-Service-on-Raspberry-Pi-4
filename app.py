from flask import Flask,jsonify
import json
import sensors

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.after_request
def add_security_headers(resp):
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@app.route("/node-01", methods=['GET'])
def node01Data():

    return jsonify(sensors.defindData())

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)