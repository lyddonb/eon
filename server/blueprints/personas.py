from flask import Blueprint, jsonify, request

from server.ai.qa_reasoner.personas import get_selected_personas


personas = Blueprint('personas', __name__)

@personas.route('/', methods=['POST'])
def index():
    question = request.get_json().get('question')
    question_personas = get_selected_personas(question)

    return jsonify(question_personas)
