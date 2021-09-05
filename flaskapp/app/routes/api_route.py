from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..models.controller import *

api_route = Blueprint('api_route', __name__, url_prefix='/api')

@api_route.route('/users/user')
@jwt_required()
def api_users_user():
    return showUser('user')

@api_route.route('/users/mentor')
@jwt_required()
def api_users_mentor():
    return showUser('mentor')

@api_route.route('/email')
def email():
    return showUserByEmail()

@api_route.route('/login', methods=['POST'])
def api_login():
    return login()

@api_route.route('/register/user', methods=['POST'])
def api_register_user():
    return register('user')

@api_route.route('/register/mentor', methods=['POST'])
@jwt_required()
def api_register_mentor():
    token_data = get_jwt_identity()
    if token_data['tipe_akun']!='admin':
        return jsonify(msg='Anda bukan admin!'), 403
    else:
        return register('mentor')

@api_route.route('/delete/<akun_id>', methods=['DELETE'])
@jwt_required()
def api_delete_account(akun_id):
    return deleteUser(akun_id)

@api_route.route('/contact_us', methods=['POST'])
def add_contact_us():
    return addContactUs()

@api_route.route('/contact_us/view', methods=['GET'])
def view_contact_us():
    return showContactUs()

@api_route.errorhandler(500)
def internal_error(error):

    return "Periksa email dan Password"