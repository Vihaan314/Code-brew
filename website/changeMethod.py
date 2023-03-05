from flask import Blueprint, render_template, request, flash, jsonify, session
from flask_login import login_required, current_user
# from . import Note
from .models import User, Note
# from .models import History
from . import db
import json
from . import misc
from . import encryptDecrypt
from . import changeMethod

views = Blueprint('views', __name__)

users = {}


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():    
    messages = Note.query.all()
    
    global method
    global key
    method = ""
    key = ""

    global Caeser
    global ascending
    global Mono
    global Vig
    global affineAB
    global affineA
    global affineB
    global newVal
    global newKey
    Caeser = ""
    ascending = "" 
    Mono = ""
    Vig = ""
    affineAB = ""
    affineA = ""
    affineB = ""
    newVal = ""
    newKey = ""

    if request.method == "POST":
        newVal = " ".join(request.values.to_dict().values())
        newKey = "".join(request.values.to_dict().keys())
        if newKey == "CaeserShift":
            Caeser = newVal
            method = "Caeser"
            key = Caeser
        elif newKey == "key":
            Vig = newVal
        elif newKey == "alphabet":
            Mono = newVal
        elif newKey == "chk":
            ascending = newVal
        elif newKey == "keyAkeyB":
            affineA = newVal.split()[0]
            affineB = newVal.split()[1]

    
    # changeMethod.newEncrypt()

    userNames = [i.user_id for i in messages]
    noteData = []

    for i in range(0, len(messages)):
        if messages[i].encryption == 1:
            shift = messages[i].message_key
            messages[i].data = encryptDecrypt.decryptVigenere(messages[i].data, shift)
            
        if messages[i].encryption == 2:
            messages[i].data = encryptDecrypt.decryptAtbash(messages[i].data)
            
        if messages[i].encryption == 3:
            alphabet = messages[i].message_key
            messages[i].data = encryptDecrypt.decryptMono(messages[i].data, alphabet)
            
        if messages[i].encryption == 4:
            key = messages[i].message_key
            messages[i].data = encryptDecrypt.decryptVigenere(messages[i].data, key)

        if messages[i].encryption == 5:
            order = messages[i].message_key
            if order == "Ascending":
                messages[i].data = encryptDecrypt.decryptTrithemius(messages[i].data, ascending=True)
            elif order == "Descending":
                messages[i].data = encryptDecrypt.decryptTrithemius(messages[i].data, ascending=False)

        if messages[i].encryption == 6:
            a = int(messages[i].message_key.split()[0])
            b = int(messages[i].message_key.split()[1])
            messages[i].data = encryptDecrypt.decryptAffine(messages[i].data, a, b)

    return render_template("home.html", user=current_user, 
                                        userName = current_user.first_name,
                                        trySessions =  [User.query.get(i).first_name for i in range(1, 8)],
                                        usersNum = len([User.query.get(i).first_name for i in range(1, 8)]),
                                        messages = messages,
                                        noteData = noteData,
                                        userNames = userNames,
                                        caeserShift = Caeser,
                                        vigKey = Vig,
                                        MonoAlpha = Mono,
                                        TrithOrder = ascending,
                                        affineKeys = affineAB,
                                        affineA = affineA,
                                        affineB = affineB
                                        )
