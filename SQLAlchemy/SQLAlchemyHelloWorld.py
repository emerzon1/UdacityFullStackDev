from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#https://video.udacity-data.com/topher/2019/August/5d4df44e_database-connection-uri-parts/database-connection-uri-parts.png (all parts of DB connection URI)

#set URI to database to fetch info from it.
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://evanmerzon@localhost:5432/example'


db = SQLAlchemy(app)

#Create Person Model(TABLE): people table
class Person(db.Model):
    __tablename__ = 'people'
    #Primary key is autoIncrementing.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)

#creates tables for all models --> in this case people table.
db.create_all()

@app.route('/')
def index():
    person = Person.query.first()
    return '<h1>Hello, '  + person.name + '!</h1>'


if __name__ == '__main__':
    app.run()