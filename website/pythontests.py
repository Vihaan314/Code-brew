#VARCHAMPT CIPHER ENCRYPTION
def varcamtCipher(message, key, alphabet, shift, a, b):
    #Vigenere Cipher
    #Atbash Cipher
    #Rot13 Cipher
    #Caeser Cipher
    #Affine cipher
    #Monoalphabetic cipher
    #Trithemius cipher
    vig = vigCipher(message, key)
    atbash = atbashCipher(vig)
    rot13 = rot13Cipher(atbash)
    caeser = caeserCipher(rot13, shift)
    affine = affineCipher(caeser, a, b)
    mono = monoCipher(affine, alphabet)
    trith = trithCipher(mono, True)
    return trith

def decryptVarcamt(message, key, alphabet, shift, a, b):
    mono = decryptTrithemius(message, True)
    affine = decryptMono(mono, alphabet)
    caeser = decryptAffine(affine, a, b)
    rot13 = decryptCaeser(caeser, shift)
    atbash = decryptRot13(rot13)
    vig = decryptAtbash(atbash)
    decrypted = decryptVigenere(vig, key)
    return decrypted







"""
#CREATE CUSTOM CIPHER
#Possible names:
#Vihcrypt
#Vihenigma
#Vinigma
"""
def Venigma(message, key):
    #Key must be length of a square number
    #String must the length of a multiple of the key

    #Convert the key 
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    def convertStringNumer(string):
        return [alphabet.index(i) for i in string]
    def convertNumArString(arr):
        return "".join([alphabet[i] for i in arr])
##    print(convertNumArString([17, 0]))
    messSpaces = message
    message = message.replace(" ", "").upper()
    key = key.upper()
    keyAlpha = np.array([alphabet.index(i)+1 for i in key]).reshape(int(math.sqrt(len(key))), int(math.sqrt(len(key))))
    messSplit = [message[i:i+int(math.sqrt(len(key)))] for i in range(0, len(message), int(math.sqrt(len(key))))]    
##    print(keyAlpha)
##    print(messSplit)
    keyIter = [(key[0:len(messSplit)] * int(math.sqrt(len(key))))[i:i+int(math.sqrt(len(key)))] for i in range(0, len((key[0:len(messSplit)] * int(math.sqrt(len(key))))), int(math.sqrt(len(key))))] 
    print(keyIter)
    for i in range(0, len(messSplit)):      
        messSplit[i] = vigCipher(messSplit[i], keyIter[i])
    mLen = len(messSplit)
##    print(messSplit)
    for i in range(0, len(messSplit)):
        messSplit[i] = convertStringNumer(messSplit[i])
##    print(messSplit)
    messSplit = np.array(messSplit)
    keyNumAr = ((messSplit @ keyAlpha))
    print(keyNumAr)
    encrypted = "".join([convertNumArString(keyNumAr[i].tolist()) for i in range(0, len(keyNumAr))])
    return encrypted
    
def decryptVenigma(message, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    def convertStringNumer(string):
        return [alphabet.index(i) for i in string]
    def convertNumArString(arr):
        return "".join([alphabet[i] for i in arr])
    key = key.upper()
    keyAlpha = np.array([alphabet.index(i)+1 for i in key]).reshape(int(math.sqrt(len(key))), int(math.sqrt(len(key))))
    messSplit = [message[i:i+int(math.sqrt(len(key)))] for i in range(0, len(message), int(math.sqrt(len(key))))]    
    keyIter = [(key[0:len(messSplit)] * int(math.sqrt(len(key))))[i:i+int(math.sqrt(len(key)))] for i in range(0, len((key[0:len(messSplit)] * int(math.sqrt(len(key))))), int(math.sqrt(len(key))))] 
    messNums = []
    for i in range(0, len(messSplit)):
        messNums.append(convertStringNumer(messSplit[i]))
    messNums = Matrix((np.array(messNums)).reshape(len(messSplit), int(len(messSplit)/2)))
    print(messNums)
    invMess = messNums.inv_mod(26)
    print(invMess)
    
def frequencyAnalysis(message):
    message = message.upper()
    mostUsedLetters = list("etaoinshrdlcumwfgypbvkjxqz".upper())
    mostUsedFreqs = [12.7, 9.1, 8.2, 7.5, 7.0, 6.7, 6.3, 6.1, 6.0, 4.3, 4.0, 2.8, 2.8, 2.4, 2.4, 2.2, 2.0, 2.0, 1.9, 1.5, 1.0, 0.8, 0.15, 0.15, 0.10, 0.07]
    mostUsed = dict(zip(mostUsedLetters, mostUsedFreqs))

    messageLetters = list(set("".join([i for i in message if i.isalpha()])))
    messageFreqs = [round(message.count(i)/len(message)*100, 1) for i in messageLetters]
    messageFreqs = dict(zip(messageLetters, messageFreqs))
    messageP = sorted(list(messageFreqs.values()), reverse = True)
    
    print(mostUsed)
    print("")
    print(messageFreqs)
    print("\n")
    
    commonWords = stopwords.words("english")
    attempts = []
    originalMessage = message

    print("Common most used", mostUsedFreqs)
    print("")
    print("Message most used", messageP)
    print("")

    messageMostCommon = sorted(messageFreqs, key=messageFreqs.get, reverse=True)
    commonLetters = list(filter(lambda x: x in "".join(messageMostCommon), "".join(mostUsedLetters)))
    messageList = list(message)

    verification = [0]*26
    for i in range(0, len(messageList)):
        if messageList[i] in messageMostCommon:
            messageList[i] = commonLetters[messageMostCommon.index(messageList[i])]
            
    attempts.append("".join(messageList))
    for i in attempts[0]:
        if i in commonWords:
            verification[0] += 1

    for i in range(0, len(messageP)):
        if messageP[i] == messageP[-1]:
            break
        elif messageP[i] == messageP[i+1]:
            pass
    print(commonLetters)
    print(messageMostCommon)
    print("\n")
    print(attempts[0])
    print(verification)
