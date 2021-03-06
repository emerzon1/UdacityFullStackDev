#imports
from flask import Flask, jsonify
from flask_cors import CORS

#FIRST TIME RUNNING in terminal:
'''
    CD to outer folder (flask_example)
    % export FLASK_APP=flaskr
    % export FLASK_ENV=development --> RUNS IN DEV MODE: SERVER AUTOMATICALLY RESTARTS
    % flask run
'''
def create_app(test_config=None):
    app = Flask(__name__)
    CORS(app, resources={r"*/api/*" : {origins: '*'}})

    @app.after_request
    def after_request():
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PATCH, DELETE, OPTIONS')
        return response

    @app.route("/")
    def hello():
        return jsonify({'message':'HELLO WORLD'})

    @app.route("/smiley")
    def smiley():
        return "<h1>:)</h1>"


    return app
