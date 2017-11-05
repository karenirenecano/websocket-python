# Python Websocket Chat

This is a simple websocket demo code adapted from [Matt Makai's](https://github.com/mattmakai) tutorial about [Flask/Gevent Websocket](https://github.com/mattmakai/python-websockets-example).


### Installation

Make sure you have Python installed.

Create a virtualenv
On Windows
```sh
$ virtualenv flask_env
$ projectDirectory/flask_env/Scripts/activate
$ pip install -r requirements
$ python app.py
```
Your page should be up and running at [localhost:5000](http://localhost:5000)

### Plugins

I have added a css/js plugin to see the feel of "real" time notification and removed Redis from requirements.txt as I did not need Redis for this.

| Plugin | Source |
| ------ | ------ |
| NotifyJS | https://notifyjs.com/|
| SocketIO | cdnjs.cloudflare.com/ajax/libs/socket.io/1.4.5/socket.io.min.js |
| JQuery | jquery-1.12.0.min.js |


