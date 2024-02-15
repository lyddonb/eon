import { postJson } from "@/http"

export interface Persona {
  title: string
  description: string
}

export const getPersonas = async (question: string) => {
  const url = "api/personas"
  const payload = {
    question: question,
  }
  const result = await postJson(url, payload)
  return (await result.json()) as Persona[]
}
