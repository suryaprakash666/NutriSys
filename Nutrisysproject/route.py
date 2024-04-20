from flask import Blueprint, request, render_template
from models import db, User

recommendation_bp = Blueprint('recommendation_bp', __name__)


@recommendation_bp.route('/recommendation', methods=['POST', 'GET'])
def recommendation():
    if request.method == 'POST':
        age = request.form['age']
        gender = request.form['gender']
        activity_level = request.form['activity-level']
        goal = request.form['goal']
        allergies = request.form['allergies']
        disliked_foods = request.form['disliked-foods']
        cultural_restrictions = request.form['cultural-restrictions']
        past_diseases = request.form['past-diseases']

        user = User(age=age, gender=gender, activity_level=activity_level, goal=goal,
                    allergies=allergies, disliked_foods=disliked_foods,
                    cultural_restrictions=cultural_restrictions, past_diseases=past_diseases)

        db.session.add(user)
        db.session.commit()

        return "Data saved successfully!"
    else:
        return render_template('form.html')



