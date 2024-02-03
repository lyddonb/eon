from langchain import PromptTemplate


def get_prompt(question: str, personas: str):
    template = PromptTemplate(
        input_variables=["selected_personas", "question"],
        template="""
        You are a QuestionImprover reasoning agent using three unique, specified personas to reason collectively step by step to ultimately provide 
        the best possible quality improvement to a given question by arriving at a synthesized improved version of the question.

        To begin with, allow each persona to share their initial insights about the following question. 
        Detail your perspective, drawing on specific knowledge, experiences, and pioneering concepts from your field.
        Aim to uncover new angles and dimensions of the question, demonstrating how your unique expertise contributes 
        to a multifaceted understanding. In subsequent prompts, we'll engage in a collaborative process where these 
        perspectives are woven into an intricate network of thoughts. Later in the conversation, we'll highlight how 
        each viewpoint complements or challenges the others, constructing a more multidimensional and higher quality question 
        to pose back to the user who asked the initial question.

        The personas are: {selected_personas}

        The question is: {question}
        
        Please output each persona's individual initial response to the question on a new line.
        """,
    )

    return template.format(selected_personas=personas, question=question)