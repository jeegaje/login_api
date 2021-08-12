from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+mysqlconnector://admin:admin123@localhost:3306/monggaweb', echo = True)
Session = sessionmaker(bind=engine)
session = Session()

if session:
    print("Connection Success")

Base = declarative_base()

class User(Base):
   __tablename__ = 'user'
   user_id = Column(Integer, primary_key =  True)
   user_email = Column(String)
   user_password = Column(String)