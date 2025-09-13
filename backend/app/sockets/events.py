import gc
from ..services.llm import evaluate_models


def register_events(socketio):
    @socketio.on('connect')
    def handle_connect():
        print('Client connected')

    @socketio.on('disconnect')
    def handle_disconnect():
        print('Client disconnected')

    @socketio.on('message')
    def handle_message(message):
        print('Received message: ' + message)
        socketio.send('Echo: ' + message)
        stored_response = evaluate_models(message)
        print(stored_response)
        socketio.emit('response', stored_response)
        gc.collect()

