from flask_socketio import SocketIO, send, emit
from flask_login import current_user
from flask import request, session  
from website import create_app
# from website import db
from website import saveMessage, deleteMessage
from website import encryptDecrypt
# from website import getUsers

app = create_app()
socketio = SocketIO(app)

@socketio.on("message")
def handleMessage(msg):
    print(f"MSG: {msg}, TYPE: {type(msg)}")
    # emit("new_private_message", msg, room = request.sid)
    # send(f"{msg.date} - {trySessions[msg.user_id-1]}\n{msg.data}", broadcast=True) #Broadcast = True makes it available to all users, if it was false it would send it to the person who sent the message to you
    saveMessage(msg) 
    send(msg, broadcast = True)

@socketio.on("p_message")
def privateMessage(msg, receiver):
    print(f"MSG: {msg}, TYPE: {type(msg)}")

    saveMessage(msg, receiver = receiver)



# @socketio.on("delete")
# def delete(user):
#     deleteMessage(user)

if __name__ == '__main__':
    socketio.run(app, debug=True) #host="0.0.0.0", port = 80




#how do I write code that returns the checks if the largest element is the same as the the second largest element in a list?










## TODO: When creating the interface for the user (when you click on a user) it should say "I speak" + fav_language 