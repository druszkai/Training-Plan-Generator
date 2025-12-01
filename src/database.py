from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 1. Adatbázis elérése (SQLite fájl: edzesek.db)
# A fájl automatikusan létrejön a mappa gyökerében.
SQLALCHEMY_DATABASE_URL = "sqlite:///./edzesek.db"

# A connect_args szükséges SQLite esetén, hogy a szálkezelés megfelelően működjön
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Munkamenet (Session) létrehozó osztály
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Alap osztály a modellekhez
Base = declarative_base()

# 2. Az Adatbázis Modell (Tábla) definíciója
class TrainingPlan(Base):
    """
    Ez az osztály reprezentálja a 'training_plans' táblát az adatbázisban.
    Minden példány egy sornak felel meg.
    """
    __tablename__ = "training_plans"

    # Egyedi azonosító (ez lesz az URL része is, pl. UUID stringként)
    id = Column(String, primary_key=True, index=True)
    
    # Felhasználói bemeneti adatok tárolása (hogy tudjuk, miből készült a terv)
    age = Column(Integer, nullable=False)
    weight = Column(Integer, nullable=False)
    goal = Column(String, nullable=False)
    
    # Az AI által generált kimenetek (JSON szövegként tárolva)
    training_plan_json = Column(Text, nullable=True) # Maga az edzésterv
    diet_plan_json = Column(Text, nullable=True)     # Étrend javaslat

# Segédfüggvény az adatbázis inicializálásához (táblák létrehozása)
def init_db():
    Base.metadata.create_all(bind=engine)