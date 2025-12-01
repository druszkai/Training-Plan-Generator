import os
import google.generativeai as genai
from dotenv import load_dotenv

# 1. Betöltjük a környezeti változókat
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

print("\n=== Gemini API Teszt Diagnosztika ===")
print(f"1. API Kulcs ellenőrzése...")

if not api_key:
    print("❌ HIBA: A GEMINI_API_KEY nincs beállítva a .env fájlban!")
    exit(1)
else:
    # Csak az első és utolsó karaktereket írjuk ki biztonsági okból
    masked_key = f"{api_key[:5]}...{api_key[-5:]}"
    print(f"✅ OK: Kulcs megtalálva a .env-ben ({masked_key})")

# 2. Konfigurálás
try:
    genai.configure(api_key=api_key)
except Exception as e:
    print(f"❌ HIBA a konfigurálásnál: {e}")
    exit(1)

print("\n2. Elérhető modellek lekérdezése a Google szerveréről...")
try:
    # Lekérjük a modellek listáját
    models = list(genai.list_models())
    available_models = []
    
    print("   A te kulcsoddal elérhető generáló modellek:")
    for m in models:
        # Csak azokat listázzuk, amik szöveget tudnak generálni (generateContent)
        if 'generateContent' in m.supported_generation_methods:
            # A 'models/' előtagot levágjuk a tisztább név érdekében
            clean_name = m.name.replace('models/', '')
            print(f"    - {clean_name} ({m.name})")
            available_models.append(clean_name)
            
    if not available_models:
        print("❌ HIBA: A list_models() sikeres volt, de nem találtunk 'generateContent' képes modellt.")
        print("   Ok lehet: Az API kulcsnak nincs jogosultsága, vagy lejárt a keret.")
        exit(1)

except Exception as e:
    print(f"❌ KRITIKUS HIBA a modellek listázásakor: {e}")
    print("   Tipp: Ez általában azt jelenti, hogy az API kulcs érvénytelen, vagy nincs netkapcsolat.")
    exit(1)

# 3. Teszt generálás
print("\n3. Teszt generálás indítása...")

# Megpróbáljuk kiválasztani a legmegfelelőbb modellt a listából
# Előnyben részesítjük a 'flash'-t, majd a 'pro'-t
selected_model = None
for m in available_models:
    if 'flash' in m and '1.5' in m:
        selected_model = m
        break
if not selected_model:
    for m in available_models:
        if 'pro' in m and '1.5' in m:
            selected_model = m
            break
if not selected_model:
    selected_model = available_models[0] # Bármi, ami van

print(f"   Kiválasztott teszt modell: '{selected_model}'")

try:
    model = genai.GenerativeModel(selected_model)
    response = model.generate_content("Írj egy szót: Működik!")
    print(f"   VÁLASZ AZ AI-TÓL: {response.text.strip()}")
    print("\n✅ SIKER! A rendszer működőképes.")
    print(f"👉 A main.py-ban használd ezt a modell nevet: '{selected_model}'")
    
except Exception as e:
    print(f"❌ HIBA a generálás során: {e}")

print("=====================================\n")