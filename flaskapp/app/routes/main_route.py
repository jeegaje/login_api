from flask import Blueprint, render_template, request, jsonify, redirect, url_for, Response, make_response
import requests

main_route = Blueprint('main_route', __name__, template_folder='../main_template')

@main_route.route('/')
def index():
    return render_template('index.html')

@main_route.route('/login', methods=['GET', 'POST'])
def login():
    if request.method=='GET':
        return render_template('login.html')
    elif request.method=='POST':
        email = request.form.get('email')
        password = request.form.get('password')
        data = {
            'email' : email,
            'password' : password
        }
        post = requests.post("http://127.0.0.1:5000/api/login", json=data)
        data_post = post.json()
        kode_status = post.status_code
        if kode_status!=200:
            return render_template('login.html', post_msg=data_post)
        elif data_post['tipe_akun']=='admin':
            response = make_response(redirect(url_for('main_route.dashbord_admin')))
            response.set_cookie('token', data_post['access_token'])
            return response
        elif data_post['tipe_akun']=='mentor':
            response = make_response(redirect(url_for('main_route.dashbord_mentor')))
            response.set_cookie('token', data_post['access_token'])
            return response
        elif data_post['tipe_akun']=='user':
            response = make_response(redirect(url_for('main_route.dashbord_user')))
            response.set_cookie('token', data_post['access_token'])
            return response

@main_route.route('/register/user', methods=['GET', 'POST'])
def register_user():
    if request.method=='GET':
        return render_template('register_user.html')
    elif request.method=='POST':
        email = request.form.get('email')
        password = request.form.get('passw')
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        data_input = {
            "email" : email,
            "password" : password,
            "fname" : first_name,
            "lname" : last_name
        }
        post = requests.post("http://127.0.0.1:5000/api/register/user", json=data_input)
        data_post = post.json()
        return render_template('register_user.html', post_msg=data_post)

@main_route.route('/register/mentor', methods=['GET', 'POST'])
def register_mentor():
    if request.method=='GET':
        return render_template('register_mentor.html')
    elif request.method=='POST':
        email = request.form.get('email')
        password = request.form.get('passw')
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        data_input = {
            "email" : email,
            "password" : password,
            "fname" : first_name,
            "lname" : last_name
        }
        token = request.cookies.get('token')
        post = requests.post("http://127.0.0.1:5000/api/register/mentor", json=data_input, headers={'Authorization': f'Bearer {token}'})
        data_post = post.json()
        return render_template('register_mentor.html', post_msg=data_post)

@main_route.route('/show/user')
def show_user():
    token = request.cookies.get('token')
    data = requests.get('http://127.0.0.1:5000/api/users/user', headers={'Authorization': f'Bearer {token}'})
    return render_template('users.html', data = data.json())

@main_route.route('/show/mentor')
def show_mentor():
    token = request.cookies.get('token')
    data = requests.get('http://127.0.0.1:5000/api/users/mentor', headers={'Authorization': f'Bearer {token}'})
    return render_template('mentors.html', data = data.json())

@main_route.route('/user/<int:id>')
def user(id):
    return render_template('user.html')

@main_route.route('/dashbord/admin')
def dashbord_admin():
    return render_template('dashbord_admin.html')

@main_route.route('/dashbord')
def dashbord_user():
    return render_template('dashbord_user.html')

@main_route.route('/dashbord/mentor')
def dashbord_mentor():
    return render_template('dashbord_mentor.html')