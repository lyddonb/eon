from flask import Flask

import config
from server.blueprints.chat import chat
from server.blueprints.converse import converse


app = Flask(__name__)

app.register_blueprint(chat, url_prefix='/chat')
app.register_blueprint(converse, url_prefix='/converse')

if __name__ == '__main__':
    app.run(port=3000, debug=True)
