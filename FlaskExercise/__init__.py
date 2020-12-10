import logging
from flask import Flask

app = Flask(__name__)
wsgi_app = app.wsgi_app
app.logger.setLevel(logging.WARNING)
streamHandler = logging.StreamHandler()
streamHandler.setLevel(logging.WARNING)
app.logger.addHandler(streamHandler)
# TODO: Set the app's logger level to "warning"
#   and any other necessary changes

import FlaskExercise.views