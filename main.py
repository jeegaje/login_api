from flask import Flask, jsonify, request
from models.user_model import User, session
from flask_jwt_extended import *



app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'monggawebindo'
jwt = JWTManager(app)


@app.route("/users")
@jwt_required()
def index():
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

@app.route("/token", methods=['POST'])
def token():
    email = request.json.get('email')
    password = request.json.get('password')
    query =  session.query(User).filter(User.user_email==email, User.user_password==password).first()
    if query is None:
        data = {
            "massage" : "Periksa email dan password!"
        }
    else:
        data = {
            "id" : query.user_id,
            "username" : query.user_email
        }
        token = create_access_token(data)
        data['token'] = token
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)