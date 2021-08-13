from flask import request, jsonify
from models.user_model import *
from flask_jwt_extended import create_access_token

def login():
    email = request.json.get('email')
    password = request.json.get('password')
    query =  session.query(User).filter(User.user_email==email, User.user_password==password).first()
    if query is None:
        data = {
            "massage" : "Periksa email dan password!"
        }
    else:
        data = {
            "user":{
                "id" : query.user_id,
                "email" : query.user_email
            }
        }
        token = create_access_token(data)
        data['token'] = token
    return jsonify(data)

def user():
    result =  session.query(User).all()
    user = []
    for row in result:
        data={ 
            "id" : row.user_id,
            "username" : row.user_email,
            "password" : row.user_password
            }
        user.append(data)
    return jsonify(user)
