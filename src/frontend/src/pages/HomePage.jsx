import TrainingForm from '../components/TrainingForm'

export default function HomePage() {
  return (
    <div className="container py-5">
      <div className="row justify-content-center">
        <div className="col-lg-8 text-center mb-5">
          <h1 className="display-4 fw-bold text-primary">MI Edzésterv Generátor</h1>
          <p className="lead text-muted">
            Add meg az adataidat, és a mesterséges intelligencia összeállítja a neked legmegfelelőbb edzéstervet és étrendet másodpercek alatt.
          </p>
        </div>
      </div>
      
      <div className="row justify-content-center">
        <div className="col-md-8 col-lg-6">
          <TrainingForm />
        </div>
      </div>
    </div>
  )
}