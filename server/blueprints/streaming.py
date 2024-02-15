from flask import Response


def _wrap_chunk(chunk: str):
    return f"data: {chunk}\n\n"

def _done():
    return "data: [DONE]"

def _wrap_iterator(response):
    for chunk in response:
        if chunk:
            if (chunk == "[DONE]"):
                yield _done()
            else:
                yield _wrap_chunk(chunk)

    # yield _done()

def wrap_streaming_response(response):
    return Response(_wrap_iterator(response), mimetype='text/event-stream')