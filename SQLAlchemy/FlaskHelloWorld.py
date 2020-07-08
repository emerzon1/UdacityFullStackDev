from flask import Flask;

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello, World</h1>'

'''TO run in terminal:
FLASK_APP=helloWorldDB.py flask run

to run with live reload/debug mode:
export FLASK_ENV=development
FLASK_APP=helloWorldDB.py FLASK_DEBUG=true flask run


ALSO: the .py extension in the terminal is OPTIONAL.

to run by calling python3 helloWorldDB.py:

write:
if __name__ == '__main__':
    app.run()

'''
if __name__ == '__main__':
    app.run()