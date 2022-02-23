import os
import sys

from flask import request

from flask_app import app
from fontend_app import fontend_app, ws_app

# sys.dont_write_bytecode = True

# from helper import start_debugger
app.register_blueprint(fontend_app)
app.register_blueprint(ws_app)
from flask_socketio import SocketIO, send

socketio = SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")

@socketio.on('connect')
def test_connect():
    print("..................test_connect.............")
    print("CONNECTED!", request.sid, "\n")

@socketio.on('disconnect')
def test_disconnect():
    print("..................test_disconnect.............")
    print('DISCONNECTED!', request.sid, "\n")

@socketio.on('message')
def received(msg):
    # print("..................received.............")
    print(".....server received msg: ", msg, "\n")
    send(msg, broadcast=True, include_self=False)

if __name__ == "__main__":
    # locally PORT 5000, Heroku will assign its own port
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_DEBUG', False)
    if os.environ.get('VSCODE_DEBUG'):
        # start_debugger()
        app.run(host='0.0.0.0', port=port, debug=False, use_evalex=False)
    else:
        app.run(host='0.0.0.0', port=port, debug=debug, use_evalex=False)
