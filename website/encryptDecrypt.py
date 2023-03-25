import os
import math
import numpy as np
import nltk
from nltk.corpus import stopwords
from collections import Counter
from sympy import Matrix
from egcd import egcd
import string
from queue import Queue
import re


lowercase = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8,
         'j':9, 'k':10, 'l':11, 'm':12, 'n':13, 'o':14, 'p':15, 'q':16,
         'r':17, 's':18,  't':19, 'u':20, 'v':21, 'w':22, 'x':23, 'y':24,
         'z':25}

uppercase ={'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8,
         'J':9, 'K':10, 'L':11, 'M':12, 'N':13, 'O':14, 'P':15, 'Q':16,
         'R':17, 'S':18,  'T':19, 'U':20, 'V':21, 'W':22, 'X':23, 'Y':24,
         'Z':25}

inv_lowercase = {0:'a', 1:'b', 2:'c', 3:'d', 4:'e', 5:'f', 6:'g', 7:'h', 8:'i',
         9:'j', 10:'k', 11:'l', 12:'m', 13:'n', 14:'o', 15:'p', 16:'q',
         17:'r', 18:'s', 19:'t', 20:'u', 21:'v', 22:'w', 23:'x', 24:'y',
         25:'z'}

inv_uppercase = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H',
                 8:'I', 9:'J', 10:'K', 11:'L', 12:'M', 13:'N', 14:'O', 15:'P',
                 16:'Q', 17:'R', 18:'S', 19:'T', 20:'U', 21:'V', 22:'W', 23:'X',
                 24:'Y', 25:'Z'}

letterFrequency = {'e' : 12.7,
't' : 9.1,
'a' : 8.2,
'o' : 7.5,
'i' : 7.0,
'n' : 6.7,
's' : 6.3,
'h' : 6.1,
'r' : 6.0,
'd' : 4.3,
'l' : 4.0,
'u' : 2.8,
'c' : 2.8,
'm' : 2.4,
'w' : 2.3,
'f' : 2.2,
'g' : 2.0,
'y' : 2.0,
'p' : 1.9,
'b' : 1.5,
'v' : 1.0,
'k' : 0.8,
'j' : 0.2,
'x' : 0.1,
'z' : 0.1,
'q' : 0.1 }

"""
LEARN ABOUT THE DIFFERENT TYPES OF CIPHERS
"""
def learnCaeser():
    print("The Caesar cipher is a simple substitution cipher that involves replacing each letter in a message with a letter that is a certain number of positions down the alphabet.")
    print("For example, if the shift value is 3, then A would be replaced by D, B would be replaced by E, and so on.")
    print("To encrypt a message using the Caesar cipher, you would perform the following three simple steps:\n")
    print("1. Choose a shift value (also known as the key). This can be any integer between 1 and 25, but it is typically a small number.")
    print("2. For each letter in the message you want to encrypt, shift it down the alphabet by the shift value. For example, if the shift value is 3 and the letter is A, then it would be replaced by D. If the letter is Z and the shift value is 3, then it would be replaced by C.")
    print("3. Repeat this process for each letter in the message.")
    print("\nTo decrypt a message that has been encrypted using the Caesar cipher, you would simply perform the same process in reverse. For example, if the shift value is 3, then you would shift each letter in the encrypted message up the alphabet by 3 positions to get the original message.")
    print("It's important to note that the Caesar cipher is not very secure, as it can easily be broken using simple frequency analysis or by trying all 25 possible shift values (as demonstrated as one of the features of this program). It is mainly used for instructional purposes or as a simple way to encode messages for fun.")
def learnAtbash():
    print("The Atbash cipher is a simple substitution cipher that is used to encode a message by replacing each letter of the alphabet with its reverse. For instance, A would map to Z, and B would map to Y. Here are the steps to use the Atbash cipher:\n")
    print("1. Start by writing out the alphabet in order: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z")
    print("2. Reverse the alphabet: Z Y X W V U T S R Q P O N M L K J I H G F E D C B A")
    print("3. To encode a message, replace each letter of the message with the corresponding letter from the reversed alphabet. That means, the letter the same distance in the reversed alphabet as in the original alphabet. For example, to encode the message 'HELLO', you would replace each letter as follows:")
    print("H becomes S\nE becomes V\nL becomes O\nL becomes O\nO becomes L")
    print("Therefore, the encoded message would be 'SVOOL'\n")
    print("\nTo decode a message that has been encoded using the Atbash cipher, simply reverse the process and replace each letter with the corresponding letter from the original alphabet.\n")
    print("It's important to note that the Atbash cipher is not secure at all as the same steps are performed everytime. It can be easily broken by reversing the string again as that would bring it back to the original string. Therefore, when handed ciphertext, you can check if it is the atbash cipher by encrypting the ciphertext using the atbash cipher again to reach the original.")
def learnMonoalpha():
    print("A monoalphabetic cipher is a simple substitution cipher that uses a fixed replacement rule to replace each letter in the plaintext with another letter. The key to the cipher is the substitution rule, which specifies which letter should be replaced with which other letter.")
    print("Here are the steps for encrypting a message using a monoalphabetic cipher:\n")
    
def learnVigenere():
    pass
def learnHill():
    pass
def learnPlayfair():
    pass
"""
#LEARN ABOUT THE DIFFERENT TYPES OF CIPHERS
"""

"""
#SPIRAL CIPHER ENCRYPTION
def spiralCipher(message, start, rotation):
    pass

#SPIRAL CIPHER DECRYPTION
def decryptSpiral(message, start, rotation):
    pass

#MORBIT CIPHER ENCRYPTION
def morbitCipher(message, key):
    pass

#MORBIT CIPHER DECRYPTION
def decryptMorbit(message, key):
    pass
"""
#SPIRAL CIPHER
#MORBIT CIPHER



##MAKE THIS LIBRARY
"""
IMPLEMENTATIONS
"""
#CAESER CIPHER
#ROT13 CIPHER
#TRITHEMIUS CIPHER
#ATBASH CIPHER
#MONOALPHABETIC CIPHER
#VIGENERE CIPHER
#TRANSPOSITION CIPHER
#AFFINE CIPHER
#HILL CIPHER
#PLAYFAIR CIPHER

#CAESER CIPHER ENCRYPTION
def caeserCipher(message, key, decrypt = 1): #DONE
    newChars = []
    for char in message:
        if char.isalpha():
            if char.isupper():
                newChar = chr((ord(char) - 65 + decrypt*key) % 26 + 65)
            else:
                newChar = chr((ord(char) - 97 + decrypt*key) % 26 + 97)
        else:
            newChar = char
        newChars.append(newChar)
    return "".join(newChars)

#CAESER CIPHER DECRYPTION
def decryptCaeser(message, key): #DONE=
    return caeserCipher(message, key, decrypt= -1)

#ROT13 ENCRYPTION
def rot13Cipher(message): #DONE
    return caeserCipher(message, 13)

#ROT13 DECRYPTION
def decryptRot13(message): #DONE
    return decryptCaeser(message, 13)

#TRITHEMIUS CIPHER ENCRYPTION
def trithCipher(message, ascending): #DONE 
    if ascending:
        newChars = "".join([caeserCipher(message.replace(" ", "")[i], i) for i in range(0, len(message.replace(" ", "")))])
        for i in range(0, len(message)):
            if message[i] == " ":
                newChars = newChars[0:i] + " " + newChars[i:]
        return newChars
    
    newChars = "".join([decryptCaeser(message.replace(" ", "")[i], i) for i in range(0, len(message.replace(" ", "")))])
    for i in range(0, len(message)):
        if message[i] == " ":
            newChars = newChars[0:i] + " " + newChars[i:]
    return newChars
#ADD "INITIAL SHIFT" PARAMETER

#TRITHEMIUS CIPHER DECRYPTION
def decryptTrithemius(message, ascending):
    return trithCipher(message, ascending=False) if ascending else trithCipher(message, ascending=True)
    
#ATBASH CIPHER ENCRYPTION  
def atbashCipher(message): #DONE
    messCaps = message
    atbash = {chr(i + 97): chr(122 - i) for i in range(0, 26)}
    encrypted = [atbash.get(i.lower(), i) for i in message]
    return "".join([encrypted[i].upper() if messCaps[i].isupper() else encrypted[i] for i in range(0, len(messCaps))])

#ATBASH CIPHER DECRYPTION
def decryptAtbash(message): #DONE
    return atbashCipher(message)

#MONOALPHABETIC CIPHER ENCRYPTION
def monoCipher(message, key): #DONE
    messCaps = message
    message = message.upper()
    encrypted = message.translate(str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZ", key))
    return "".join([encrypted[i].lower() if messCaps[i].islower() else encrypted[i] for i in range(0, len(messCaps))])

#MONOALPHABETIC CIPHER DECRYPTION
def decryptMono(message, key): #DONE
    messCaps = message
    message = message.upper()
    decrypted = message.translate(str.maketrans(key, "ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    return "".join([decrypted[i].lower() if messCaps[i].islower() else decrypted[i] for i in range(0, len(messCaps))])

#VIGENERE CIPHER ENCRYPTION
def vigCipher(message, key): #DONE
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    messCaps = message
    message = message.upper()
    key = key.upper()
    mL = len(message.replace(" ", ""))    
    key *= (math.ceil(mL / len(key)))
    for i in range(0, len(message)):
        if message[i] == " ":
            key = key[0:i] + " " + key[i:len(key)]    
    key = key[0:len(message)]
    encrypted = []
    for i in range(0, len(message)):
        if message[i].isalpha() == False:
            encrypted.append(message[i])
        elif alphabet.index(message[i]) + alphabet.index(key[i]) < 26:   
            encrypted.append(chr((alphabet.index(message[i]) + alphabet.index(key[i])) + 65))
        elif alphabet.index(message[i]) + alphabet.index(key[i]) > 25:
            encrypted.append(chr((alphabet.index(message[i]) + alphabet.index(key[i])) % 26 + 65))
    return "".join([encrypted[i].lower() if messCaps[i].islower() else encrypted[i] for i in range(0, len(messCaps))])

#VIGENERE CIPHER DECRYPTION
def decryptVigenere(message, key): #DONE
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    messCaps = message
    message = message.upper()
    key = key.upper()
    mL = len(message.replace(" ", ""))    
    key *= (math.ceil(mL / len(key)))
    for i in range(0, len(message)):
        if message[i] == " ":
            key = key[0:i] + " " + key[i:len(key)]      
    key = key[0:len(message)]
    decrypted = []
    for i in range(0, len(message)):
        if message[i].isalpha() == False:
            decrypted.append(message[i])
        elif alphabet.index(message[i]) < alphabet.index(key[i]):
            decrypted.append(alphabet[(26 - (alphabet.index(key[i]) - alphabet.index(message[i])))])
        else:
            decrypted.append(alphabet[(alphabet.index(message[i])+1) - alphabet.index(key[i])-1])
    return "".join([decrypted[i].lower() if messCaps[i].islower() else decrypted[i] for i in range(0, len(messCaps))])

#TRANSPOSITION CIPHER ENCRYPTION
def transposCipher(message, key):
    cipher = ""
    kIdx = 0
    row = int(math.ceil(float(len(message)) / len(key)))
    spaceFill = int((row * len(key)) - float(len(message)))
    message = list(message) + list("_"*spaceFill)
    matrix = [message[i: i + len(key)] for i in range(0, len(message), len(key))]
    for i in range(len(key)):
        cIdx = key.index(sorted(list(key))[kIdx])
        cipher += "".join([j[cIdx] for j in matrix])
        kIdx += 1
    return cipher

#TRANSPOSITION CIPHER DECRYPTION
def decryptTransposition(cipher, key):
    message = ""
    kIdx = 0
    mIdx = 0
    m = list(cipher)
    k = sorted(list(key))
    decrypted = [[None] * len(key) for i in range(0, int(math.ceil(len(cipher) / len(key))))]
    for i in range(0, len(key)):
        cIdx = key.index(k[kIdx])
        for j in range(0, int(math.ceil(len(cipher) / len(key)))):
            decrypted[j][cIdx] = m[mIdx]
            mIdx += 1
        kIdx += 1
    message = "".join(sum(decrypted, []))
    spaceCount = message.count("_")
    if spaceCount > 0:
        return message[: -spaceCount]
    return message

#AFFINE CIPHER ENCRYPTION
def affineCipher(message, a, b):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypted = [(alphabet[(a * alphabet.index(i.lower()) + b) % 26]).upper() if i.isupper() else alphabet[(a * alphabet.index(i.lower()) + b) % 26] if i.isalpha() else i for i in message]
    return "".join(encrypted)

#AFFINE CIPHER DECRYPTION
def decryptAffine(message, a, b):
    messSpaces = message
    messCaps = message
    message = message.replace(" ", "").lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    gcd, x, y = egcd(a, len(alphabet))
    if gcd != 1:
        return "Modular inverse does not exist"
    else:
        aInv = x % len(alphabet)        
    messageAlpha = [alphabet.index(i) if i in alphabet else i for i in message]
    decrypted = [(aInv*(i - b))%26 if isinstance(i, int) else i for i in messageAlpha]
    decrypted = "".join([alphabet[i] if isinstance(i, int) else i for i in decrypted])
    for i in range(0, len(messSpaces)):
        if messSpaces[i] == " ":
            decrypted = decrypted[0:i] + " " + decrypted[i:]
    return "".join([decrypted[i].upper() if messCaps[i].isupper() else decrypted[i].lower() for i in range(0, len(messCaps))])
  

#HILL CIPHER ENCRYPTION (K * P)
def hillCipher(message, key): #DONE
    if len(message) % int(math.sqrt(len(key))) != 0:
        return "Wrong key. Please enter a key of the same / factor of the key length"
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message = [message[i:i+int(math.sqrt(len(key)))] for i in range(0, len(message), int(math.sqrt(len(key))))]
    k = np.array([alphabet.index(i) for i in key]).reshape(int(math.sqrt(len(key))), int(math.sqrt(len(key))))
    if len(message) == 1:
        message = "".join(message)
        m = np.array([alphabet.index(i) for i in message]).reshape(len(message), 1)
        km = (k @ m) % 26
        return "".join(alphabet[i[0]] for i in km)
    else:
        mess = []
        for i in range(0, len(message)):
            mess.append(np.array([alphabet.index(j) for j in message[i]]).reshape(len(message[i]), 1))
        keyMess = [((k @ mess[i]) % 26) for i in range(0, len(mess))]
        encrypted = [alphabet[keyMess[i][j][0]] for i in range(0, len(keyMess)) for j in range(0, len(keyMess[i]))]
        return "".join(encrypted)

#HILL CIPHER DECRYPTION (K^(-1) (mod 26) * P)
def decryptHill(message, key): #DONE
    if len(message) % int(math.sqrt(len(key))) != 0:
        return "Wrong key. Key needs to be of the same / factor of the key length"
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    k = Matrix([alphabet.index(i) for i in key]).reshape(int(math.sqrt(len(key))), int(math.sqrt(len(key))))
    KInv = np.array(k.inv_mod(26))
    message = [message[i:i+int(math.sqrt(len(key)))] for i in range(0, len(message), int(math.sqrt(len(key))))]
    if len(message) == 1:
        message = "".join(message)
        m = np.array([alphabet.index(i) for i in message]).reshape(len(message), 1)
        decryptMat = np.array((KInv @ m) % 26)
        return "".join([alphabet[i[0]] for i in decryptMat])
    else:
        mess = []
        for i in range(0, len(message)):
            mess.append(np.array([alphabet.index(j) for j in message[i]]).reshape(len(message[i]), 1))
        decryptMats = [(KInv @ mess[i]) % 26 for i in range(0, len(mess))]
        decrypted = [alphabet[decryptMats[i][j][0]] for i in range(0, len(decryptMats)) for j in range(0, len(decryptMats[i]))]
        return "".join(decrypted)

#PLAYFAIR CIPHER ENCRYPTION
def playfairCipher(message, key, fillerLetter = "z", decrypt = 1):
    messSpaces = message
    message = message.replace(" ", "").lower()
    def FillerLetter(text):
        k = len(text)
        if k % 2 == 0:
            for i in range(0, k, 2):
                if text[i] == text[i+1]:
                    filledWord = text[0:i+1] + "x" + text[i+1:]
                    filledWord = FillerLetter(filledWord)
                    break
                else:
                    filledWord = text
        else:
            for i in range(0, k-1, 2):
                if text[i] == text[i+1]:
                    filledWord = text[0:i+1] + "x" + text[i+1:]
                    filledWord = FillerLetter(filledWord)
                    break
                else:
                    filledWord = text
        return filledWord
    if decrypt == 1:
        text = FillerLetter(message.replace("j", "i"))
        messSplit = [text[i:i+2] for i in range(0, len(text), 2)]    
        if (len(messSplit[-1]) != 2) and (messSplit[-1] != "z"):
            messSplit[-1] = messSplit[-1]+ fillerLetter
        elif (len(messSplit[-1]) != 2) and (messSplit[-1] == "z"):
            messSplit[-1] = messSplit[-1]+"x"
    elif decrypt == -1:
        messSplit = [message[i:i+2] for i in range(0, len(message), 2)]

    remainingAlpha = "".join(list(filter(lambda x: x not in key.lower(), "abcdefghiklmnopqrstuvwxyz")))
    key = "".join(dict.fromkeys(key.replace("j", "i"))).lower()
    keyAlpha = np.array([(i) for i in (key+remainingAlpha)]).reshape(5, 5)
    decrypted = {}
    decryptTry = []
    for i in range(0, 5):
        for j in range(0, len(messSplit)):
            if (np.where(keyAlpha == messSplit[j][0])[0]) == (np.where(keyAlpha == messSplit[j][1])[0]):
                el1Row = (int(np.where(keyAlpha == messSplit[j][0])[0]))
                el1Col = ((int(np.where(keyAlpha == messSplit[j][0])[1]) + decrypt)) % 5
                el2Row = (int(np.where(keyAlpha == messSplit[j][1])[0]))
                el2Col = ((int(np.where(keyAlpha == messSplit[j][1])[1]) + decrypt)) % 5
                decrypted[messSplit[j][0] + messSplit[j][1]] = [keyAlpha[el1Row][el1Col], keyAlpha[el2Row][el2Col]]
            elif (messSplit[j][0] in keyAlpha[ :,i]) and (messSplit[j][1] in keyAlpha[ :,i]):
                decrypted[messSplit[j][0] + messSplit[j][1]] = ([keyAlpha[ :,i][(np.where(keyAlpha[ :,i] == messSplit[j][0])[0][0] + decrypt) % 5],
                                                                 keyAlpha[ :,i][(np.where(keyAlpha[ :,i] == messSplit[j][1])[0][0] + decrypt) % 5]])
            
            elif ((messSplit[j][0] not in keyAlpha[ :,i]) and (messSplit[j][1] not in keyAlpha[ :,i])) and ((messSplit[j][0] not in keyAlpha[i, :]) and (messSplit[j][1] not in keyAlpha[i, :])):
                charWhereOne = np.where(keyAlpha == messSplit[j][0])
                charWhereTwo = np.where(keyAlpha == messSplit[j][1])
                el1 = charWhereOne[0].tolist() + charWhereOne[1].tolist()
                el2 = charWhereTwo[0].tolist() + charWhereTwo[1].tolist()
                
                if el1[1] > el2[1]:  
                    remainingMat = np.transpose(np.array(
                        [keyAlpha[i][j] for j in range(min([el1[1], el2[1]]), max([el1[1], el2[1]])+1) for i in range(min([el1[0], el2[0]]), max([el1[0], el2[0]])+1)]).reshape(
                                                                                                                                    abs(el2[1]-el1[1])+1, abs(el2[0]-el1[0])+1))
                    if remainingMat[0][0] in messSplit[j]:
                        lets = [(remainingMat[0][len(remainingMat[0])-1]), remainingMat[len(remainingMat)-1][0]][::-1]
                    elif remainingMat[0][len(remainingMat[0])-1] == messSplit[j][0]:
                        lets = [remainingMat[0][0], remainingMat[len(remainingMat)-1][len(remainingMat[0])-1]]
                    else:
                        lets = [remainingMat[0][0], remainingMat[len(remainingMat)-1][len(remainingMat[0])-1]][::-1]
                    decrypted[messSplit[j][0] + messSplit[j][1]] = lets
                    
                if el1[1] < el2[1]:                        
                    remainingMat = np.transpose(np.array(
                        [keyAlpha[i][j] for j in range(min([el2[1], el1[1]]), max(el2[1], el1[1])+1) for i in range(min([el2[0], el1[0]]), max(el2[0], el1[0])+1)]).reshape(
                                                                                                                                    abs(el2[1]-el1[1])+1, (abs(el2[0]-el1[0]) + 1)))
                    if remainingMat[0][0] in messSplit[j]:
                        lets = [remainingMat[len(remainingMat)-1][0], (remainingMat[0][len(remainingMat[0])-1])][::-1]
                    elif remainingMat[0][len(remainingMat[0])-1] in messSplit[j]:
                        lets = [remainingMat[0][0], remainingMat[len(remainingMat)-1][len(remainingMat[0])-1]][::-1]
                    else:
                        lets = [remainingMat[0][0], remainingMat[len(remainingMat)-1][len(remainingMat[0])-1]]
                    decrypted[messSplit[j][0] + messSplit[j][1]] = lets
                    
    decrypted = "".join(["".join(decrypted[i]) for i in messSplit])
    for i in range(0, len(messSpaces)):
        if messSpaces[i] == " ":
            decrypted = decrypted[0:i] + " " + decrypted[i:len(decrypted)]
    return decrypted.upper()
            
#PLAYFAIR CIPHER DECRYPTION
def decryptPlayfair(message, key):
    return playfairCipher(message, key, decrypt = -1)




"""
CODEBREAKERS
"""

def frequencies(ciphertext):
    cipherUpdated = "".join(e for e in ciphertext if e.isalnum()).lower()
    freqDict = Counter(cipherUpdated)
    return freqDict, cipherUpdated

def crackShiftCipher(ciphertext):
    letterFrequency = {'e' : 12.7,
        't' : 9.1,
        'a' : 8.2,
        'o' : 7.5,
        'i' : 7.0,
        'n' : 6.7,
        's' : 6.3,
        'h' : 6.1,
        'r' : 6.0,
        'd' : 4.3,
        'l' : 4.0,
        'u' : 2.8,
        'c' : 2.8,
        'm' : 2.4,
        'w' : 2.3,
        'f' : 2.2,
        'g' : 2.0,
        'y' : 2.0,
        'p' : 1.9,
        'b' : 1.5,
        'v' : 1.0,
        'k' : 0.8,
        'j' : 0.2,
        'x' : 0.1,
        'z' : 0.1,
        'q' : 0.1 }
    freqDict, cipherUpdated = frequencies(ciphertext)
    differences = []
    sum = 0
    for key in range(0, 26):
        possible_decryption = decryptCaeser(ciphertext, key)
        for letter in list(possible_decryption):
            if letter in letterFrequency.keys():
                probability = (1/26) * (letterFrequency[letter] / len(cipherUpdated))
                sum += probability
        differences.append(sum)
        sum = 0

    decryptedKey = np.where(differences == np.max(differences))[0][0]
    decryption = decryptCaeser(ciphertext, decryptedKey)

    return decryption, decryptedKey

# def crackVigenereCipher(ciphertext):
#     def lowestDiv(n):
#         return min([i for i in range(2, int(math.sqrt(n)) + 1) if n % i == 0] + [n])

#     print(ciphertext, "\n")
#     freqDict, cipherUpdated = frequencies(ciphertext.lower())
#     tri = list(filter(lambda x: len(x) == 3, ciphertext.split()))
#     triSet = set(list(filter(lambda x: len(x) == 3, ciphertext.split())))
#     triDuplicates = set(list(filter(lambda x: Counter(tri)[x]>1, tri)))
#     hasDuplicates = not(len(triSet) == len(tri))
#     triDuplicateLens = [{i: (len("".join([j for j in ciphertext.split(i)[1] if j.isalpha()]))+3, lowestDiv(len("".join([j for j in ciphertext.split(i)[1] if j.isalpha()]))+3)) } for i in triDuplicates]
#     triDuplicateLens2 = np.array([[ciphertext.split(i)] for i in triDuplicates])
#     print(triDuplicateLens)
# ##    print(triDuplicateLens2)
# ##    print(hasDuplicates)
# ##    print(tri)
# ##    print(triSet)
#     print(triDuplicates)
# ##    print(freqDict)
    


K = range(0, 26)  # the key space


def vigenere_encryption(plaintext, key):

    ciphertext = ""
    plaintext_updated = ''.join(e for e in plaintext if e.isalnum())

    for i in range(0, len(plaintext_updated)):
        element = plaintext_updated[i]
        if element.lower() in letterFrequency.keys():
            cipher_element = (lowercase[element.lower()] + lowercase[key[i % len(key)].lower()]) % 26
            encrypted_letter = inv_lowercase[cipher_element]
            ciphertext += encrypted_letter
        else:
            ciphertext += element

    return ciphertext


def vigenere_decryption(ciphertext, key):

    plaintext = ""
    ciphertext_updated = ''.join(e for e in ciphertext if e.isalnum())

    for i in range(0, len(ciphertext_updated)):
        element = ciphertext_updated[i]
        if element.lower() in letterFrequency.keys():
            plain_element = (lowercase[element.lower()] - lowercase[key[i % len(key)].lower()]) % 26
            decrypted_letter = inv_lowercase[plain_element]
            plaintext += decrypted_letter
        else:
            plaintext += element

    return plaintext


def shift_cipher_dec(ciphertext, key):
    plaintext = ''
    ciphertext_updated = ''.join(e for e in ciphertext if e.isalnum())

    for letter in ciphertext_updated:
        if letter.lower() in letterFrequency.keys():
            decrypted_int = (lowercase[letter.lower()] - key) % 26
            decrypted_letter = inv_lowercase[decrypted_int]
            plaintext += decrypted_letter
        else:
            plaintext += letter
    return plaintext


def find_recurring_words(ciphertext):
    no_punctuation_ciphertext = re.sub(r'[^\w\s]', '', ciphertext)
    cipher_array = list(no_punctuation_ciphertext.split())
    merged_ciphertext = ""

    for element in no_punctuation_ciphertext:
        if element in lowercase.keys() or uppercase.keys():
            merged_ciphertext += element

    merged_ciphertext = merged_ciphertext.replace(" ", "")
    merged_ciphertext = merged_ciphertext.replace("\n", "")
    unique_words = set(cipher_array)

    recurring_words = {}
    for word in unique_words:
        if cipher_array.count(word) > 1:
            recurring_words[word] = cipher_array.count(word)

    return merged_ciphertext, recurring_words, cipher_array


def find_recurring_word_placements(ciphertext):

    index_dictionary = {}
    merged_ciphertext, recurring_words, cipher_array = find_recurring_words(ciphertext)

    for element in cipher_array:
        if element in recurring_words.keys():
            index_dictionary[element] = [index for index, el in enumerate(cipher_array) if el == element]

    return index_dictionary, merged_ciphertext, recurring_words, cipher_array


def find_key_length_kasiski(ciphertext):

    index_dictionary, merged_ciphertext, recurring_words, cipher_array = find_recurring_word_placements(ciphertext)

    distances = []
    for element, indexes in index_dictionary.items():
        substring = ""
        for word in cipher_array[indexes[0]+1:indexes[1]+1]:
            substring += word
        distances.append(len(substring))

    gcd_list = []
    key_length = 0
    for index in range(0, len(distances)-1):
        gcd_list.append(math.gcd(distances[index], distances[index+1]))  # pair-wise greatest common divisors
        key_length = np.min(gcd_list)

##    print("Key length:", key_length)
    return key_length, index_dictionary, merged_ciphertext, recurring_words, cipher_array, gcd_list


def find_cipher_key(ciphertext, K):

    ciphertext_updated = ''.join(e for e in ciphertext if e.isalnum())
    differences = []
    sum = 0

    for key in K:
        possible_decryption = shift_cipher_dec(ciphertext_updated, key)
        for letter in list(possible_decryption):
            if letter in letterFrequency.keys():
                probability = (1/26) * (letterFrequency[letter] / len(ciphertext_updated))
                sum += probability

        differences.append(sum)
        sum = 0

    true_key = np.where(differences == np.max(differences))[0][0]
    return differences, true_key


def vigenere_attack(ciphertext, K):

    key_length, index_dictionary, merged_ciphertext, recurring_words, cipher_array, gcd_list = find_key_length_kasiski(ciphertext)
    true_key = ""

    for block_number in range(0, key_length):
        block = ""
        for i in range(0+block_number, len(merged_ciphertext), key_length):
            block += merged_ciphertext[i]

        differences, index = find_cipher_key(block, K)
        true_key += inv_lowercase[index]

    return true_key


def add_punctuation_back(ciphertext):

    true_key = vigenere_attack(ciphertext, K)
    decryption = vigenere_decryption(ciphertext, true_key)

    punctuation = Queue()
    for character in ciphertext:
        punctuation.put(character)

    dec_el = Queue()
    for character in decryption:
        dec_el.put(character)

    final_dec = ""
    while dec_el.qsize() > 0:
        punc = punctuation.get()
        if punc.lower() in letterFrequency.keys():
            dec = dec_el.get()
            final_dec += dec
        else:
            final_dec += punc
    return final_dec




def frequencyAnalyis(ciphertext):
    ciphertext_common, _ = frequencies(ciphertext)
##    print(ciphertext_common)
    twoLetter = list(filter(lambda x: len(x) == 2, ciphertext.split()))
##    print(twoLetter)
    threeLetter = list(filter(lambda x: len(x) == 3, ciphertext.split()))
##    print(threeLetter)
    return [ciphertext_common, twoLetter, threeLetter]

print(frequencyAnalyis("Eittlt ol q wtsgctr yggr ygk dqfn, qfr oz'l fgz iqkr zg ltt vin. Vozi ozl vort kqfut gy ysqcgkl qfr ztbzxktl, zitkt'l q eittlt gxz zitkt ygk tctkngft. Ykgd zit liqkh zqfu gy eitrrqk zg zit ektqdn koeiftll gy wkot, zitkt qkt egxfzstll cqkotzotl gy eittlt zg tfpgn. Eittlt ol qslg ofektrowsn ctklqzost, dqaofu oz q lzqhst ofuktrotfz of dqfn royytktfz exoloftl qkgxfr zit vgksr. Oz eqf wt dtsztr gf zgh gy hommq, ukqztr gctk hqlzq, gk xltr zg qrr q rtsoeogxl zqfu zg q lqfrvoei. Qrrozogfqssn, eittlt ol q uktqz lgxket gy hkgztof qfr eqseoxd, dqaofu oz q itqszin qfr lqzolynofu lfqea. Vitzitk tfpgntr gf ozl gvf gk ofegkhgkqztr ofzg q roli, eittlt ol q yggr ziqz wkoful htghst zgutzitk qfr qrrl q rtsoeogxl, egdygkzofu tstdtfz zg qfn dtqs."))









## Cheese is a beloved food for many, and it's not hard to see why. With its wide range of flavors and textures, there's a 
## cheese out there for everyone. From the sharp tang of cheddar to the creamy richness of brie, there are countless varieties of 
## cheese to enjoy. Cheese is also incredibly versatile, making it a staple ingredient in many different cuisines around the world.
## It can be melted on top of pizza, grated over pasta, or used to add a delicious tang to a sandwich. 
## Additionally, cheese is a great source of protein and calcium, making it a healthy and satisfying snack. 
## Whether enjoyed on its own or incorporated into a dish, cheese is a food that brings people together and adds a delicious, 
## comforting element to any meal.

##print(crackShiftCipher("Hmjjxj nx f gjqtaji ktti ktw rfsd, fsi ny'x sty mfwi yt xjj bmd. Bnym nyx bnij wfslj tk kqfatwx fsi yjcyzwjx, ymjwj'x f hmjjxj tzy ymjwj ktw jajwdtsj. Kwtr ymj xmfwu yfsl tk hmjiifw yt ymj hwjfrd wnhmsjxx tk gwnj, ymjwj fwj htzsyqjxx afwnjynjx tk hmjjxj yt jsotd. Hmjjxj nx fqxt nshwjingqd ajwxfynqj, rfpnsl ny f xyfuqj nslwjinjsy ns rfsd inkkjwjsy hznxnsjx fwtzsi ymj btwqi. Ny hfs gj rjqyji ts ytu tk uneef, lwfyji tajw ufxyf, tw zxji yt fii f ijqnhntzx yfsl yt f xfsibnhm. Fiinyntsfqqd, hmjjxj nx f lwjfy xtzwhj tk uwtyjns fsi hfqhnzr, rfpnsl ny f mjfqymd fsi xfynxkdnsl xsfhp. Bmjymjw jsotdji ts nyx tbs tw nshtwutwfyji nsyt f inxm, hmjjxj nx f ktti ymfy gwnslx ujtuqj ytljymjw fsi fiix f ijqnhntzx, htrktwynsl jqjrjsy yt fsd rjfq."))
# print(crackVigenereCipher("DAZFI SFSPA VQLSN PXYSZ WXALC DAFGQ UISMT PHZGA MKTTF TCCFX KFCRG GLPFE TZMMM ZOZDE ADWVZ WMWKV GQSOH QSVHP WFKLS LEASE PWHMJ EGKPU RVSXJ XVBWV POSDE TEQTX OBZIK WCXLW NUOVJ MJCLL OEOFA ZENVM JILOW ZEKAZ EJAQD ILSWW ESGUG KTZGQ ZVRMN WTQSE OTKTK PBSTA MQVER MJEGL JQRTL GFJYG SPTZP GTACM OECBX SESCI YGUFP KVILL TWDKS ZODFW FWEAA PQTFS TQIRG MPMEL RYELH QSVWB AWMOS DELHM UZGPG YEKZU KWTAM ZJMLS EVJQT GLAWV OVVXH KWQIL IEUYS ZWXAH HUSZO GMUZQ CIMVZ UVWIF JJHPW VXFSE TZEDF".lower()))

##print(crackVigenereCipher("Jlppg xjpw mk gqvp"))



"""
#IMPLEMENTATIONS
"""







##print(rot13Cipher("I like cheese"))
##print(decryptRot13("V yvxr purrfr"))
##print(atbashCipher("Hello my name is Bob"))
##print(decryptAtbash("svool nb mznv rh erszzm"))
##print(monoCipher("HELLOMYNAMEISVIHAAN", "QWERTYUIOPASDFGHJKLZXCVBNM"))
##print(decryptMono("ITSSGDNFQDTOLCOIQQF", "QWERTYUIOPASDFGHJKLZXCVBNM"))
##print(trithCipher("Hello my name is bob", True))
##print(trithCipher("Hfnosreuivoteocq", True)) #NOT DONE
##print(vigCipher("MICHIGAN TECHNOLOGICAL UNIVERSITY", "HOUGHTON"))
##print(vigCipher("HELLO MEET ME AT BOBS HOUSE", "SECRETMESSAGE"))
##print(vigCipher("DCODE", "KEY"))
##print(decryptVigenere("ZINCS FQIL EE GX TSDJ LHGWW", "SECRETMESSAGE"))
##print(decryptVigenere("NGMNI", "KEY"))
##print(decryptVigenere("TWWNPZOA ASWNUHZBNWWGS NBVCSLYPMM", "HOUGHTON"))
##print(hillCipher("ACT", "GYBNQKURP"))
##print(hillCipher("ACT", "BESTHILLR"))
##print(hillCipher("PAY", "RRFVSVCCT"))
##print(hillCipher("ACTPAY", "BESTHILLR"))
##print(hillCipher("EX", "HILL"))
##print(hillCipher("EXAM", "HILL"))
##print(decryptHill("POH", "GYBNQKURP"))
##print(decryptHill("EL", "HILL"))
##print(decryptHill("SC", "HILL"))
##print(decryptHill("ELSC", "HILL"))
##print(decryptHill("MKH", "BESTHILLR"))
##print(decryptHill("LNS", "RRFVSVCCT"))
##print(decryptHill("MKHFJB", "BESTHILLR"))
##print(playfairCipher("birmingham", "diamond"))
##print(playfairCipher("why dont you", "keyword"))
##print(playfairCipher("come to the window", "keyword"))
##print(playfairCipher("the big wheel", "keyword"))
##print(playfairCipher("communicate", "computer"))
##print(playfairCipher("jazz", "genere"))
##print(playfairCipher("instruments", "monarchy"))
##print(decryptPlayfair("gatlmzclrqtx", "monarchy"))
##print(decryptPlayfair("ogvyvy", "genere"))
##print(decryptPlayfair("omrmpcsgpter", "computer"))
##print(decryptPlayfair("hbtidbhkmo", "diamond"))
##print(decryptPlayfair("rbia bdigt psz", "diskjockey"))
##print(decryptPlayfair("pwkoc vapfsqys pcdliea", "attackwhen"))
##print(playfairCipher("the shipment is arriving at the docks tomorrow evening be ready", "cheese"))
##print(decryptPlayfair("nic eipmsntf tp eqyqpxsa db ani ncldc mnqhuqyu qvnscth ad enlangzv", "shipment"))  
##
##print(transposCipher("message", "code"))
##print(transposCipher("transpositioncipher", "transpo"))
##print(decryptTransposition("mases_eg", "code"))
##print(decryptTransposition("athnieoc_pn_ripsortsi", "transpo"))
##print(affineCipher("meet me at the docks tomorrow be ready for the shipment", 17, 20))
##print(decryptAffine("qkkf qk uf fjk tycio fyqyxxye lk xkutm byx fjk ojapqkhf", 17, 20))
##print(varcamtCipher("MEETTOMORROWATTHEDOCKS", "MEET", "QWERTYUIOPASDFGHJKLZXCVBNM", 18, 17, 20))
##print(decryptVarcamt("LUVJVOTJATTSSCDPDTBDKL", "MEET", "QWERTYUIOPASDFGHJKLZXCVBNM", 18, 17, 20))
##print(varcamtCipher("SHIPMENTISCOMINGSTJOHNSAVENUENIGHT", "SHIP", "ZXCVBNMASDFGHJKLQWERTYUIOP", 7, 17, 20)) 
##print(decryptVarcamt("WYTOPENWVDGXXSVWMEUFOQJCCYHTAYVMAU", "SHIP", "ZXCVBNMASDFGHJKLQWERTYUIOP", 7, 17, 20))



##print(Venigma("shipment", "dock"))
##print(Venigma("tomorrows", "shipments"))
##print(decryptVenigma("RLKRAJHY", "dock"))
##main()






#Learn about caeser cipher and learn about all of the other ciphers option
#Copy to clipboard option
