from pydantic import BaseModel
from typing import Optional

# ==========================================
# Bemeneti (Input) Sémák
# ==========================================

class TrainingPlanCreate(BaseModel):
    """
    Ez a modell validálja a frontendről érkező adatokat, amikor
    a felhasználó rákattint a "Generálás" gombra.
    """
    age: int                # Életkor (pl. 25)
    weight: int             # Testsúly (kg)
    height: int             # Magasság (cm) - a BMI számításhoz hasznos lehet
    gender: str             # Nem (pl. "male", "female")
    fitness_level: str      # Edzettségi szint (pl. "beginner", "advanced")
    goal: str               # Cél (pl. "weight_loss", "muscle_gain")
    days_per_week: int      # Hány napot ér rá edzeni egy héten

    # Példa adat, ami segít a dokumentációban (Swagger UI)
    class Config:
        json_schema_extra = {
            "example": {
                "age": 25,
                "weight": 80,
                "height": 180,
                "fitness_level": "beginner",
                "goal": "muscle_gain",
                "days_per_week": 3
            }
        }

# ==========================================
# Kimeneti (Output) Sémák
# ==========================================

class TrainingPlanResponse(BaseModel):
    """
    Ez a modell határozza meg, hogy mit küldünk vissza a kliensnek.
    Tartalmazza az adatbázisból kiolvasott adatokat és a generált ID-t.
    """
    id: str                         # A generált egyedi azonosító (UUID)
    age: int
    weight: int
    goal: str
    training_plan_json: Optional[str] = None  # Maga az edzésterv szövege
    diet_plan_json: Optional[str] = None      # Étrend szövege

    class Config:
        # Fontos: Ez teszi lehetővé, hogy az SQLAlchemy adatbázis objektumot
        # a Pydantic automatikusan átalakítsa JSON kompatibilis formátummá.
        from_attributes = True