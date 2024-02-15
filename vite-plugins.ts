import { PluginOption } from "vite"
import react from "@vitejs/plugin-react"
import basicSsl from "@vitejs/plugin-basic-ssl"
import eslint from "vite-plugin-eslint"

const plugins = (mode: string): PluginOption[] => {
  const eslintConfig =
    mode === "development"
      ? {
          failOnError: false,
          failOnWarning: false,
          emitError: true,
          emitWarning: true,
          useEslintrc: true, // Incase you already have eslintrc in the app
        }
      : {
          failOnError: true,
          failOnWarning: false,
          emitError: false,
          emitWarning: false,
          useEslintrc: true, // Incase you already have eslintrc in the app
        }

  return [
    react({ include: "pathToAllReactFiles.{jsx,tsx}" }),
    basicSsl(),
    eslint(eslintConfig),
  ]
}

export default plugins
