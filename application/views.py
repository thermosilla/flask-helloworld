from application import app
from flask import json
import socket

@app.route("/")
def index():
    data = {
            'Response':'Hola!!',
            'Hostname': socket.gethostname()
            }
    respuesta = app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
            )
    return respuesta
