from flask import json, jsonify, request
from flask_jwt_extended import create_access_token, get_jwt_identity
import datetime
import uuid

from sqlalchemy.orm.session import Session
from .model import contact_us, data_diri, session, akun, kelas, wishlist


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
        data_akun = {
            "akun_id" : uuid.uuid4().hex,
            "email" : input_email,
            "sandi" : input_password,
            "nama_depan" : input_nama_depan,
            "nama_akhir" : input_nama_belakang,
            "create_date" : datetime.datetime.now(),
            "tipe_akun": tipe_akun
        }
        data_diri_akun = {
            "data_diri_id" : uuid.uuid4().hex,
            "akun_id" : data_akun['akun_id']
        }
    session.add(akun(**data_akun))
    session.commit()
    session.add(data_diri(**data_diri_akun))
    session.commit()
    if tipe_akun=='user':
        data_wishlist = {
            "wishlist_id" : uuid.uuid4().hex,
            "user_id" : data_akun['akun_id']
        }
        session.add(wishlist(**data_wishlist))
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
    database_data_akun = session.query(akun).filter(akun.akun_id==input_akun_id).first()
    database_data_datadiri = session.query(data_diri).filter(data_diri.akun_id==input_akun_id).first()
    database_data_wishlist = session.query(wishlist).filter(wishlist.user_id==input_akun_id).first()
    tipe_akun = database_data_akun.tipe_akun
    if input_akun_id==None:
        return jsonify(msg='Mausukan akun_id!'), 400
    elif database_data_akun==None:
        return jsonify(msg='Akun tidak ditemukan!'), 400
    else:
        if tipe_akun=='user':
            session.delete(database_data_wishlist)
            session.commit()
        elif tipe_akun=='mentor':
            cek_database_data_kelas = session.query(kelas).filter(kelas.mentor_id==input_akun_id).first()
            if cek_database_data_kelas!=None:
                database_data_kelas = session.query(kelas).filter(kelas.mentor_id==input_akun_id).all()
                for list in database_data_kelas:
                    data_kelas = session.query(kelas).filter(kelas.mentor_id==list.mentor_id).first()
                    session.delete(data_kelas)
                    session.commit()
        session.delete(database_data_datadiri)
        session.commit()
        session.delete(database_data_akun)
        session.commit()
        return jsonify(msg='User berhasil dihapus!')

def updateDataDiri(akun_id):
    input_jenis_kelamin = request.json.get('jenis_kelamin')
    input_tempat_lahir = request.json.get('tempat_lahir')
    input_tanggal_lahir = request.json.get('tanggal_lahir')
    input_alamat = request.json.get('alamat')
    input_nomor_hp = request.json.get('nomor_hp')
    database_data = session.query(akun).filter(akun.akun_id==akun_id).first()
    if database_data==None:
        return jsonify(msg='akun tidak ditemukan'), 400
    else:
        data = {
            "jenis_kelamin" : input_jenis_kelamin,
            "tempat_lahir" : input_tempat_lahir,
            "tanggal_lahir" : input_tanggal_lahir,
            "alamat" : input_alamat,
            "nomor_hp" : input_nomor_hp,
            "update_date" : datetime.datetime.now(),
        }
        session.query(data_diri).filter(data_diri.akun_id==akun_id).update(data)
        session.commit()
        return jsonify(msg='data diri berhasil diupdate!')

def tambahKelas(mentor_id):
    input_nama_kelas = request.json.get('nama_kelas')
    input_harga = request.json.get('harga')
    input_deskripsi = request.json.get('deskripsi')
    if input_nama_kelas==None or input_harga==None or input_deskripsi==None:
        return jsonify("Masukkan nama_kelas, harga, deskripsi!"), 400
    elif input_nama_kelas=='' or input_harga=='' or input_deskripsi=='':
        return jsonify("Masukkan nama_kelas, harga, deskripsi!"), 400 
    else:
        data = {
            'kelas_id' : uuid.uuid4().hex,
            'nama_kelas' : input_nama_kelas,
            'harga' : input_harga,
            'deskripsi' : input_deskripsi,
            'create_date' : datetime.datetime.now(),
            'mentor_id' : mentor_id
        }
        session.add(kelas(**data))
        session.commit()
        return jsonify(msg='Kelas berhasil ditambahkan!')

def showKelas():
    database_data = session.query(kelas).all()
    kelas_data = []
    for list in database_data:
        data_mentor = session.query(akun).filter(akun.akun_id==list.mentor_id).one()
        data = {
            'kelas_id' : uuid.uuid4().hex,
            'nama_kelas' : list.nama_kelas,
            'harga' : list.harga,
            'deskripsi' : list.deskripsi,
            'create_date' : list.create_date,
            'mentor' : {
                'nama_depan' : data_mentor.nama_depan,
                'nama_akhir' : data_mentor.nama_akhir,
                'akun_id' : data_mentor.akun_id
            }
        }
        kelas_data.append(data)
    return jsonify(kelas_data)

def hapusKelas(kelas_id):
    database_data = session.query(kelas).filter(kelas.kelas_id==kelas_id).first()
    if kelas_id==None:
        return jsonify(msg='isi kelas_id!'), 400
    elif database_data==None:
        return jsonify(msg='Kelas tidak ditemukan!'), 400
    else:
        session.delete(database_data)
        session.commit()
        return jsonify(msg='Kelas berhasil dihapus!')

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

def cekjoin():
    database_data =  session.query(akun, data_diri).filter(akun.akun_id==data_diri.akun_id).filter(akun.akun_id=='5232e86ee268444db4e8e8a134d681ac').first()
    kumpul=[]
    for data1, data2 in database_data:
        kumpul.append(data1.jenis_kelamin)
    #    kumpul.append(data2.jenis_kelamin)
    return f'{kumpul}'
    #session.delete(database_data)
    #session.commit()
    #return 'udah'
