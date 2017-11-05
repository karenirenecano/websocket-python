from gevent import monkey
monkey.patch_all()

import cgi
from flask import Flask, render_template, request
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

# prepare your endpoints
@app.route('/')
def main():
    return render_template('main.html')

# when a message is emitted from the client on 'go-message', it goes here
@socketio.on('go-message', namespace='/dd')
def ws_announce(data):
    print(data)
    socketio.emit('go-message',{'content': data}, namespace="/dd")
    
# serve your page up on localhost:5000
if __name__ == '__main__':
    socketio.run(app, "0.0.0.0", port=5000)
