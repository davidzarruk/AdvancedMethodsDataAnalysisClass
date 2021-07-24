#!/usr/bin/python
from flask import Flask, request
from m09_model_deployment import predict_proba

app = Flask(__name__)

@app.route('/predict', methods=['GET'])
def URLpredict():
    return predict_proba(request.args.get('URL'))

@app.route('/hola', methods=['GET'])
def hola():
    return "todo bien"


@app.route('/nombre', methods=['GET'])
def nombre():
    return request.args.get('NOMBRE')


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, host='0.0.0.0', port=8888)

