from sqlalchemy import create_engine, Column, Integer, String, Date, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.expression import update

engine = create_engine('mysql+mysqlconnector://admin:admin123@localhost:3306/monggaweb', echo = True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class akun(Base):
   __tablename__ = 'akun'
   akun_id = Column(String, primary_key =  True)
   nama_depan = Column(String)
   nama_akhir = Column(String)
   email = Column(String)
   sandi = Column(String)
   tipe_akun = Column(String)
   create_date = Column(DateTime)

class data_diri(Base):
   __tablename__ = 'data_diri'
   data_diri_id = Column(String, primary_key =  True)
   jenis_kelamin = Column(String)
   tempat_lahir = Column(String)
   tanggal_lahir = Column(Date)
   alamat = Column(String)
   nomor_hp = Column(String)
   update_date = Column(DateTime)
   akun_id = Column(String)

class contact_us(Base):
   __tablename__ = 'contact_us'
   id = Column(String, primary_key =  True)
   perihal = Column(String)
   nama = Column(String)
   email = Column(String)
   subjek = Column(String)
   pesan = Column(String)
   create_date = Column(DateTime)

class kelas(Base):
   __tablename__ = 'kelas'
   kelas_id = Column(String, primary_key =  True)
   nama_kelas = Column(String)
   harga = Column(String)
   deskripsi = Column(String)
   create_date = Column(DateTime)
   mentor_id = Column(String)

class wishlist(Base):
   __tablename__ = 'wishlist'
   wishlist_id = Column(String, primary_key =  True)
   update_date = Column(DateTime)
   user_id = Column(String)

class wishlist_kelas(Base):
   __tablename__ = 'wishlist_kelas'
   wishlist_id = Column(String, primary_key =  True)
   kelas_id = Column(String)
