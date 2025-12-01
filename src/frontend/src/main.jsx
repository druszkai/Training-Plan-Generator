import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import { BrowserRouter } from 'react-router-dom'

// A Bootstrap CSS-t már behúztuk az index.html-ben CDN-en keresztül.

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    {/* A BrowserRouter teszi lehetővé az oldalak közötti navigációt (pl. /plan/123) */}
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </React.StrictMode>,
)