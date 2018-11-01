from flask_sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash
import psycopg2
from flask_login import UserMixin
from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app

import json


db = SQLAlchemy()

class User(UserMixin,db.Model):
  __tablename__ = 'account'
  id = db.Column(db.Integer, primary_key = True)
  email = db.Column(db.String(64), unique=True, index=True)
  username = db.Column(db.String(64), unique=True, index=True)
  pwdhash = db.Column(db.String(128))
  
  

  def __init__(self, firstname, lastname, email, username,password):
    self.firstname = firstname.title()
    self.lastname = lastname.title()
    self.email = email.lower()
    self.username= username.lower()
    self.set_password(password)
     
  def set_password(self, password):
    self.pwdhash = generate_password_hash(password)

  def check_password(self, password):
    return check_password_hash(self.pwdhash, password)


class tweets(db.Model):
  __tablename__ = 'tweets'
  id = db.Column(db.Integer, primary_key=True)
  body = db.Column(db.Text)
  timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
  author_id = db.Column(db.Integer, db.ForeignKey('account.id'))

  def __init__(self,body,timestamp):
    self.body = body
    self.timestamp = datetime.now()
    

  