from flask import Blueprint, Response, request

from server.ai.chat import chat_completion

chat = Blueprint('chat', __name__)

# TODO: Make this a POST
@chat.route('/', methods=['GET'])
def completion():
    # Get flask query arg
    query = request.args.get('query')

    return Response(chat_completion(query), mimetype='text/event-stream')
