import { useState } from 'react'
import axios from 'axios'
import { useNavigate } from 'react-router-dom'

export default function TrainingForm() {
  const navigate = useNavigate()
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  // Űrlap állapotának kezelése
  const [formData, setFormData] = useState({
    age: '',
    gender: 'male', // Alapértelmezett érték
    weight: '',
    height: '',
    fitness_level: 'beginner',
    goal: 'weight_loss',
    days_per_week: 3
  })

  // Mezők változásának kezelése
  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    })
  }

  // Beküldés kezelése
  const handleSubmit = async (e) => {
    e.preventDefault()
    setLoading(true)
    setError(null)

    try {
      const payload = {
        age: parseInt(formData.age),
        gender: formData.gender, // Elküldjük a nemet is
        weight: parseInt(formData.weight),
        height: parseInt(formData.height),
        fitness_level: formData.fitness_level,
        goal: formData.goal,
        days_per_week: parseInt(formData.days_per_week)
      }

      const response = await axios.post('http://127.0.0.1:8000/api/generate-plan', payload)
      navigate(`/plan/${response.data.id}`)
      
    } catch (err) {
      console.error("Hiba történt:", err)
      setError("Nem sikerült elérni a szervert. Ellenőrizd, hogy fut-e a backend!")
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="card shadow p-4">
      <h3 className="mb-4 text-center">Add meg az adataidat</h3>
      
      {error && <div className="alert alert-danger">{error}</div>}

      <form onSubmit={handleSubmit}>
        <div className="row">
          {/* Kor */}
          <div className="col-md-4 mb-3">
            <label className="form-label">Kor (év)</label>
            <input 
              type="number" 
              name="age" 
              className="form-control" 
              required 
              min="10" max="100"
              value={formData.age} 
              onChange={handleChange} 
            />
          </div>

          {/* Nem kiválasztása - ÚJ MEZŐ */}
          <div className="col-md-4 mb-3">
            <label className="form-label">Nem</label>
            <select 
                name="gender" 
                className="form-select" 
                value={formData.gender} 
                onChange={handleChange}
            >
                <option value="male">Férfi</option>
                <option value="female">Nő</option>
            </select>
          </div>
          
          {/* Testsúly */}
          <div className="col-md-4 mb-3">
            <label className="form-label">Súly (kg)</label>
            <input 
              type="number" 
              name="weight" 
              className="form-control" 
              required 
              min="30" max="300"
              value={formData.weight} 
              onChange={handleChange} 
            />
          </div>
        </div>

        <div className="row">
           {/* Magasság */}
           <div className="col-md-6 mb-3">
            <label className="form-label">Magasság (cm)</label>
            <input 
              type="number" 
              name="height" 
              className="form-control" 
              required 
              min="100" max="250"
              value={formData.height} 
              onChange={handleChange} 
            />
          </div>

          {/* Edzési napok száma */}
          <div className="col-md-6 mb-3">
            <label className="form-label">Heti edzésnapok</label>
            <input 
              type="number" 
              name="days_per_week" 
              className="form-control" 
              required 
              min="1" max="7"
              value={formData.days_per_week} 
              onChange={handleChange} 
            />
          </div>
        </div>

        {/* Edzettségi szint */}
        <div className="mb-3">
          <label className="form-label">Edzettségi szint</label>
          <select 
            name="fitness_level" 
            className="form-select" 
            value={formData.fitness_level} 
            onChange={handleChange}
          >
            <option value="beginner">Kezdő</option>
            <option value="intermediate">Haladó</option>
            <option value="advanced">Profi</option>
          </select>
        </div>

        {/* Cél */}
        <div className="mb-4">
          <label className="form-label">Mi a célod?</label>
          <select 
            name="goal" 
            className="form-select" 
            value={formData.goal} 
            onChange={handleChange}
          >
            <option value="weight_loss">Fogyás</option>
            <option value="muscle_gain">Izomépítés</option>
            <option value="endurance">Állóképesség növelés</option>
            <option value="health">Általános egészség</option>
          </select>
        </div>

        <button 
          type="submit" 
          className="btn btn-primary w-100 btn-lg" 
          disabled={loading}
        >
          {loading ? (
            <span>
              <span className="spinner-border spinner-border-sm me-2"></span>
              Terv Generálása...
            </span>
          ) : (
            "Generálás Indítása 🚀"
          )}
        </button>
      </form>
    </div>
  )
}