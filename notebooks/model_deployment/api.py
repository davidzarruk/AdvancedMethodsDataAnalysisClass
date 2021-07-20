#!/usr/bin/python
from flask import Flask, request
from flask_restful import Resource, Api
from m09_model_deployment import predict_proba

app = Flask(__name__)
api = Api(app)

class URLpredict(Resource):
    def get(self):
        return {
         "result": predict_proba(request.args.get('URL'))
        }, 200

api.add_resource(URLpredict, '/predict')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, host='0.0.0.0', port=8888)

