from flask import jsonify, request
from flask_jwt_extended import create_access_token, get_jwt_identity
import datetime
import uuid
from .model import contact_us, session, akun


def login():
    input_email = request.json.get('email')
    input_password = request.json.get('password')
    database_data = session.query(akun).filter(akun.email==input_email).first()
    if input_email==None or input_password==None:
        return jsonify(msg ='isi email dan password!'), 400
    elif input_email=='' or input_password=='':
        return jsonify(msg ='isi email dan password!'), 400
    elif database_data==None:
        return jsonify(msg='akun tidak ditemukan!'), 400
    elif database_data.sandi!=input_password:
        return jsonify(msg='Password salah!'), 400
    else:
        user_data = {
            'akun_id' : database_data.akun_id,
            'email' : database_data.email,
            'tipe_akun' : database_data.tipe_akun
        }
        token = create_access_token(user_data)
        user_data['access_token'] = token
        return jsonify(user_data)

def register(tipe_akun):
    input_email = request.json.get('email')
    input_password = request.json.get('password')
    input_nama_depan = request.json.get('fname')
    input_nama_belakang = request.json.get('lname')
    database_data = session.query(akun).filter(akun.email==input_email).first()
    if input_email==None or input_password==None or input_nama_depan==None or input_nama_belakang==None:
        return jsonify(msg ='isi email, password, nama depan, dan nama belakang!'), 400
    elif input_email=='' or input_password=='' or input_nama_depan=='' or input_nama_belakang=='':
        return jsonify(msg ='isi email, password, nama depan, dan nama belakang!'), 400
    elif database_data!=None:
        return jsonify(msg='email sudah terdaftar!'), 400
    else:
        user_data = {
            "akun_id" : uuid.uuid4().hex,
            "email" : input_email,
            "sandi" : input_password,
            "nama_depan" : input_nama_depan,
            "nama_akhir" : input_nama_belakang,
            "create_date" : datetime.datetime.now(),
            "tipe_akun": tipe_akun
        }
        session.add(akun(**user_data))
        session.commit()
        return jsonify(msg='user berhasil dibuat!')

def showUser(tipe_akun):
    token_data = get_jwt_identity()
    if token_data['tipe_akun']!='admin':
        return jsonify(msg='Anda bukan admin!'), 403
    else:
        database_data =  session.query(akun).filter_by(tipe_akun=tipe_akun).all()
        users_data = []
        for list in database_data:
            user = {
                'akun_id' : list.akun_id,
                'nama_depan' : list.nama_depan,
                'nama_akhir' : list.nama_akhir,
                'email' : list.email,
                'sandi' : list.sandi,
                'tipe_akun' : list.tipe_akun,
                'create_date' : list.create_date
            }
            users_data.append(user)
        return jsonify(users_data)

def deleteUser(input_akun_id):
    token_data = get_jwt_identity()
    database_data = session.query(akun).filter(akun.akun_id==input_akun_id).first()
    if token_data['tipe_akun']!='admin':
        return jsonify(msg='Anda bukan admin!'), 403
    elif input_akun_id==None:
        return jsonify(msg='Mausukan akun_id!'), 400
    elif database_data==None:
        return jsonify(msg='Akun tidak ditemukan!'), 400
    else:
        session.delete(database_data)
        session.commit()
        return jsonify(msg='User berhasil dihapus!')

def addContactUs():
    input_perihal = request.json.get('perihal')
    input_nama = request.json.get('nama')
    input_email = request.json.get('email')
    input_subjek = request.json.get('subjek')
    input_pesan = request.json.get('pesan')
    if input_perihal==None or input_nama==None or input_email==None or input_subjek==None or input_pesan==None:
        return jsonify(msg='Harap isi semua!'), 400
    elif input_perihal=='' or input_nama=='' or input_email=='' or input_subjek=='' or input_pesan=='':
        return jsonify(msg='Harap isi semua!'), 400
    else:
        data = {
            "id" : uuid.uuid4().hex,
            "perihal" : input_perihal,
            "nama" : input_nama,
            "email" : input_email,
            "subjek" : input_subjek,
            "pesan" : input_pesan,
            "create_date" : datetime.datetime.now(),
        }
        session.add(contact_us(**data))
        session.commit()
        return jsonify(msg='pesan berhasil dibuat!')

def showContactUs():
    database_data =  session.query(contact_us).all()
    contact_us_data = []
    for list in database_data:
        data = {
            "id" : list.id,
            "perihal" : list.perihal,
            "nama" : list.nama,
            "email" : list.email,
            "subjek" : list.subjek,
            "pesan" : list.pesan,
            "create_date" : list.create_date,
        }
        contact_us_data.append(data)
    return jsonify(contact_us_data)

def showContactUsBy(input_perihal):
    database_data =  session.query(contact_us).filter(contact_us.perihal==input_perihal).all()
    contact_us_data = []
    for list in database_data:
        data = {
            "id" : list.id,
            "perihal" : list.perihal,
            "nama" : list.nama,
            "email" : list.email,
            "subjek" : list.subjek,
            "pesan" : list.pesan,
            "create_date" : list.create_date,
        }
        contact_us_data.append(data)
    return jsonify(contact_us_data)

def showUserByEmail():
    database_data =  session.query(akun).filter(akun.email=='user1@gmail.com').one()
    user_data = {
        'email' : database_data.email,
        'password' : database_data.sandi,
        'firstName' : database_data.nama_depan,
        'lastName' : database_data.nama_akhir
    }
    return jsonify(user_data)
