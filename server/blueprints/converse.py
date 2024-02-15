from flask import Blueprint, Response, request

from server.ai.qa_reasoner.conversation import converse as qa_converse
from server.blueprints.streaming import wrap_streaming_response

converse = Blueprint('converse', __name__)

@converse.route('/', methods=['POST'])
def index():
    # Get flask query arg
    question = request.get_json().get('question')
    print('Asking question:', question)

    return wrap_streaming_response(qa_converse(question))
