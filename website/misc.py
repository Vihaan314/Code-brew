from .models import User
import random

def getNumUsers():
    return len(User.query.all()) + 1

def randomSentence():
    randomSentences = ["Hello this is secret", "So sad eklavya", "Uh say muns this is cap"]
    randomSentence = random.choice(randomSentences)
    return randomSentence
