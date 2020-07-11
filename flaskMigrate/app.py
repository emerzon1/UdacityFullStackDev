'''
USE MIGRATION LIBRARY:

command line:
1. flask db init --> Creates initial migration structure
2. DROP DB --> dropdb {database name}
    a. If this doesn't work, try to turn of postgreSQL (pg_ctl -D /usr/local/var/postgres stop) and then start it again 
    (pg_ctl -D /usr/local/var/postgres start)
3. flask db migrate --> Creates migration file w/ upgrade/downgrade logic set up  (use when want to apply change or set up file to upgrade/downgrade)
OTHER COMMANDS: flask db upgrade --> Runs upgrade function in migration file to apply upgrade
OTHER COMMANDS: flask db downgrade --> Runs downgrade function in migration file to de-apply upgrade
'''
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://evanmerzon@localhost:5432/todoapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#Use migration class
migrate = Migrate(app, db)

class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)
    completed = db.Column(db.Boolean(), nullable=True, default=True)

    def __repr__(self):
        return f'<Todo {self.id} {self.description}>'

#DON'T NEED db.create_all()
#db.create_all()
#db.session.add(Todo(description='Have a good day'))
#db.session.commit()
@app.route("/todos/create", methods=['POST'])
def create_todo():
    description = request.get_json()['description']
    todo = Todo(description=description)
    db.session.add(todo)
    db.session.commit()
    return jsonify({
        'description':todo.description
    })

@app.route("/")
def index():
    return render_template('index.html', data=Todo.query.all())