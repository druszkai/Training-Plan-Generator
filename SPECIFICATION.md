MI Edzésterv Generátor – Rendszerspecifikáció

1. Bevezetés és Célkitűzés
A projekt célja egy mesterséges intelligenciával támogatott webalkalmazás, az MI Edzésterv Generátor létrehozása. Az alkalmazás megoldást nyújt azoknak a felhasználóknak, akik szeretnének személyre szabott edzéstervet és táplálkozási tanácsokat kapni anélkül, hogy személyi edzőhöz kellene fordulniuk.
A rendszer a felhasználó által megadott paraméterek (kor, nem, testsúly, célok, időkeret) alapján egy külső LLM (Large Language Model) API segítségével generál strukturált tervet, amelyet elment, és egy egyedi, megosztható linken keresztül tesz elérhetővé.

2. Szerepkörök
Az alkalmazás egyszerűsített működése miatt nem igényel regisztrációt, így a szerepkörök a következők:

2.1. Látogató (Felhasználó)
    . Eléri a weboldal nyitólapját.
    . Kitölti az edzésterv generálásához szükséges űrlapot.
    . Megkapja a generált edzéstervet.
    . A későbbiekben az egyedi link birtokában bármikor visszatérhet megnézni a tervét.

2.2. Rendszer (Backend + AI Ágens)
    . Fogadja a kéréseket.
    . Validálja a bemeneti adatokat (pl. ne lehessen negatív testsúlyt megadni).
    . Kommunikál a külső AI szolgáltatóval (OpenAI API).
    . Az adatokat adatbázisban tárolja.
    . Generálja a perzisztens elérési útvonalakat (URL).

3. Felhasználói Forgatókönyvek (User Stories)

US-01: Adatok megadása
Mint Látogató, Szeretném megadni a fizikai paramétereimet és céljaimat egy áttekinthető felületen, Azért, hogy a rendszer ezek alapján tudjon nekem tervet készíteni.
    . Elfogadási kritérium: Az űrlap tartalmazza a következő mezőket: Nem, Kor, Testsúly (kg), Magasság (cm), Edzettségi szint (Kezdő/Haladó/Profi), Cél (Fogyás/Izomépítés/Erőnlét), Heti ráérős napok száma.

US-02: Edzésterv generálás
Mint Látogató, Szeretném, ha az adatok beküldése után a rendszer automatikusan létrehozná a tervemet, Azért, hogy ne kelljen kézzel összeállítanom azt.
    . Elfogadási kritérium: A "Generálás" gomb megnyomása után töltőképernyő jelenik meg. A háttérben lefut az AI hívás, és sikeres válasz esetén megjelenik az eredmény oldal.

US-03: Eredmény megtekintése és mentése
Mint Látogató, Szeretném látni a kész heti bontású edzéstervet és a napi kalóriajavaslatot, valamint kapni egy linket, Azért, hogy később is visszataláljak ehhez a tervhez.
    . Elfogadási kritérium: Az eredmény oldalon jól elkülönítve látszik az edzésterv és az étrend. Az oldal URL-je egyedi (pl. /plan/550e8400-e29b...), amely könyvjelzőzhető.


4. Funkcionális Követelmények

4.1. Frontend (React)
    . FR-FE-01: Reszponzív, mobilbarát megjelenés (Bootstrap, Tailwind vagy Material UI használatával).
    . FR-FE-02: Űrlap validáció kliens oldalon (pl. kötelező mezők ellenőrzése).
    . FR-FE-03: "Loading state" kezelése: amíg az AI dolgozik (kb. 5-10 másodperc), a felhasználó kapjon vizuális visszajelzést (spinner).
    . FR-FE-04: Az eredmények strukturált megjelenítése (Táblázatos vagy kártya nézet a napokhoz).

4.2. Backend (Python)
    . FR-BE-01: REST API végpontok biztosítása a frontend számára.
    . FR-BE-02: Bemeneti adatok szerver oldali validációja (Pydantic modellekkel).
    . FR-BE-03: Integráció az OpenAI API-val (vagy hasonló LLM-mel). A promptnak utasítania kell az AI-t, hogy JSON formátumban válaszoljon a könnyebb feldolgozhatóság érdekében.
    . FR-BE-04: Adatbázis kapcsolat kezelése (írás/olvasás).
    . FR-BE-05: Hibakezelés (pl. ha az OpenAI API nem elérhető, megfelelő hibaüzenet küldése a kliensnek).

5. Technológiai Stack
A feladat megvalósításához választott technológiák modern, iparági sztenderdeknek megfelelő eszközök, amelyek támogatják a gyors fejlesztést és az AI integrációt.
    . Frontend: React.js (Vite build tool használatával).
        . Indoklás: Komponens alapú, gyors és könnyen kezelhető state management.
    . Backend: Python - FastAPI.
        . Indoklás: A Python a de facto szabvány az AI projektekben. A FastAPI aszinkron működése és automatikus dokumentációja (Swagger UI) nagyban segíti a fejlesztést.
    . Adatbázis: SQLite.
        . Indoklás: Fájl alapú, nem igényel külön szerver telepítést, a házi feladat méretéhez tökéletesen elegendő és könnyen mozgatható.
    . AI Szolgáltatás: Gemini API (gemini-2.0-flash vagy gemini-2.5-flash).

6. Adatmodell Tervezet
Az alkalmazás egy fő entitást kezel, a generált terveket.

Tábla neve: training_plans
Mezőnév,Típus,Leírás
id,STRING (UUID),"Elsődleges kulcs, egyedi azonosító a linkhez."
user_age,INTEGER,A felhasználó kora.
user_weight,INTEGER,Testsúly (kg).
user_goal,STRING,"Cél (pl. ""fogyás"")."
training_plan_json,TEXT (JSON),Az AI által generált edzésterv strukturált formában.
diet_plan_json,TEXT (JSON),Az AI által generált táplálkozási tanácsok.
created_at,DATETIME,A létrehozás ideje.

7. API Végpontok Terve
A Backend a következő REST végpontokat biztosítja:

7.1. Új terv generálása
    . Útvonal: POST /api/generate-plan
    . Bemenet (Request Body):
        {
        "age": 25,
        "weight": 80,
        "height": 180,
        "fitness_level": "beginner",
        "goal": "muscle_gain",
        "days_per_week": 3
        }

    . Kimenet (Response):
        {
            "plan_id": "550e8400-e29b-41d4-a716-446655440000",
            "status": "success"
        }
    
7.2. Terv lekérése
    . Útvonal: GET /api/plan/{plan_id}
    . Kimenet (Response): Visszaadja a teljes edzéstervet és étrendet JSON formátumban, amit a frontend megjelenít.