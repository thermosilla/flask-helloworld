from flask import Flask

app = Flask(__name__)

import application.views

app.run(host="0.0.0.0",port=8888)
