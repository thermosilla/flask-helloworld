from flask import Flask

app = Flask(__name__)

import application.views

if __name__ == '__main__':
    app.run()
