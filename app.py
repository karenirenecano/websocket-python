from chatterbot import ChatBot
from pymongo import MongoClient # Database connector
import json
from flask import jsonify
from gevent import monkey
import cgi
from flask import Flask, render_template, request
from flask_socketio import SocketIO
monkey.patch_all()

app = Flask(__name__)
socketio = SocketIO(app)

client = MongoClient('mongodb://mongoadmin:secret@192.168.99.100', 27017)    #Configure the connection to the database
db = client.chat_db    #Select the database

def getAll():
    journal = db.journal
    output = []
    for j in journal.find():
        output.append(j['intent'])
        output.append(j['reply'])
    return output

output = getAll()
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
# Train the chat bot from the mongoDB
chatbot.train(output)

# prepare your endpoints
@app.route('/')
def main():
    return render_template('main.html')

#list all trained journal conversation
@app.route('/journal/all')
def getAllTrainedJournal():
    journal = db.journal
    output = []
    for j in journal.find():
        output.append({'intent' : j['intent'], 'reply' : j['reply'] })
    return jsonify({'journal' : output})

# when a message is emitted from the client on 'go-message', it goes here
@socketio.on('go-message', namespace='/dd')
def ws_announce(data):
    # print(data)
    response = chatbot.get_response(data["message"])
    data["chat-response"] = str(response)
    socketio.emit('go-message',{'content': data}, namespace="/dd")
    
# serve your page up on localhost:5000
if __name__ == '__main__':
    socketio.run(app, "0.0.0.0",port=4900) #enable this if you want to test out the chat
#    app.run(host="0.0.0.0",port=5000,debug=True)
