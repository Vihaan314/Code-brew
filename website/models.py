from website import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    encryption = db.Column(db.Integer)
    message_key = db.Column(db.String(10000))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    current_encryption = db.Column(db.Integer)
    current_key = db.Column(db.String(10000))
    fav_lang = db.Column(db.String(10000))
    about_me = db.Column(db.String(20000))
    colour_theme = db.Column(db.String(10000))
    messages_sent = db.Column(db.Integer)
    
    notes = db.relationship("Note")

"""
1 = Caeser Cipher
2 = Atbash Cipher
3 = Monoalphabetic cipher
4 = Vigenere Cipher 
5 = Trithemius Cipher
6 = Affine Cipher
"""