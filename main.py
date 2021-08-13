from flask import Flask
from flask_jwt_extended.jwt_manager import JWTManager
from routes.login_route import *

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'monggawebindo'
app.register_blueprint(loginRoute)

jwt = JWTManager(app)

if __name__ == "__main__":
    app.run(debug=True)