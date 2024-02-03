from flask import Blueprint, Response, request

from server.ai.qa_reasoner.conversation import converse as qa_converse

converse = Blueprint('converse', __name__)

# TODO: Make this a POST
@converse.route('/', methods=['GET'])
def index():
    # Get flask query arg
    question = request.args.get('question')
    print('Asking question:', question)

    return Response(qa_converse(question), mimetype='text/event-stream')
