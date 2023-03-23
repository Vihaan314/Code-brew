from .models import User
import random
from . import encryptDecrypt

def getNumUsers():
    return len(User.query.all()) + 1

def randomAlphabet():
    shiftLearnCaeser = random.randint(1, 26)
    shiftAlphabetLearnCaeser = encryptDecrypt.caeserCipher("ABCDEFGHIJKLMNOPQRSTUVWXYZ", shiftLearnCaeser)
    return shiftLearnCaeser, shiftAlphabetLearnCaeser

def randomSentence():
    randomSentences = ["Hello this is secret", "This is another secret message"]
    randomSentence = random.choice(randomSentences)
    return randomSentence

def randomWord():
    randomWords = ["Cheese", "Beans", "Yellow", "Blue", "Piano"]
    randomWord = random.choice(randomWords)
    return randomWord

def getShiftInWords(shift):
    words = "one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty twenty-one twenty-two twenty-three twenty-four twenty-five twenty-six".split()
    return words[shift-1]