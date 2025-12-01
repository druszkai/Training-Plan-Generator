import { useEffect, useState } from 'react'
import { useParams, Link } from 'react-router-dom'
import axios from 'axios'

export default function ResultPage() {
  const { id } = useParams()
  const [planData, setPlanData] = useState(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => {
    const fetchPlan = async () => {
      try {
        const response = await axios.get(`http://127.0.0.1:8000/api/plan/${id}`)
        
        // Fontos: A backend stringként tárolja a JSON-t, ezért parse-olni kell
        // Ha null jönne vissza, kezeljük le
        const training = response.data.training_plan_json 
          ? JSON.parse(response.data.training_plan_json) 
          : null
          
        const diet = response.data.diet_plan_json 
          ? JSON.parse(response.data.diet_plan_json) 
          : null

        setPlanData({
          ...response.data,
          trainingParsed: training,
          dietParsed: diet
        })
      } catch (err) {
        console.error(err)
        setError("Nem sikerült betölteni az edzéstervet. Lehet, hogy hibás az ID.")
      } finally {
        setLoading(false)
      }
    }

    fetchPlan()
  }, [id])

  if (loading) return (
    <div className="text-center mt-5">
      <div className="spinner-border text-primary" role="status"></div>
      <p className="mt-2">Edzésterv betöltése...</p>
    </div>
  )

  if (error) return (
    <div className="container mt-5 text-center">
      <div className="alert alert-danger">{error}</div>
      <Link to="/" className="btn btn-secondary">Vissza a főoldalra</Link>
    </div>
  )

  return (
    <div className="container py-5">
      <div className="d-flex justify-content-between align-items-center mb-4">
        <h2 className="text-primary">📋 A Te Személyes Terved</h2>
        <Link to="/" className="btn btn-outline-secondary">Új tervezés</Link>
      </div>

      <div className="alert alert-info">
        <strong>Mentsd el ezt a linket!</strong> Bármikor visszatérhetsz ide: <br/>
        <code>{window.location.href}</code>
      </div>

      {/* Edzésterv Megjelenítése */}
      {planData.trainingParsed && (
        <div className="card mb-4 shadow-sm">
          <div className="card-header bg-dark text-white">
            <h4>🏋️ {planData.trainingParsed.title}</h4>
          </div>
          <div className="card-body">
            <div className="table-responsive">
              <table className="table table-hover">
                <thead className="table-light">
                  <tr>
                    <th>Nap</th>
                    <th>Edzés Típusa</th>
                    <th>Időtartam</th>
                  </tr>
                </thead>
                <tbody>
                  {planData.trainingParsed.schedule.map((day, index) => (
                    <tr key={index}>
                      <td className="fw-bold">{day.day}</td>
                      <td>{day.workout}</td>
                      <td>{day.duration}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
            <p className="text-muted mt-2 fst-italic">{planData.trainingParsed.note}</p>
          </div>
        </div>
      )}

      {/* Étrend Megjelenítése */}
      {planData.dietParsed && (
        <div className="card shadow-sm border-success">
          <div className="card-header bg-success text-white">
            <h4>🥗 Táplálkozási Javaslat</h4>
          </div>
          <div className="card-body">
            <div className="row text-center mb-3">
              <div className="col-4">
                <h5>{planData.dietParsed.calories} kcal</h5>
                <small className="text-muted">Napi kalória</small>
              </div>
              <div className="col-8">
                 <div className="d-flex justify-content-around">
                    <span className="badge bg-danger p-2">Fehérje: {planData.dietParsed.macros.protein}</span>
                    <span className="badge bg-warning text-dark p-2">Szénhidrát: {planData.dietParsed.macros.carbs}</span>
                    <span className="badge bg-info text-dark p-2">Zsír: {planData.dietParsed.macros.fats}</span>
                 </div>
              </div>
            </div>
            <hr />
            <p className="lead">{planData.dietParsed.advice}</p>
          </div>
        </div>
      )}
    </div>
  )
}