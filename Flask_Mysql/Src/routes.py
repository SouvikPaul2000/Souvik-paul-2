
from Src import app
from flask_sqlalchemy import SQLAlchemy

from flask import Flask,request, jsonify
from Src.models import Emp


db = SQLAlchemy(app)

# Create a Emp
@app.route('/Emp', methods=['POST'])
def add_Emp():
  Emp = request.json['Emp']
  email = request.json['email']
  

  new_Emp = Emp(Emp, email)

  db.session.add(new_Emp)
  db.session.commit()

  return jsonify(new_Emp)



  # Update a Emp
@app.route('/Emp/<id>', methods=['PUT'])
def update_Emp(id):
  Emp = Emp.query.get(id)

  Emp = request.json['Emp']
  email = request.json['email']
  

  Emp.Emp = Emp
  email.email = email
 

  db.session.commit()

  return jsonify(Emp)

# Delete Emp
@app.route('/Emp/<id>', methods=['DELETE'])
def delete_Emp(id):
  Emp = Emp.query.get(id)
  db.session.delete(Emp)
  db.session.commit()

  return jsonify(Emp)