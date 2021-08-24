from flask import Blueprint
from flask_jwt_extended.view_decorators import jwt_required
from ..controller.login_control import login, register

loginRoute = Blueprint('login_route', __name__, url_prefix='/api')

@loginRoute.route('/login', methods=['POST'])
def loginAPI():
    return login()

@loginRoute.route('/register', methods=['POST'])
def registerAPI():
    return register()