import os
from flask import Flask
from flask_cors import CORS

import config
from server.blueprints.chat import chat
from server.blueprints.converse import converse
from server.blueprints.personas import personas


app = Flask(__name__)
CORS(app)

app.register_blueprint(chat, url_prefix='/api/chat')
app.register_blueprint(converse, url_prefix='/api/converse')
app.register_blueprint(personas, url_prefix='/api/personas')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 9999)))
