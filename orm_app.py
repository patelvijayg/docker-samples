#pip install flask-sqlalchemy (SQLAlchemy-1.2.11 flask-sqlalchemy-2.3.2)
#pip install Flask-Restless
#pip install flask-mysql
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import flask_restless

app = Flask(__name__)
#1
#app.config.from_pyfile('config.cfg')
#2
#app.config['MYSQL_HOST'] = 'localhost'
#app.config['MYSQL_USER'] = 'yourusername'
#app.config['MYSQL_PASSWORD'] = 'mypassword'
#app.config['MYSQL_DB'] = 'yourdatabasename'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb1.db'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@postgresql:5432/sampledb'
db = SQLAlchemy(app)
#mysql = MySQL(app)

class Person(db.Model):
	def __init__(self,id,name):
		self.id=id
		self.name=name
		
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20))
	pets = db.relationship('Pet', backref='owner', lazy='dynamic')
	
	def __str__(self):
	 return "{0} and {1} ".format(self.id,self.name )
	 
class Pet(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20))
	owner_id = db.Column(db.Integer, db.ForeignKey('person.id'))

def addperson(p):
	db.session.add(p)
	db.session.commit()

db.create_all()	
one = Person(3,'vijay')
#addperson(one)
fetchon=Person.query.filter_by(id=2).first()

result=db.engine.execute('select id,name from person')
for r in result:
	print(r)
	

	
print(fetchon)
	
manager = flask_restless.APIManager(app, flask_sqlalchemy_db=db)
manager.create_api(Person, methods=['GET', 'POST', 'DELETE'])

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8080,debug=True)

#http://127.0.0.1:5000/api/person
#http://127.0.0.1:5000/api/person?q={"filter":[{"name":"id","op":"eq","val":"2"}]}
#curl -X POST http://127.0.0.1:5000/api/person  -H 'Accept: application/json' -H 'Content-Type: application/json'   -d '{"id": 4,"name": "vijay2","pets": []}'
#more detail sample https://github.com/jfinkels/flask-restless