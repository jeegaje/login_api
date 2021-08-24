from flask import request, jsonify
from ..models.user_model import *

def register():
    firstName = request.json.get('fname')
    lastName = request.json.get('lname')
    email = request.json.get('email')
    password = request.json.get('password')
    session.add(User(user_email=email, user_password=password, firstName=firstName, lastName=lastName))
    session.commit()
    return jsonify({"massage":"user sudah ditambah"})
