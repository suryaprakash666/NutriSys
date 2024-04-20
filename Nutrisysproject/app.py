from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from route import recommendation_bp
from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:suryabhai64@localhost:3306/nutrisys'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Register Blueprints
app.register_blueprint(recommendation_bp)

# Initialize SQLAlchemy
db.init_app(app)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
