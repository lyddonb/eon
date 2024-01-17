from flask import Flask

import config
from server.blueprints.chat import chat


app = Flask(__name__)

app.register_blueprint(chat, url_prefix='/chat')

if __name__ == '__main__':
    app.run(debug=True)
