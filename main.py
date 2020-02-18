from flask import Flask
from flask_restful import Api 
from information import Information
import random

app = Flask(__name__)
api = Api(app)

api.add_resource(Information, "/v1/ai/information", "/v1/ai/information/", "/v1/ai/information/<string:name>")

if __name__ == '__main__':
    app.run(debug=True)