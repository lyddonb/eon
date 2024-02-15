import { Persona } from "@/core/personas"

const PersonaDetail = ({ persona }: { persona: Persona }) => {
  return (
    <div>
      <h3>{persona.title}</h3>
      <p>{persona.description}</p>
    </div>
  )
}

const PersonasList = ({ personas }: { personas: Persona[] }) => {
  // render the list of personas
  return (
    <div>
      <h2>Personas</h2>
      {personas.map((persona, index) => (
        <PersonaDetail key={index} persona={persona} />
      ))}
    </div>
  )
}

export default PersonasList
