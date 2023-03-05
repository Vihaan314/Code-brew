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
import numpy as np
import random

views = Blueprint('views', __name__)

vigJ = ""
@views.route('/vig_step')
def vig_step():
    vigJ = 2
    return jsonify({'vigJ': vigJ})


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():    
    messages = Note.query.all()
    
    newKey = ""
    newVal = ""
    playground = ""
    playgroundD = ""
    playgroundE = ""
    
    randomWords = ["Hello", "Cheese"]
    randomWord = random.choice(randomWords)

    user_encryption = User.query.filter_by(first_name=current_user.first_name).order_by(User.current_encryption).first()
    method = ""
    if user_encryption.current_encryption == 1:
        method = "Caeser"
    elif user_encryption.current_encryption == 2:
        method = "Atbash"
    elif user_encryption.current_encryption == 3:
        method = "Monoalphabetic"
    elif user_encryption.current_encryption == 4:
        method = "Vigenere"
    elif user_encryption.current_encryption == 5:
        method = "Trithemius"
    elif user_encryption.current_encryption == 6:
        method = "Affine"

    key = user_encryption.current_key
    playgroundThings = ""
    shiftedAlphabet = ""
    plaintext = ""
    vigWord = ""

    playgroundKey = ""
    playgroundMethod = ""
    playgroundA = ""
    playgroundB = ""
    playgroundIndices = ""
    playgroundILen = ""
    alphabetVisual = ""
    vigJ = ""
    
    if request.method == "POST":
        newVal = " ".join(request.values.to_dict().values())
        newKey = "".join(request.values.to_dict().keys())
        playground = newVal
        playgroundThings = request.form
        if newKey == "playgroundMethodplayEncryptencryptKeyplayDecrypt":
            if request.form["playEncrypt"]:
                if playground.split()[0] not in ["Caeser", "Atbash", "Monoalphabetic", "Vigenere", "Trithemius", "Affine"]:
                    flash('Please choose an encryption method', category='error')
                elif not request.form["encryptKey"] and playground.split()[0] in ["Caeser", "Monoalphabetic", "Vigenere", "Trithemius", "Affine"]:
                    flash('Please enter a key', category='error')
                else:  
                    if playground.split()[0] == "Caeser":
                        playgroundMethod = "Caeser"

                        playgroundKey = request.form["encryptKey"]
                        playgroundE = encryptDecrypt.caeserCipher(request.form["playEncrypt"], int(playgroundKey))
                        shiftedAlphabet = [encryptDecrypt.caeserCipher("ABCDEFGHIJKLMNOPQRSTUVWXYZ", i) for i in range(1, int(playgroundKey)+1)]
                        plaintext = request.form["playEncrypt"]

                    elif playground.split()[0] == "Atbash":
                        playgroundMethod = "Atbash"

                        playgroundE = encryptDecrypt.atbashCipher(request.form["playEncrypt"])
                        shiftedAlphabet = ["ABCDEFGHIJKLMNOPQRSTUVWXYZ"[::-1]]
                        plaintext = request.form["playEncrypt"]
                        
                    elif playground.split()[0] == "Monoalphabetic":
                        playgroundMethod = "Monoalphabetic"

                        playgroundKey = request.form["encryptKey"]
                        shiftedAlphabet = [request.form["encryptKey"]]
                        playgroundE = encryptDecrypt.monoCipher(request.form["playEncrypt"], playgroundKey)
                        plaintext = request.form["playEncrypt"]

                    elif playground.split()[0] == "Vigenere":
                        playgroundMethod = "Vigenere"
                        alphabetVisual = np.array([encryptDecrypt.caeserCipher("ABCDEFGHIJKLMNOPQRSTUVWXYZ", i) for i in range(0, 26)])
                        playgroundKey = request.form["encryptKey"]
                        
                        playgroundE = encryptDecrypt.vigCipher(request.form["playEncrypt"], playgroundKey)
                        plaintext = request.form["playEncrypt"]
                        vigWord = [i for i in range(0, len(playgroundE))]
                        vigJ = vigWord[1]

                    elif playground.split()[0] == "Trithemius":
                        plaintext = request.form["playEncrypt"]
                        playgroundMethod = "Trithemius"
                        playgroundIndices = ",\n+".join(list(map(str, [i for i, c in enumerate(plaintext) if c == "l"])))
                        playgroundKey = request.form["encryptKey"]
                        if playgroundKey.lower() == "ascending":
                            playgroundE = encryptDecrypt.trithCipher(request.form["playEncrypt"], ascending = True)
                        elif playgroundKey.lower() == "descending":
                            playgroundE = encryptDecrypt.trithCipher(request.form["playEncrypt"], ascending = False)

                    elif playground.split()[0] == "Affine":
                        playgroundMethod = "Affine"

                        playgroundKey = request.form["encryptKey"]
                        playgroundA = int(playgroundKey.split()[0])
                        playgroundB = int(playgroundKey.split()[1])
                        playgroundE = encryptDecrypt.affineCipher(request.form["playEncrypt"], playgroundA, playgroundB)
                        plaintext = request.form["playEncrypt"]
                    
            if request.form["playDecrypt"]:
                if playground.split()[0] == "Caeser":
                    playgroundD = encryptDecrypt.decryptCaeser(request.form["playDecrypt"], 3)
                    shiftedAlphabet = [encryptDecrypt.caeserCipher("ABCDEFGHIJKLMNOPQRSTUVWXYZ", i) for i in range(1, 4)]
                    plaintext = request.form["playDecrypt"]

                elif playground.split()[0] == "Atbash":
                    playgroundD = encryptDecrypt.decryptAtbash(request.form["playDecrypt"])
                elif playground.split()[0] == "Monoalphabetic":
                    playgroundD = encryptDecrypt.decryptMono(request.form["playDecrypt"], "QWERTYUIOPASDFGHJKLZXCVBNM")
                elif playground.split()[0] == "Vigenere":
                    playgroundD = encryptDecrypt.decryptVigenere(request.form["playDecrypt"], "KEY")
                elif playground.split()[0] == "Trithemius":
                    playgroundD = encryptDecrypt.decryptTrithemius(request.form["playDecrypt"], ascending = True)
                elif playground.split()[0] == "Affine":
                    playgroundD = encryptDecrypt.decryptAffine(request.form["playDecrypt"], 17, 20)
        key = newVal

        if newKey == "CaeserShift":
            user_encryption.current_encryption = 1
            user_encryption.current_key = key
            db.session.commit()
            method = "Caeser"

        elif newKey == "key":
            user_encryption.current_encryption = 4
            user_encryption.current_key = key
            db.session.commit()
            method = "Vigenere"

        elif newKey == "alphabet":
            user_encryption.current_encryption = 3
            user_encryption.current_key = key
            db.session.commit()
            method = "Monoalphabetic"

        elif newKey == "chk":
            user_encryption.current_encryption = 5
            user_encryption.current_key = key
            db.session.commit()
            method = "Trithemius"

        elif newKey == "keyAkeyB":
            user_encryption.current_encryption = 6
            user_encryption.current_key = key
            db.session.commit()
            method = "Affine"


    for i in range(0, len(messages)):
        if messages[i].encryption == 1:
            shift = messages[i].message_key
            messages[i].data = encryptDecrypt.decryptCaeser(messages[i].data, int(shift))
            
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
                                        trySessions =  [User.query.get(i).first_name for i in range(1, len(User.query.all())+1)],
                                        usersNum = len([User.query.get(i).first_name for i in range(1, len(User.query.all())+1)]),
                                        enumerate=enumerate,
                                        messages = messages ,
                                        proglang = User.query.filter_by(first_name=current_user.first_name).order_by(User.current_encryption).first().fav_lang,
                                        aboutme = User.query.filter_by(first_name=current_user.first_name).order_by(User.current_encryption).first().about_me,
                                        method = method,
                                        userE = user_encryption,
                                        newVal = newVal,
                                        newKey = newKey,
                                        playground = playground,
                                        playgroundE = playgroundE,
                                        playgroundD = playgroundD,
                                        playgroundThings = playgroundThings,
                                        shiftedAlphabet = shiftedAlphabet,
                                        plaintext = plaintext,
                                        plainUpper = plaintext.upper(),
                                        playgroundEUpper = playgroundE.upper(),
                                        playgroundKey = playgroundKey,
                                        playgroundKeyUpper = playgroundKey.upper(),
                                        playgroundMethod = playgroundMethod,
                                        playgroundA = str(playgroundA),
                                        playgroundB = str(playgroundB),
                                        playgroundIndices = playgroundIndices,
                                        playgroundILen = len(playgroundIndices),
                                        alphabetVisual = alphabetVisual,
                                        regularAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                                        randomWords = randomWords,
                                        randomWord = randomWord,
                                        vigWord = vigWord,
                                        vigJ = vigJ
                                        )