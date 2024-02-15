import path from "path"
import { defineConfig, loadEnv } from "vite"
import plugins from "./vite-plugins"

export default defineConfig(({ mode }) => {
  const env = loadEnv(mode, process.cwd(), ["VITE_"])

  return {
    plugins: plugins(mode),
    server: {
      port: 9998,
      open: true, // Open the app once its started
      https: true,
      secure: false,
      proxy: {
        '/api': {
          target: "http://127.0.0.1:9999",
          changeOrigin: true,
          secure: false,
          // rewrite: path => path.replace('/api', ''),
          configure: (proxy, _options) => {
            proxy.on('error', (err, _req, _res) => {
              console.log('proxy error', err)
            })
            proxy.on('proxyReq', (proxyReq, req, _res) => {
              console.log('Sending Request to the Target:', proxyReq.host, req.method, req.url)
            })
            proxy.on('proxyRes', (proxyRes, req, _res) => {
              console.log('Received Response from the Target:', proxyRes.statusCode, req.url)
            })
          },
        }
      }
    },
    define: {
      "process.env": {
        ENV_VARIABLE: env.VARIABLE,
      },
      global: {},
      anotherVariable: {},
    },
    resolve: {
      alias: {
        "@": path.resolve(__dirname, "./src"),
      },
    },
  }
})
