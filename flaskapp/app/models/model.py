from sqlalchemy import create_engine, Column, Integer, String, Date, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

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
   agama = Column(String)
   alamat = Column(String)
   nomor_hp = Column(String)
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

