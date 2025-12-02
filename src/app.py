import os
import uuid
import json
import google.generativeai as genai
from dotenv import load_dotenv
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

# Importáljuk a saját moduljainkat
# Megjegyzés: Ha ezek a fájlok ugyanabban a mappában vannak, simán importálhatók
import database
import schemas

# ==========================================
# Konfiguráció
# ==========================================

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    print("⚠️ FIGYELEM: Nincs beállítva a GEMINI_API_KEY a .env fájlban!")
else:
    genai.configure(api_key=GEMINI_API_KEY)

# Adatbázis táblák létrehozása
database.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="MI Edzésterv Generátor")

# ==========================================
# CORS Beállítások
# ==========================================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==========================================
# Segédfüggvények
# ==========================================

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

def generate_with_ai(data: schemas.TrainingPlanCreate):
    
    # MODELL KIVÁLASZTÁSA (Diagnosztika alapján)
    try:
        # A diagnosztika szerint ez a modell elérhető nálad
        model = genai.GenerativeModel('gemini-2.5-flash')
    except Exception:
        # Fallback
        model = genai.GenerativeModel('gemini-2.0-flash')

    # Prompt
    prompt = f"""
    Te egy professzionális személyi edző és dietetikus vagy. 
    Készíts egy részletes heti edzéstervet és étrendet a következő kliensnek:

    - Kor: {data.age} év
    - Testsúly: {data.weight} kg
    - Nem: {data.gender}
    - Magasság: {data.height} cm
    - Edzettségi szint: {data.fitness_level}
    - Cél: {data.goal}
    - Heti edzésnapok száma: {data.days_per_week}

    FELADAT:
    A választ KIZÁRÓLAG érvényes JSON formátumban küldd vissza. Ne írj semmilyen bevezető vagy záró szöveget, csak a nyers JSON-t.
    
    A JSON struktúrája PONTOSAN ez legyen:
    {{
        "training": {{
            "title": "Adj egy motiváló címet a tervnek",
            "schedule": [
                {{
                    "day": "Hétfő", 
                    "workout": "Edzés neve és rövid leírása", 
                    "duration": "pl. 45 perc"
                }},
                ... (Annyi napot generálj, amennyit a felhasználó kért: {data.days_per_week})
            ],
            "note": "Egy rövid szakmai jótanács"
        }},
        "diet": {{
            "calories": "Javasolt napi kalória (csak szám)",
            "macros": {{
                "protein": "Javasolt fehérje (pl. 150g)",
                "carbs": "Javasolt szénhidrát",
                "fats": "Javasolt zsír"
            }},
            "advice": "Rövid táplálkozási tanács"
        }}
    }}
    
    """

    try:
        response = model.generate_content(prompt)
        response_text = response.text.strip()

        # Markdown tisztítás
        if response_text.startswith("```json"):
            response_text = response_text[7:]
        elif response_text.startswith("```"): 
            response_text = response_text[3:]
        if response_text.endswith("```"):
            response_text = response_text[:-3]
        
        response_text = response_text.strip()
        
        parsed_data = json.loads(response_text)

        training_json = json.dumps(parsed_data.get("training"))
        diet_json = json.dumps(parsed_data.get("diet"))

        return training_json, diet_json

    except Exception as e:
        print(f"HIBA AZ AI GENERÁLÁS KÖZBEN: {e}")
        if "429" in str(e):
             print("TIPP: Túl sok kérés rövid idő alatt. Várj egy picit!")
        raise HTTPException(status_code=500, detail=f"AI Generálási hiba: {str(e)}")

# ==========================================
# API Végpontok
# ==========================================

@app.post("/api/generate-plan", response_model=schemas.TrainingPlanResponse)
def generate_plan(plan_data: schemas.TrainingPlanCreate, db: Session = Depends(get_db)):
    plan_id = str(uuid.uuid4())
    training_json, diet_json = generate_with_ai(plan_data)

    db_plan = database.TrainingPlan(
        id=plan_id,
        age=plan_data.age,
        weight=plan_data.weight,
        goal=plan_data.goal,
        training_plan_json=training_json,
        diet_plan_json=diet_json
    )

    db.add(db_plan)
    db.commit()
    db.refresh(db_plan)

    return db_plan

@app.get("/api/plan/{plan_id}", response_model=schemas.TrainingPlanResponse)
def get_plan(plan_id: str, db: Session = Depends(get_db)):
    plan = db.query(database.TrainingPlan).filter(database.TrainingPlan.id == plan_id).first()
    if plan is None:
        raise HTTPException(status_code=404, detail="A keresett edzésterv nem található.")
    return plan
