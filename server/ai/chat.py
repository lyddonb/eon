from langchain import hub
from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_openai import ChatOpenAI

# Taken from: https://python.langchain.com/docs/modules/agents/how_to/streaming
# Add the AgentAction/observation/AgentFinish stuff later

# Prompt:
# input_variables=['agent_scratchpad', 'input']
# input_types={
#     'chat_history': typing.List[typing.Union[langchain_core.messages.ai.AIMessage, langchain_core.messages.human.HumanMessage, langchain_core.messages.chat.ChatMessage, langchain_core.messages.system.SystemMessage, langchain_core.messages.function.FunctionMessage, langchain_core.messages.tool.ToolMessage]], 
#     'agent_scratchpad': typing.List[typing.Union[langchain_core.messages.ai.AIMessage, langchain_core.messages.human.HumanMessage, langchain_core.messages.chat.ChatMessage, langchain_core.messages.system.SystemMessage, langchain_core.messages.function.FunctionMessage, langchain_core.messages.tool.ToolMessage]]
# } 
# messages=[SystemMessagePromptTemplate(prompt=PromptTemplate(input_variables=[], template='You are a helpful assistant')), MessagesPlaceholder(variable_name='chat_history', optional=True), HumanMessagePromptTemplate(prompt=PromptTemplate(input_variables=['input'], template='{input}')), MessagesPlaceholder(variable_name='agent_scratchpad')]


def chat_completion(initial_message: str):
    prompt = hub.pull("hwchase17/openai-functions-agent")

    # print("Prompt: ", prompt)

    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

    search = TavilySearchResults()
    tools = [search]

    agent = create_openai_functions_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools)

    input = {
        "input": initial_message
    }

    for chunk in agent_executor.stream(input):
        # Agent Action
        if "actions" in chunk:
            for action in chunk["actions"]:
                print(
                    f"Calling Tool ```{action.tool}``` with input ```{action.tool_input}```"
                )

        # Observation
        elif "steps" in chunk:
            for step in chunk["steps"]:
                print(f"Got result: ```{step.observation}```")

        # Final result
        elif "output" in chunk:
            yield chunk["output"]

        else:
            raise ValueError

        print("------")