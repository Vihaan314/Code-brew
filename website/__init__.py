from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager, current_user
from flask_socketio import SocketIO, send
from . import encryptDecrypt
import os

# from flask_login import UserMixin
# from sqlalchemy.sql import func


db = SQLAlchemy()
DB_NAME = "database.db"

def getMethod():
    from .models import Note, User
    user_encryption = User.query.filter_by(first_name=current_user.first_name).order_by(User.current_encryption).first().current_encryption
    if user_encryption == 1:
        return "Caeser"
    if user_encryption == 2:
        return "Atbash"
    if user_encryption == 3:
        return "Mono"
    if user_encryption == 4:
        return "Vigenere"
    if user_encryption == 5:
        return "Trithemius"
    if user_encryption == 6:
        return "Affine"
    
def getKey():
    from  .models import Note, User
    user_key = User.query.filter_by(first_name=current_user.first_name).order_by(User.current_encryption).first().current_key
    return user_key

def saveMessage(msg, usersNum=0):
    from .models import User, Note
    method = getMethod()
    key = getKey()
    receiver= "".join([str(i) for i in range(1, usersNum+1)])
    
           
    if method == "Caeser":
        message = Note(data=msg, user_id=current_user.id, encryption=1, message_key=key)
        message.data = encryptDecrypt.caeserCipher(message.data, int(key))
        
    if method == "Atbash":
        message = Note(data=msg, user_id=current_user.id, encryption=2, message_key="NULL")
        message.data = encryptDecrypt.atbashCipher(message.data)

    if method == "Mono":
        message = Note(data=msg, user_id=current_user.id, encryption=3, message_key=key)
        message.data = encryptDecrypt.monoCipher(message.data, key)

    if method == "Vigenere":
        message = Note(data=msg, user_id=current_user.id, encryption=4, message_key=key)
        message.data = encryptDecrypt.vigCipher(message.data, key)

    if method == "Trithemius":
        message = Note(data=msg, user_id=current_user.id, encryption=5, message_key=key)
        if key == "Ascending":
            message.data = encryptDecrypt.trithCipher(message.data, ascending=True)
        else:
            message.data = encryptDecrypt.trithCipher(message.data, ascending=False)

    if method == "Affine":
        message = Note(data=msg, user_id=current_user.id, encryption=6, message_key=key)
        a = int(key.split()[0])
        b = int(key.split()[1])
        message.data = encryptDecrypt.affineCipher(message.data, a, b)

    print(message)
    
    db.session.add(message)
    messagesSent = len(list(filter(lambda x: x.user_id == current_user.id, Note.query.all())))
    currentUser = User.query.filter_by(first_name=current_user.first_name).order_by(User.messages_sent).first()
    currentUser.messages_sent = messagesSent
    db.session.commit()

# def deleteMessage(id):
#     from .models import User
#     User.query.filter(User.id == id).delete()
#     db.session.commit()
def deleteMessage(user):
    from .models import User, Note
    User.query().filter(User.id == user.id).update({'notes': None})

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.urandom(12)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note

    with app.app_context():
        db.create_all()


    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app
