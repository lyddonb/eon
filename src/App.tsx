import { Route, Routes } from "react-router-dom"
import QAImpover from "./pages/QAImprover"

const App = () => {
  return (
    <>
      <Routes>
        <Route path="qa" element={<QAImpover />} />
        <Route path="/" element={<QAImpover />} />
      </Routes>
    </>
  )
}

export default App
