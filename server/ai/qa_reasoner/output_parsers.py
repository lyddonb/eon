from langchain.output_parsers import ResponseSchema, StructuredOutputParser


# Defines the response schema we want to receive
PERSONAS_RESPONSE_SCHEMAS = [
    ResponseSchema(name="persona1", description="the most relevant persona selected to use to reason through the question"),
    ResponseSchema(name="persona2", description="the second persona selected to use to reason through the question"),
    ResponseSchema(name="persona3", description="the third persona selected to use to reason through the question"),
    ResponseSchema(name="rationale", description="for each persona, carefully explain the most compelling reason for including them")
]

def get_personas_output_parser():
    return StructuredOutputParser.from_response_schemas(PERSONAS_RESPONSE_SCHEMAS)

CREATE_PERSONA_RESPONSE_SCHEMAS = [
    ResponseSchema(name="title", description="the title of the persona"),
    ResponseSchema(name="description", description="the description of the persona"),
]

def get_create_persona_output_parser():
    return StructuredOutputParser.from_response_schemas(CREATE_PERSONA_RESPONSE_SCHEMAS)
