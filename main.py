from flask import Flask
import logging


logging.getLogger().setLevel(logging.DEBUG)
app = Flask(__name__)
app.config.update(DEBUG=True)


@app.route('/')
def hello_world():
    return 'Hello, World!'