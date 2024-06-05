from flask import Flask
from flask_socketio import SocketIO
import modelsdb

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

modelsdb.register_events(socketio)

if __name__ == '__main__':
    socketio.run(app, debug=True)