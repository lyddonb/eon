import {
  EventSourceMessage,
  EventStreamContentType,
  fetchEventSource,
} from "@microsoft/fetch-event-source"

export class RetriableError extends Error {}
export class FatalError extends Error {}

export enum ResultType {
  CHAT = "chat",
  PERSONAS = "personas",
}

export enum ResultMimeType {
  JSON = "application/json",
  TEXT = "text/plain",
  HTML = "text/html",
}

export interface Result {
  type: ResultType
  format: ResultMimeType
  result: unknown

  fromJson(json: string): Result
}

const makeResult: Result = {
  type: ResultType.CHAT,
  format: ResultMimeType.JSON,
  result: null,

  fromJson(json: string): Result {
    const parsedJson = JSON.parse(json)
    return {
      type: parsedJson.type,
      format: parsedJson.format,
      result: parsedJson.result,
    } as Result
  },
}

export const postEvent = (
  url: string,
  body: unknown | null,
  onResult?: (result: Result) => void,
  onClose?: () => void,
) => {
  return fetchEventSource(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: body ? JSON.stringify(body) : null,
    async onopen(response) {
      if (
        response.ok &&
        response.headers.get("content-type")?.startsWith(EventStreamContentType)
      ) {
        return // everything's good
      } else if (
        response.status >= 400 &&
        response.status < 500 &&
        response.status !== 429
      ) {
        // client-side errors are usually non-retriable:
        console.log("Client error", response)
        throw new FatalError()
      } else {
        console.log("Server error", response)
        throw new RetriableError()
      }
    },
    onmessage(msg: EventSourceMessage) {
      // if the server emits an error message, throw an exception
      // so it gets handled by the onerror callback below:
      if (msg.event === "FatalError") {
        console.log("FatalError", msg.data)
        throw new FatalError(msg.data)
      } else if (onResult) {
        onResult(makeResult.fromJson(msg.data))
      }
    },
    onclose() {
      if (onClose) {
        onClose()
      }
    },
    onerror(err) {
      console.log("onerror", err)
      if (err instanceof FatalError) {
        throw err // rethrow to stop the operation
      } else {
        // do nothing to automatically retry. You can also
        // return a specific retry interval here.
      }
    },
  })
}
