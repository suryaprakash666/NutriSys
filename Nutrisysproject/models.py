from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    activity_level = db.Column(db.String(20), nullable=False)
    goal = db.Column(db.String(20), nullable=False)
    allergies = db.Column(db.String(100))
    disliked_foods = db.Column(db.String(100))
    cultural_restrictions = db.Column(db.String(100))
    past_diseases = db.Column(db.String(100))
