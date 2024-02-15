from enum import Enum
import json

from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_openai import ChatOpenAI

from server.ai.qa_reasoner.personas import get_selected_personas, personas_to_string
from server.ai.qa_reasoner.prompts.brainstorm import get_prompt as get_brainstorm_prompt


class ResultType(Enum):
    CHAT = "chat"
    PERSONAS = "personas"


class ResultMimeType(Enum):
    JSON = "application/json"
    TEXT = "text/plain"
    HTML = "text/html"


def _get_chain():
    # Invoke conversation chain
    chat = ChatOpenAI(temperature=0.5, model='gpt-4-1106-preview')

    return ConversationChain(
        llm=chat,
        memory=ConversationBufferMemory()
    )

def _wrap_result(result_type: ResultType, result: any, format: ResultMimeType = ResultMimeType.JSON):
    return json.dumps({
        "type": result_type.value,
        "format": format.value,
        "result": result
    })

def converse(question: str):
    yield _wrap_result(
        ResultType.CHAT,
        'Finding the best personas to answer the question: ' + question,
        ResultMimeType.TEXT
    )
    chain = _get_chain()

    personas = get_selected_personas(question)
    yield _wrap_result(ResultType.PERSONAS, personas)

    personas_string = personas_to_string(personas)
    brainstorm_prompt = get_brainstorm_prompt(question, personas_string)
    print('Brainstorm')
    response = chain.stream(brainstorm_prompt)
    for chunk in response:
        if chunk:
            print('has chunk')
            yield _wrap_result(
                ResultType.CHAT,
                chunk.get("response"),
                ResultMimeType.TEXT
            )
