from flask import Blueprint
from flask_jwt_extended.view_decorators import jwt_required
from ..controller.login_control import login
from ..controller.register_control import register


apiRoute = Blueprint('api_route', __name__, url_prefix='/api')

@apiRoute.route('/login', methods=['POST'])
def loginAPI():
    return login()

@apiRoute.route('/register', methods=['POST'])
def registerAPI():
    return register()