from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_community.chat_models import ChatOpenAI

from server.ai.qa_reasoner.personas import get_selected_personas
from server.ai.qa_reasoner.prompts.brainstorm import get_prompt as get_brainstorm_prompt


def _get_chain():
    # Invoke conversation chain
    chat = ChatOpenAI(temperature=0.5, model='gpt-4-1106-preview')

    return ConversationChain(
        llm=chat,
        memory=ConversationBufferMemory()
    )

def converse(question: str):
    chain = _get_chain()
    personas = get_selected_personas(question)

    brainstorm_prompt = get_brainstorm_prompt(question, personas)
    brainstorm = chain.run(brainstorm_prompt)

    print(brainstorm)

    return {
        "result": brainstorm
    }
