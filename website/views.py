from flask import Blueprint, render_template, request, flash, jsonify, session
from flask_login import login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import math
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

playedAnimation = ""

@views.route('/vig_step', methods=['POST'])
def vig_step():
    playedAnimation = list(request.form)
    if playedAnimation:
        return playedAnimation[0]



@views.route('/', methods=['GET', 'POST'])
@login_required
def home():    
    messages = Note.query.all()
    
    newKey = ""
    newVal = ""
    playground = ""
    playgroundD = ""
    playgroundE = ""
    
    shiftLearnCaeser, shiftAlphabetLearnCaeser = misc.randomAlphabet()
    shiftLearnCaeserInWords = misc.getShiftInWords(shiftLearnCaeser)
    randomWordLearnCaeser = misc.randomWord()
    randomWordLearnCaeserEncrypted = encryptDecrypt.caeserCipher(randomWordLearnCaeser, shiftLearnCaeser)

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

    playgroundUse = ""

    playgroundKey = ""
    playgroundMethod = ""
    playgroundA = ""
    playgroundB = ""
    playgroundIndices = ""
    playgroundILen = ""
    alphabetVisual = ""
    vigJ = ""
    
    shiftDecrypted = ""
    shiftKey = ""

    encryptRandom = ""
    randomKey = ""

    decryptedVigenere = ""
    vigenereKey = ""
    
    frequencies, bigraphs, trigraphs = "", "", ""
    freqAnalysis = ""

    randSentence = ""
    solvedCryptogram = ""
    cryptogramInput = ""

    practiceCaeserSolved = ""
    practiceCaeserInput = ""

    q1Res = q2Res = q3Res = q4Res = q5Res = ""
    totalMarkCaeser = percentageCaeser = ""

    q3 = q4 = q5 = ""

    if request.method == "POST":
        randSentence = misc.randomSentence()
        randomKey = random.randint(1, 27)
        encryptRandom = encryptDecrypt.caeserCipher(randSentence, randomKey)
        


        newVal = " ".join(request.values.to_dict().values())
        newKey = "".join(request.values.to_dict().keys())
        print("NEW KEY IS THIS", newKey)

        playground = newVal
        playgroundThings = request.form
        if newKey == "userNamefavLangaboutmepasswordconfirm_password":
            if request.form["userName"]:
                newuserName = request.form["userName"]
                if " " not in newuserName:
                    user_encryption.first_name = newuserName
                    db.session.commit()
            if request.form["favLang"]:
                newfavLang = request.form["favLang"]
                if newfavLang.lower() in ["python", "java", "c++", "c", "c#"]:
                    user_encryption.fav_lang = newfavLang.title()
                    db.session.commit()
            if request.form["aboutme"]:
                newaboutme = request.form["aboutme"]
                user_encryption.about_me = newaboutme
                db.session.commit()
            if request.form["password"] and request.form["confirm_password"]:
                new_password = request.form["password"]
                confirmed_password = request.form["confirm_password"]
                if len(new_password) < 7:
                    flash('Password must be at least 7 characters.', category='error')
                elif new_password != confirmed_password:
                    flash('Passwords don\'t match.', category='error')
                else:
                    user_encryption.password = generate_password_hash(
                    new_password, method='sha256')
                    db.session.commit()
            

        if newKey == "shiftBreakervigenereBreakerfreqAnalysis":
            if request.form["shiftBreaker"]:
                ciphertext = request.form["shiftBreaker"]
                shiftDecrypted, shiftKey = encryptDecrypt.crackShiftCipher(ciphertext)
            if request.form["vigenereBreaker"]:
                ciphertext = request.form["vigenereBreaker"]
                decryptedVigenere = encryptDecrypt.add_punctuation_back(ciphertext)
                vigenereKey = encryptDecrypt.vigenere_attack(ciphertext, range(0, 26))
            if request.form["freqAnalysis"]:
                ciphertext = request.form["freqAnalysis"]
                frequencies, bigraphs, trigraphs = encryptDecrypt.frequencyAnalyis(ciphertext)
                freqAnalysis = [" ".join((frequencies)), ", ".join(bigraphs), ", ".join(trigraphs)]
                
                
        if newKey == "cryptogramInput":
            print(request.form["cryptogramInput"])
            cryptogramInput = request.form["cryptogramInput"]
            solvedCryptogram = False
            print("RANDOM SENTENCE", randSentence)
            if request.form["cryptogramInput"].lower().replace(" ", "") == randSentence.lower().replace(" ", ""):
                solvedCryptogram = True
            
        if newKey == "practiceCaeserInput":
            practiceCaeserInput = request.form["practiceCaeserInput"]
            practiceCaeserSolved = False
            if practiceCaeserInput.lower().replace(" ", "") == encryptDecrypt.caeserCipher("hello", 12):
                practiceCaeserSolved = True

        if newKey == "q1CaesercaeserOp1caeserOp2caeserOp3caeserOp4q3Caeserq4Caeserq5Caeser":
            q1 = request.form["q1Caeser"]
            q1Res = False

            q2Op1 = request.form["caeserOp1"]
            q2Op2 = request.form["caeserOp2"]
            q2Op3 = request.form["caeserOp3"]
            q2Op4 = request.form["caeserOp4"]
            q2Res = False
            print(q2Op1, q2Op2, q2Op3, q2Op4)
           
            q3 = request.form["q3Caeser"]
            q3Res = False

            q4 = request.form["q4Caeser"]
            q4Res = False

            q5 = request.form["q5Caeser"]
            q5Res = False

            if q1.replace(" ", "") == "26":
                q1Res = True
            if q2Op3 == "substitution":
                q2Res = True
            if q3.replace(" ", "").lower() == "kvzrklod":
                q3Res = True
            if q4.replace(" ", "").lower() == "hello":
                q4Res = True
            if q5.replace(" ", "").lower() == "cheese":
                q5Res = True    

            totalMarkCaeser = len(list(filter(lambda x: x == True, [q1Res, q2Res, q3Res, q4Res, q5Res])))
            percentageCaeser = (totalMarkCaeser / 5) * 100


        if newKey == "playgroundMethodplayEncryptencryptKeyplayDecryptdecryptKey":
            if request.form["playEncrypt"]:
                playgroundUse = "encrypt"

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
                        playgroundKey *= (math.ceil(len(request.form["playEncrypt"]) / len(playgroundKey)))
                        for i in range(0, len(request.form["playEncrypt"])):
                            if request.form["playEncrypt"][i] == " ":
                                playgroundKey = playgroundKey[0:i] + " " + playgroundKey[i:len(playgroundKey)] 
                        playgroundKey = playgroundKey[0:len(request.form["playEncrypt"])]

                        playgroundE = encryptDecrypt.vigCipher(request.form["playEncrypt"], request.form["encryptKey"])
                        plaintext = request.form["playEncrypt"]
                 

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
                playgroundUse = "decrypt"

                if playground.split()[0] not in ["Caeser", "Atbash", "Monoalphabetic", "Vigenere", "Trithemius", "Affine"]:
                    flash('Please choose an encryption method', category='error')
                elif not request.form["decryptKey"] and playground.split()[0] in ["Caeser", "Monoalphabetic", "Vigenere", "Trithemius", "Affine"]:
                    flash('Please enter a key', category='error')
                
                if playground.split()[0] == "Caeser":
                        playgroundMethod = "Caeser"

                        playgroundKey = request.form["decryptKey"]
                        playgroundE = encryptDecrypt.decryptCaeser(request.form["playDecrypt"], int(playgroundKey))
                        shiftedAlphabet = [encryptDecrypt.decryptCaeser("ABCDEFGHIJKLMNOPQRSTUVWXYZ", i) for i in range(1, int(playgroundKey)+1)]
                        plaintext = request.form["playDecrypt"]

                elif playground.split()[0] == "Atbash":
                    playgroundMethod = "Atbash"

                    playgroundE = encryptDecrypt.decryptAtbash(request.form["playDecrypt"])
                    shiftedAlphabet = ["ABCDEFGHIJKLMNOPQRSTUVWXYZ"[::-1]]
                    plaintext = request.form["playDecrypt"]
                    
                elif playground.split()[0] == "Monoalphabetic":
                    playgroundMethod = "Monoalphabetic"

                    playgroundKey = request.form["decryptKey"]
                    shiftedAlphabet = [request.form["decryptKey"]]
                    playgroundE = encryptDecrypt.decryptMono(request.form["playDecrypt"], playgroundKey)
                    plaintext = request.form["playDecrypt"]

                elif playground.split()[0] == "Vigenere":
                    playgroundMethod = "Vigenere"
                    alphabetVisual = np.array([encryptDecrypt.caeserCipher("ABCDEFGHIJKLMNOPQRSTUVWXYZ", i) for i in range(0, 26)])
                    playgroundKey = request.form["decryptKey"]
                    playgroundKey *= (math.ceil(len(request.form["playDecrypt"]) / len(playgroundKey)))
                    for i in range(0, len(request.form["playDecrypt"])):
                        if request.form["playDecrypt"][i] == " ":
                            playgroundKey = playgroundKey[0:i] + " " + playgroundKey[i:len(playgroundKey)] 
                    playgroundKey = playgroundKey[0:len(request.form["playDecrypt"])]

                    playgroundE = encryptDecrypt.decryptVigenere(request.form["playDecrypt"], request.form["decryptKey"])
                    plaintext = request.form["playDecrypt"]
                    vigWord = [i for i in range(0, len(playgroundE))]
                    vigJ = vigWord[1]

                elif playground.split()[0] == "Trithemius":
                    plaintext = request.form["playDecrypt"]
                    playgroundMethod = "Trithemius"
                    playgroundIndices = ",\n+".join(list(map(str, [i for i, c in enumerate(plaintext) if c == "l"])))
                    playgroundKey = request.form["decryptKey"]
                    if playgroundKey.lower() == "ascending":
                        playgroundE = encryptDecrypt.decryptTrithemius(request.form["playDecrypt"], ascending = True)
                    elif playgroundKey.lower() == "descending":
                        playgroundE = encryptDecrypt.decryptTrithemius(request.form["playDecrypt"], ascending = False)

                elif playground.split()[0] == "Affine":
                    playgroundMethod = "Affine"

                    playgroundKey = request.form["decryptKey"]
                    playgroundA = int(playgroundKey.split()[0])
                    playgroundB = int(playgroundKey.split()[1])
                    playgroundE = encryptDecrypt.decryptAffine(request.form["playDecrypt"], playgroundA, playgroundB)
                    plaintext = request.form["playDecrypt"]





                    
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
                                        playgroundUse = playgroundUse,
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
                    
                                        shiftDecrypted = shiftDecrypted,
                                        playedAnimation =playedAnimation,
                                        shiftKey = shiftKey,
                                        messages_sent = current_user.messages_sent,
                                        allUsers =  [User.query.get(i) for i in range(1, len(User.query.all())+1)],
                                        sentenceKey = randomKey,
                                        randomSentence = encryptRandom,
                           
                                        decryptedVigenere = decryptedVigenere,
                                        vigenereKey = vigenereKey,
                                        frequencies = frequencies,
                                        bigraphs = bigraphs,
                                        trigraphs = trigraphs,
                                        freqAnalysis = freqAnalysis,

                                        solvedCryptogram = solvedCryptogram,
                                        originalSentence = randSentence,
                                        cryptogramInput = cryptogramInput,

                                        shiftLearnCaeser = shiftLearnCaeser,
                                        shiftLearnCaeserInWords = shiftLearnCaeserInWords,
                                        shiftAlphabetLearnCaeser = shiftAlphabetLearnCaeser,
                                        randomWordLearnCaeser = randomWordLearnCaeser,
                                        randomWordLearnCaeserEncrypted = randomWordLearnCaeserEncrypted,

                                        isString = lambda x: x.isalpha(),
                                        filter = filter,

                                        practiceCaeserSolved = practiceCaeserSolved,
                                        practiceCaeserInput = practiceCaeserInput,

                                        caeserQ3Input = q3,
                                        caeserQ4Input = q4,
                                        caeserQ5Input = q5,
                                        
                                        q1Res = q1Res,
                                        q2Res = q2Res,
                                        q3Res = q3Res,
                                        q4Res = q4Res,
                                        q5Res = q5Res,
                                        totalMarkCaeser = totalMarkCaeser,
                                        percentageCaeser = percentageCaeser,
                                        )
