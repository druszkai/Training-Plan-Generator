# **🏋️ MI Edzésterv Generátor**

**Tantárgy:** Szoftverfejlesztés MI támogatással (BME)

**Típus:** Házi feladat

Ez az alkalmazás egy mesterséges intelligenciával (Google Gemini) támogatott webes felület, amely személyre szabott edzésterveket és táplálkozási tanácsokat generál a felhasználó fizikai paraméterei (kor, nem, súly, célok) alapján.

## **📂 Fájlszerkezet**

A projekt legfontosabb elemeinek áttekintése:

/  
├── src/                        \# A teljes forráskód mappája  
│   ├── app.py                  \# Backend belépési pont (FastAPI szerver)  
│   ├── database.py             \# Adatbázis konfiguráció és modellek  
│   ├── schemas.py              \# Pydantic adatvalidációs sémák  
│   └── frontend/               \# React alapú kliensoldali alkalmazás  
│       ├── src/  
│       ├── package.json  
│       └── ...  
├── SPECIFICATION.md            \# Részletes specifikáció és user story-k  
├── DOKUMENTACIO.md             \# Felhasználói és fejlesztői dokumentáció  
└── README.md                   \# Ez a fájl (Telepítés \+ AI Napló)

## **🚀 Telepítési és Futtatási Útmutató**

A rendszer futtatásához **két** külön terminál ablakra lesz szükség (egy a Szervernek, egy a Kliensnek).

### **0\. Előfeltételek**

* **Python 3.10+**  
* **Node.js 18+**  
* **Google Gemini API kulcs** (Ingyenesen beszerezhető a [Google AI Studio](https://aistudio.google.com/)\-ból).

### **1\. Backend (Szerver) Indítása**

Nyisd meg az **első terminált**, és navigálj a src mappába:

cd src

#### **1\. lépés: Környezeti változók beállítása**

Hozz létre egy .env nevű fájlt (kiterjesztés nélkül) a src mappában, és másold bele a kulcsodat:

GEMINI\_API\_KEY=IDE\_MASOLD\_A\_GOOGLE\_API\_KULCSODAT

#### **2\. lépés: Csomagok telepítése**

pip install fastapi uvicorn sqlalchemy google-generativeai python-dotenv

#### **3\. lépés: Szerver indítása**

python \-m uvicorn app:app \--reload

✅ *Ha sikeres, a szerver a http://127.0.0.1:8000 címen figyel.*

### **2\. Frontend (Kliens) Indítása**

Nyisd meg a **második terminált**, és navigálj a frontend mappába:

cd src/frontend

#### **1\. lépés: Csomagok telepítése**

npm install

#### **2\. lépés: Alkalmazás indítása**

npm run dev

✅ *A böngészőben nyisd meg a megjelenő linket (általában: http://localhost:5173).*

# **🤖 MI Használat Dokumentációja (AI Log)**

Alább található a fejlesztés során alkalmazott promptok, a kapott válaszok és a hibaelhárítási lépések részletes naplója.

### **1\. Specifikáció**

**DÁTUM:** 2025.11.28.

**AI:** Gemini AI

**RÉSZ:** Specifikáció

**CÉL:** A Részletes specifikáció kidolgozása, tervek elkészítése.

**PROMPT:**

Te egy szoftverfejlesztő vagy, akinek a feladata egy edzésterv generátor fejlesztése integrált MI használattal. Jelenleg a szoftverfejlesztés egy korai fázisban, a részletes specifikáció megírásánál tart.  
Rövid specifikáció már adott, ezt mellékeltem neked.  
Feladatod ezen rövid specifikációt bővíteni, fontosabb szerepköröket, forgatókönyveket, illetve funkcionális követelményeket megfelelően részletezni. Én python backend-re és és react (vagy valamilyen nem túl bonyolult) frontendre gondoltam, mivel ezekben van jártasságom.

**EREDMÉNY:**  
Elkészítette a SPECIFICATION.md fájlban található, már általam formázott specifikációt. A lényege azonos azzal, amit az MI írt. Ezt validáltam és megfelelőnek ítéltem további promptolás nélkül.

### **2\. Backend Alapok**

**DÁTUM:** 2025.11.28.

**AI:** Gemini AI

**RÉSZ:** Backend

**CÉL:** Adatbázissal foglalkozó kód elkészítése

**PROMPT:**

Most egy python fejlesztő vagy. A korábban elkészített specifikáció alapján segíts a Backend kód elkészítésében a megbeszélt FastAPI és SQL adatbázis (SQLite) adatbázis használatával.  
Javaslatom, hogy a kódot bontsuk szét több részre. Legyen egy, ami az SQLite adatbázissal foglalkozik, illetve egy rész, ami a backend többi részével. Így két fájlt kell majd megírnod. Kezdd először az adatbázissal foglalkozó réteggel.  
A készülő kódot kommenteld az érthetőségért, illetve a konvenciókat betartva átláthatóan írdd.

**EREDMÉNY:**  
Az MI elkészítette a database.py első verzióját a kért módon. Elmondta emellett, hogy a fastapi uvicorn sqlalchemy könyvtárakat le szükséges töltenem.

### **3\. Backend Architektúra**

**DÁTUM:** 2025.11.28.

**AI:** Gemini AI

**RÉSZ:** Backend

**CÉL:** Tudakozás az MI által gondolt optimális backendről

**PROMPT:**

Érdemesnek tartod-e a Backend további komponensekre bontását?

**EREDMÉNY:**  
Javasolta egy három .py fájlból álló szerkezetet, amelyek a következők:

* database.py \- adatbázissal beszélő rész  
* schemas.py \- ez mondja meg mit várunk a frontendtől  
* main.py (később app.py) \- összekötő, fő logikát tartalmazó egység

### **4\. Adatvalidáció**

**DÁTUM:** 2025.11.28.

**AI:** Gemini AI

**RÉSZ:** Backend

**CÉL:** schemas.py elkészítése

**PROMPT:**

Kérlek készítsd el az előbb egyeztetettek alapján a megfelelő schemas.py fájlt. A formai követelményeim azonosak a database.py-nál említettekkel.

**EREDMÉNY:**  
Legenerálta a schemas.py fájl első verzióját. Szerepel benne:

* TrainingPlanCreate \- Validálja a frontendről érkező űrlapadatokat (kor, súly, magasság, célok stb.)  
* TrainingPlanResponse \- Strukturálja a választ, biztosítva, hogy a frontend csak a szükséges adatokat kapja meg.

### **5\. Üzleti Logika (Mock)**

**DÁTUM:** 2025.11.28.

**AI:** Gemini AI

**RÉSZ:** Backend

**CÉL:** main.py fő üzleti logika implementálása

**PROMPT:**

Lépjünk át a main.py, vagyis a fő üzleti logikát tartalmazó fájlra. Először csak mock AI részt implementálj bele az azonnali tesztelés érdekében. Formai követelményekre innentől fogva ugyan azok vonatkoznak minden fájlra: Tiszta kód, konvenciók használata, kommentezés, mint eddig.  
Kösd össze benne az adatbázis használattal és a sémákkal foglalkozó részeket, illetve implementáld az üzleti logikát.

**EREDMÉNY:**  
Létrehozta a main.py fájlt. Definiálta a megfelelő importokat, illetve a megfelelő @post és @get api hívásokat.

### **6\. Backend Hibaelhárítás**

**DÁTUM:** 2025.11.28.

**AI:** Gemini AI

**RÉSZ:** Backend

**CÉL:** Backend tesztelési hiba elhárítása

**PROMPT:**

Az előbb adott parancs lefuttatása, amit a tesztelés érdekében mellékeltél (python \-m uvicorn main:app \--reload) az alábbi hibát dobta.  
ERROR: Error loading ASGI app. Could not import module "main".  
Segíts a hiba elhárításában.

**EREDMÉNY:**  
Az MI segítette diagnosztikával kiderült, hogy a python modulkeresési útvonala nem tartalmazta a main modult. A hibát sikeresen elhárítottuk a könyvtárstruktúra újrakonfigurálásával. Ezek után sikeresen elindult az alkalmazás a 8000 porton. A tesztelés sikeres volt.

### **7\. Frontend Tervezés**

**DÁTUM:** 2025.11.28.

**AI:** Gemini AI

**RÉSZ:** Frontend

**CÉL:** Frontend architektúra tervezése

**PROMPT:**

Te egy frontend fejlesztő vagy. A feladatod egy Python (FastApi) backendhez tartozó kliensoldal elkészítése Vite React környezetben.  
A backend a schemas.py-ban definiált adatmodellekkel dolgozik... Először segíts a frontend struktúrájának felépítésében, adj javaslatokat hozzá. Kódot még ne írj.

**EREDMÉNY:**  
A kliensoldali architektúrát átbeszéltük. Az MI komponens alapú fejlesztést javasolt. A struktúra implementálja a kliensoldali routing-ot a react-router-dom könyvtár segítségével. Az adatfolyam is tisztább lett: Adatbevitel \-\> API kommunikáció állapotjelzéssel \-\> Dinamikus routing generált ID alapján.

### **8\. Frontend Könyvtárak**

**DÁTUM:** 2025.11.28

**AI:** Gemini AI

**RÉSZ:** Frontend

**CÉL:** Szükséges könyvtárak telepítése

**PROMPT:**

Elfogadom az ajánlott architektúrát. Add meg a szükséges kódot a react-router-dom és axios könyvtárak telepítéséhez.

**EREDMÉNY:**  
Megadta a terminálból történő telepítéshez szükséges kódokat. Javasolta a bootstrap telepítését is a kézzel írandó css elkerülése érdekében.

### **9\. Frontend Stílus**

**DÁTUM:** 2025.11.28.

**AI:** Gemini AI

**RÉSZ:** Frontend

**CÉL:** Bootstrap keretrendszer globális elérhetővé tétele.

**PROMPT:**

Módosítsd most úgy az index.html-t, hogy tartalmazzon css keretrendszert. Ez a keretrendszer Bootstrap legyen.

**EREDMÉNY:**  
Megfelelően módosította az index.html fájlt.

### **10\. Frontend Routing**

**DÁTUM:** 2025.11.28.

**AI:** Gemini AI

**RÉSZ:** Frontend

**CÉL:** Main.jsx és App.jsx megírása, tesztelése

**PROMPT:**

Írd meg a main.jsx és App.jsx fájlokat, amelyek beállítják a routingot két útvonalra. Először csak hozz létre két egyszerű placeholder komponenst.

**EREDMÉNY:**  
Létrehozta a main.jsx és App.jsx fájlokat, amelyek teszteléséhez is útmutatót készített. A tesztelés sikeres volt.

### **11\. Űrlap Implementáció**

**DÁTUM:** 2025.11.28.

**AI:** Gemini AI

**RÉSZ:** Frontend

**CÉL:** Űrlap implementálása

**PROMPT:**

Folytasd a feladatot az űrlap implementálásával. A fájl neve legyen TrainingForm, illetve az eredményt a ResultPage nevű komponensben definiáld.

**EREDMÉNY:**  
Implementálta a TrainingForm, ResultPage komponenseket, illetve a HomePage oldalt a specifikációjuk szerint. Emellett eltávolította a tesztelésre használt placeholder elemeket is az App.jsx fájlból.

### **12\. Kommunikációs Hiba**

**DÁTUM:** 2025.11.28.

**AI:** Gemini AI

**RÉSZ:** Kompozit: Frontend \- Backend

**CÉL:** Frontend \- Backend kommunikációs probléma elhárítása

**PROMPT:**

A backend szervert nem sikerült elérnie a react-nak. Mi lehet a probléma?

**EREDMÉNY:**  
Nem futott valójában a backend szerver. Tanulság, hogy két terminál szükséges: egy a frontend-nek, egy a backend-nek.

### **13\. MI Integráció Tervezése**

**DÁTUM:** 2025.11.28.

**AI:** Gemini AI

**RÉSZ:** MI Integráció

**CÉL:** Generatív MI implementálás megkezdése

**PROMPT:**

Minden működik. Most az MI implementáció lenne a következő, amihez én egy gemini modellben gondolkoztam. Segíts az MI implementációjának tervében.

**EREDMÉNY:**  
Vázolta a főbb lépéseket az MI implementációhoz, mint az API kulcs használata, gemini telepítése, rendszer és felhasználói promptok megírása, majd végül a main.py módosítása.

### **14\. MI Kódolás**

**DÁTUM:** 2025.11.28.

**AI:** Gemini AI

**RÉSZ:** MI Integráció

**CÉL:** Mock MI lecserélése valóban működő változatra

**PROMPT:**

Egy Python backend fejlesztő vagy, akinek a feladata a meglévő mock MI lecserélése egy valóban működő változatra. Importáld a gemini és .env könyvtárakat. A mock\_ai\_generate függvényt módosítsd generate\_with\_ai függvényre, ami már valóban működőképes. A működéséhez szükséges promptban add meg a felhasználó életkorát, súlyát, testmagasságát, célját, edzettségi szintjét és ráérését. A választ JSON formátumban kérd.

**EREDMÉNY:**  
Módosította a main.py-t. Lecserélte a benne lévő mock MI hívásokat valódira, azonban hibába futott. A hiba a Gemini API kulcs nem megfelelő használata volt.

### **15\. MI Hibajavítás (Diagnosztika)**

**DÁTUM:** 2025.11.28.

**AI:** Gemini AI

**RÉSZ:** MI Integráció

**CÉL:** Az előbbi promptból kapott hiba kijavítása

**PROMPT:**

Az alábbi hibára jutottam tesztelés közben: HIBA AZ AI GENERÁLÁS KÖZBEN: 404 models/gemini-1.5-flash-latest is not found... Segíts a hiba kijavításában.

**EREDMÉNY:**  
Rövid troubleshooting után az MI generálta a test\_gemini.py-ban található script-et, aminek kimenetének elküldésével kiderült, hogy melyik modell érhető el. A kód javítása után a frontend és backend megfelelően kommunikál.

### **16\. Funkció Bővítés (Nem/Gender)**

**DÁTUM:** 2025.11.28.

**AI:** Gemini AI

**RÉSZ:** Frontend

**CÉL:** Nemek szétválasztása, megfelelő kezelése

**PROMPT:**

Módosítsd megfelelően a TrainingForm.jsx, hogy már a nemet is megfelelően használja, így pontosítva a generált tervet.

**EREDMÉNY:**  
Az új TrainingForm.jsx fájl megfelelően formázva, implementálva a nemekkel. Emellett javította a backend promptot is (app.py), hogy az MI megkapja ezt az adatot.

### **17\. Dokumentálás**

**DÁTUM:** 2025.11.28.

**AI:** Gemini AI

**RÉSZ:** Dokumentáció

**CÉL:** Dokumentáció generálása

**PROMPT:**

Szoftverfejlesztői tudásoddal készíts nekem az előzőekben generált kódról megfelelően tördelt, igényes és részletes dokumentációt.

**EREDMÉNY:**  
Generált egy várt részletességű és igényességű szöveget (DOKUMENTACIO.md).

### **18\. Végső Validálás**

**DÁTUM:** 2025.11.30.

**AI:** Gemini AI

**RÉSZ:** Összesített

**CÉL:** Specifikációk és követelmények meglétének validálása a projektben.

**PROMPT:**

Mellékeltem a követelményeket és specifikációt, amely szerint ezt a programot írni kellett. Validáld, hogy amit eddig írtunk az ezeknek megfelel-e.

**EREDMÉNY:**  
Az MI áttekintette a projektet, és javasolta a README.md összevonását a PROMPTS.md fájllal a beadáshoz való megfelelés érdekében, valamint apró pontosításokat végzett a specifikációban.

### **19\. README.md Előkészítése**

**DÁTUM:** 2025.11.30.

**AI:** Gemini AI

**RÉSZ:** README.md

**CÉL:** README.md fájl elejére rövid tartalom generálása.

**PROMPT:**

Adj egy rövid bevezető szöveget a readme.md fájl elejére, ahol látható, hogy mit hol lehet megtalálni, illetve egy rövid működési útmutató is szerepel benne.

EREDMÉNY:  
Megszerkesztve legenerálta a jelenleg látható szöveget a README.md fájl elejére.