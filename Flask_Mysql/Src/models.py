from Src import app
from flask_sqlalchemy import SQLAlchemy

import MySQLdb
app.config['SQLALCHEMY_DATABASE_URI']="mysql://root:Souvik@localhost/souvikdb"
app.config['SQLALCHEMY_TRACK_MODIFICATION']= False


db = SQLAlchemy(app)


class Emp (db.Model):
    id=db.Column(db.Integer,primary_key=True)
    Emp=db.Column(db.String(80),nullable=False)
    email=db.Column(db.String(80),nullable=False)


    def __init__(self,Emp,email):
        self.Emp=Emp
        self.email=email