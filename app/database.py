import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv

load_dotenv()

flask_app  = Flask(__name__)
flask_app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')

db = SQLAlchemy(flask_app)
migrate = Migrate(flask_app , db)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    price = db.Column(db.Float)
    classes = db.relationship('Class', backref='student', lazy=True)

class Class(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    price = db.Column(db.Float)
    time = db.Column(db.Integer)
    date = db.Column(db.Date)
    paid_date = db.Column(db.Date, nullable=True)
    paid = db.Column(db.Boolean, default=False)