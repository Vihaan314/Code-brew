from .models import User

def getNumUsers():
    return len(User.query.all()) + 1
