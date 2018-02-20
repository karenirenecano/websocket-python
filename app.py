from chatterbot import ChatBot
import json
from gevent import monkey
monkey.patch_all()

import cgi
from flask import Flask, render_template, request
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)


chatbot = ChatBot(
    'Default Response Example Bot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch'
        },
        {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            'threshold': 0.65,
            'default_response': 'I am sorry, but I do not understand.'
        }
    ],
    trainer='chatterbot.trainers.ListTrainer'
)

# Train the chat bot with a few responses
chatbot.train([
    'How can I help you?',
    'I want to create a chat bot',
    'Have you read the documentation?',
    'No, I have not',
    'This should help get you started: http://chatterbot.rtfd.org/en/latest/quickstart.html',
    'Who created you?',
    'Mainly fron gunthercox but I am from Commude Philippines Inc! :)',
    'Sino gwapo?',
    'Sino pa? edi si Rui! ;)',
    'Sino mga gwapo?',
    'Required lahat gwapo at maganda sa Commude! :)',
    'Mahal ba niya ako?',
    'Importante pa ba yon? ;)'
])




'''chatbot = ChatBot('Charlie',trainer='chatterbot.trainers.ListTrainer')
chatbot.train([
        "Hi, can I help you?",
        "Sure, I'd like to book a flight to Iceland.",
        "Your flight has been booked."
    ])'''
#response = chatbot.get_response('I would like to book a flight.')

# prepare your endpoints
@app.route('/')
def main():
    return render_template('main.html')

# when a message is emitted from the client on 'go-message', it goes here
@socketio.on('go-message', namespace='/dd')
def ws_announce(data):
    print(data)
    response = chatbot.get_response(data["message"])
    data["chat-response"] = str(response)
    socketio.emit('go-message',{'content': data}, namespace="/dd")
    
# serve your page up on localhost:5000
if __name__ == '__main__':
    socketio.run(app, "0.0.0.0",port=4900)
#    app.run(host="127.0.0.1",port=5000,debug=True)
