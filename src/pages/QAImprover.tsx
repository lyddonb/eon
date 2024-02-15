import PersonasList from "@/components/PersonasList"
import { Persona } from "@/core/personas"
import { Result, ResultType, postEvent } from "@/http"
import React from "react"

const getComponent = (result: Result): React.ReactNode => {
  switch (result.type) {
    case ResultType.CHAT:
      return <div>{result.result as string}</div>
    case ResultType.PERSONAS:
      return <PersonasList personas={result.result as Persona[]} />
    default:
      null
  }
}

const QAImpover = () => {
  const [question, setQuestion] = React.useState<string>("")
  const [results, setResults] = React.useState<Result[]>([])
  const [loading, setLoading] = React.useState<boolean>(false)

  const onQuestionChange = (
    event: React.ChangeEvent<HTMLInputElement>,
  ): void => {
    setQuestion(event.target.value)
  }

  // https://react.dev/reference/react/useCallback#updating-state-from-a-memoized-callback
  const onResult = React.useCallback((value: Result) => {
    setResults((results) => [...results, value])
  }, [])

  const onClose = () => {
    console.log("Close")
    setLoading(false)
  }

  const onAskQuestion = (event: React.MouseEvent<HTMLButtonElement>): void => {
    event.preventDefault()

    if (question) {
      setLoading(true)
      const url = "/api/converse"
      const payload = { question }
      postEvent(url, payload, onResult, onClose)
    }
  }

  const components = React.useMemo(
    () =>
      results.map((result, index) => (
        <div key={index}>{getComponent(result)}</div>
      )),
    [results],
  )

  return (
    <div>
      <h1>QA Improver</h1>
      <div>
        <p>Ask a question and get an answer</p>
        <input type="text" onChange={onQuestionChange} />
        <button onClick={onAskQuestion}>Ask</button>
      </div>
      <div>{components}</div>
      <div>{loading && <div>Loading...</div>}</div>
    </div>
  )
}

export default QAImpover
