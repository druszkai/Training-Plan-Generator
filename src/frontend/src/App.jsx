import { Routes, Route, Link } from 'react-router-dom'
import HomePage from './pages/HomePage'
import ResultPage from './pages/ResultPage'

// ==========================================
// Fő Alkalmazás Komponens
// ==========================================

function App() {
  return (
    <div className="App min-vh-100 bg-light">
      {/* Navigációs sáv */}
      <nav className="navbar navbar-dark bg-primary mb-4 shadow-sm">
        <div className="container">
          <Link to="/" className="navbar-brand text-white fw-bold">
            🏋️ MI Edzésterv App
          </Link>
        </div>
      </nav>

      {/* Útvonalválasztó */}
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/plan/:id" element={<ResultPage />} />
      </Routes>
    </div>
  )
}

export default App