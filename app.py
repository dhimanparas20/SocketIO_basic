from flask import Flask, render_template, request
from flask_socketio import SocketIO, send, emit
from os import system

system("clear")

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app, cors_allowed_origins="*")  # Allow CORS for testing

# REST endpoint example
@app.route('/')
def index():
    return render_template('index.html')  # Render the index.html template

# Generic WebSocket event handler to capture any event and print its name and data
@socketio.on('message')
def handle_any_event(data):
    event_name = request.event['message']
    print(f'Event: {event_name}, Data: {data}')
    emit('message', f'Echo from {event_name}: {data}', broadcast=True)

# WebSocket event handler for a new connection
@socketio.on('connect')
def handle_connect():
    print('Client connected')
    emit('message', 'Welcome to the WebSocket server!', broadcast=True)

# WebSocket event handler for disconnection
@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
