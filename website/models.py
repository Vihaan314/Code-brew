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

class Ciphers(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)
    caeser_progress = db.Column(db.String(10000))
    atbash_progress = db.Column(db.String(10000))
    monoalphabetic_progress = db.Column(db.String(10000))
    vigenere_progress = db.Column(db.String(10000))
    trithemius_progress = db.Column(db.String(10000))
    affine_progress = db.Column(db.String(10000))    
    
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    current_encryption = db.Column(db.Integer, default=0)
    current_key = db.Column(db.String(10000), default="")
    fav_lang = db.Column(db.String(10000), default="")
    about_me = db.Column(db.String(20000), default="")
    colour_theme = db.Column(db.String(10000), default="")
    messages_sent = db.Column(db.Integer, default=0)
    
    notes = db.relationship("Note")
    cipherprogress = db.relationship("Ciphers", uselist=False, backref="user")

    def __init__(self, email, first_name, password):
        self.email = email
        self.password = password
        self.first_name = first_name
        self.current_encryption = 6
        self.current_key = "17 20"
        self.fav_lang = "Java"
        self.about_me = "I like cheese"
        self.colour_theme = "Hacking"
        self.messages_sent = 0
        self.cipherprogress = Ciphers(caeser_progress = "Beginner", atbash_progress = "Beginner", monoalphabetic_progress = "Beginner", vigenere_progress = "Beginner", trithemius_progress = "Beginner", affine_progress = "Beginner")



"""
1 = Caeser Cipher
2 = Atbash Cipher
3 = Monoalphabetic cipher
4 = Vigenere Cipher 
5 = Trithemius Cipher
6 = Affine Cipher
"""