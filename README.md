# Python Websocket Chat

This is a simple websocket demo code adapted from [Matt Makai's](https://github.com/mattmakai) tutorial about [Flask/Gevent Websocket](https://github.com/mattmakai/python-websockets-example). Chatterbot has been integrated on this project.
MongoDB is used to contain the Chatbot intents

### Installation

We will need a data storage for our Chat bot intents and replies. We will be using MongoDB. Make sure you have docker installed on your machine.

```
docker pull mongo
```
This will pull the latest image of mongo, and you now have a full blown mongo server :) Now let's set it up.

```
docker run -d -p 27017:27017 --name some-mongo -e MONGO_INITDB_ROOT_USERNAME=mongoadmin -e MONGO_INITDB_ROOT_PASSWORD=secret mongo
```
This runs a container from the mongo image. Runs on -d (daemon or on background), exposes -p (port) 27017 of the container to your local machine. Naming --name the container to 'some-mongo' with environment variables -e, MONGO_INITDB_ROOT_USERNAME and MONGO_INITDB_ROOT_PASSWORD, and finally referring to the mongo image.

Seed some initial values having this key pair format
```
"intent" : "Watcha doin?",
"reply" : "Exploring Python and Chatbot and MongoDB"
```

Make sure you have Python installed. I recommend using Anaconda and then install virtualenv.

Create a virtualenv
On Windows
```sh
$ virtualenv flask_env
$ projectDirectory/flask_env/Scripts/activate
$ pip install -r requirements
$ source flask_env/Scripts/activate
#you should see the current virtualenv you are un
$ (flask_env)
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
| ChatterBot | https://github.com/gunthercox/ChatterBot |
| MongoDB Docker Image | https://hub.docker.com/_/mongo/

### Deployment

I have included the [apache-pychat.conf](https://github.com/karenirenecano/websocket-python/blob/master/apache-pychat.conf) to proxy pass the requests coming from localhost:5000(your python script) to be redirected to localhost. A shell script : [gunicornstart.sh](https://github.com/karenirenecano/websocket-python/blob/master/gunicornstart.sh) has also been added to run gunicorn at the background and restart using [supervisorctl](https://github.com/karenirenecano/websocket-python/blob/gunicornDeployment/supervisor.conf) should the app stop.

Happy Coding! :)
