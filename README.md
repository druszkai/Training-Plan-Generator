***MI Edzésterv Generátor***

Ez a projekt a Szoftverfejlesztés MI támogatással tantárgy házi feladatára készült.
Az alkalmazás egy mesterséges intelligenciával (Google Gemini) támogatott webes felület, amely személyre szabott edzésterveket és táplálkozási tanácsokat generál a felhasználó fizikai paraméterei alapján.

**📂 Fájlszerkezet és Tartalom**

Hogy könnyen eligazodj a repository-ban, itt láthatod a legfontosabb elemeket:

    . src/: A teljes forráskód mappája.

    . src/app.py: A Backend belépési pontja (FastAPI szerver).

    . src/database.py: Adatbázis konfiguráció és modellek.

    . src/schemas.py: Adatvalidációs sémák.

    . src/frontend/: A React alapú kliensoldali alkalmazás kódja.

    . SPECIFICATION.md: A szoftver részletes specifikációja (követelmények, user story-k).

    . DOKUMENTACIO.md: Részletes felhasználói és fejlesztői dokumentáció.

    . README.md: Ez a fájl (telepítési útmutató + MI használati napló).

**🚀 Telepítési és Futtatási Útmutató**

A rendszer futtatásához két külön terminál ablakra lesz szükség (egy a Szervernek, egy a Kliensnek).

0. Előfeltételek

    Python 3.10+

    Node.js 18+

    Google Gemini API kulcs (ingyenesen beszerezhető a Google AI Studio-ból).

1. Backend (Szerver) Indítása

    Nyisd meg az első terminált, és navigálj a src mappába:

    cd src

    1. lépés: Környezeti változók beállítása
    Hozz létre egy .env nevű fájlt (kiterjesztés nélkül) a src mappában, és másold bele a kulcsodat:

    GEMINI_API_KEY=IDE_MASOLD_A_GOOGLE_API_KULCSODAT


    2. lépés: Csomagok telepítése

    pip install fastapi uvicorn sqlalchemy google-generativeai python-dotenv


    3. lépés: Szerver indítása

    python -m uvicorn app:app --reload


    Ha sikeres, a szerver a http://127.0.0.1:8000 címen figyel.

2. Frontend (Kliens) Indítása

    Nyisd meg a második terminált, és navigálj a frontend mappába:

    cd src/frontend


    1. lépés: Csomagok telepítése

    npm install


    2. lépés: Alkalmazás indítása
        npm run dev

    A böngészőben nyisd meg a megjelenő linket (általában: http://localhost:5173).

**🤖 MI Használat Dokumentációja (AI Log)**

Alább található a fejlesztés során alkalmazott promptok, a kapott válaszok és a hibaelhárítási lépések részletes naplója.

####################################################

1.
**DÁTUM:** 2025.11.28.
**AI:** Gemini AI
**RÉSZ:** Specifikáció
**CÉL:** A Részletes specifikáció kidolgozása, tervek elkészítése.

**PROMPT:**
Te egy szoftverfejlesztő vagy, akinek a feladata egy edzésterv generátor fejlesztése integrált MI használattal. Jelenleg a szoftverfejlesztés egy korai fázisban, a részletes specifikáció megírásánál tart.

Rövid specifikáció már adott, ezt mellékeltem neked.

Feladatod ezen rövid specifikációt bővíteni, fontosabb szerepköröket, forgatókönyveket, illetve funkcionális követelményeket megfelelően részletezni. Én python backend-re és és react (vagy valamilyen nem túl bonyolult) frontendre gondoltam, mivel ezekben van jártasságom.


**EREDMÉNY:** Elkészítette a SPECIFICATION.md fájlban található, már általam formázott specifikációt. A lényege azonos azzal, amit az MI írt. Ezt validáltam és megfelelőnek ítéltem további promptolás nélkül.

####################################################

2.
**DÁTUM:** 2025.11.28.
**AI:** Gemini AI
**RÉSZ:** Backend
**CÉL:** Adatbázissal foglalkozó kód elkészítése

**PROMPT:**
Most egy python fejlesztő vagy. A korábban elkészített specifikáció alapján segíts a Backend kód elkészítésében a megbeszélt FastAPI és SQL adatbázis (SQLite) adatbázis használatával.



Javaslatom, hogy a kódot bontsuk szét több részre. Legyen egy, ami az SQLite adatbázissal foglalkozik, illetve egy rész, ami a backend többi részével. Így két fájlt kell majd megírnod. Kezdd először az adatbázissal foglalkozó réteggel.



A készülő kódot kommenteld az érthetőségért, illetve a konvenciókat betartva átláthatóan írdd.

**EREDMÉNY:**
Az MI elkészítette a database.py első verzióját a kért módon. Elmondta emellett, hogy a 'fastaou uvicorn sqlalchemy' könyvtárat le szükséges töltenem


####################################################

3.
**DÁTUM:** 2025.11.28.
**AI:** Gemini AI
**RÉSZ:** Backend
**CÉL:** Tudakozás az MI által gondolt optimális backendről

**PROMPT:**
Érdemesnek tartod-e a Backend további komponensekre bontását?

**EREDMÉNY:**
Javasolta egy három .py fájlból álló szerkezetet, amelyek a következők:
database.py - adatbázissal beszélő rész
schemas.py - ez mondja meg mit várunk a frontendtől
main.py - összekötő, fő logikát tartalmazó egység

####################################################

4.
**DÁTUM:** 2025.11.28.
**AI:** Gemini AI
**RÉSZ:** Backend
**CÉL:** schemas.py elkészítése

**PROMPT:**
Kérlek készítsd el az előbb egyeztetettek alapján a megfelelő schemas.py fájlt. A formai követelményeim azonosak a database.py-nál említettekkel.

**EREDMÉNY:**
Legenerálta a schemas.py fájl első verzióját. Szerepel benne:
'TrainingPlanCreate' - Validálja a frontendről érkező űrlapadatokat (kor, súly, magasság, célok stb.)
'TrainingPlanResponse' - Strukturálja a választ, biztosítva, hogy a frontend csak a szükséges adatokat kapja meg
függvények.

####################################################

5.
**DÁTUM:** 2025.11.28.
**AI:** Gemini AI
**RÉSZ:** Backend
**CÉL:** main.py fő üzleti logika implementálása

**PROMPT:**
Lépjünk át a main.py, vagyis a fő üzleti logikát tartalmazó fájlra. Először csak mock AI részt implementálj bele az azonnali tesztelés érdekében. Formai követelményekre innentől fogva ugyan azok vonatkoznak minden fájlra: Tiszta kód, konvenciók használata, kommentezés, mint eddig.
Kösd össze benne az adatbázis használattal és a sémákkal foglalkozó részeket, illetve implementáld az üzleti logikát.

**EREDMÉNY:**
Létrehozta a main.py fájlt. Definiálta a megfelelő importokat, illetve a megfelelő @post és @get api hívásokat.

####################################################

6.
**DÁTUM:** 2025.11.28.
**AI:** Gemini AI
**RÉSZ:** Backend
**CÉL:** Backend tesztelési hiba elhárítása

**PROMPT:**
Az előbb adott parancs lefuttatása, amit a tesztelés érdekében mellékeltél (python -m uvicorn main:app --reload) az alábbi hibát dobta.

INFO:     Will watch for changes in these directories: ['C:\\Users\\ruszk\\OneDrive\\Desktop\\BME\\szabval\\S5\\SzoftMI\\HF\src']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [34196] using StatReload
ERROR:    Error loading ASGI app. Could not import module "main".
INFO:     Stopping reloader process [34196]

Segíts a hiba elhárításában.

**EREDMÉNY:**
Az MI segítette diagnosztikával kiderült, hogy a python modulkeresési útvonala nem tartalmazta a main modult. A hibát sikeresen elhárítottuk a könyvtárstruktúra újrakonfigurálásával. Ezek után sikeresen elindult az alkalmazás a 8000 porton. A tesztelés sikeres volt.

####################################################

7.
**DÁTUM:** 2025.11.28.
**AI:** Gemini AI
**RÉSZ:** Frontend
**CÉL:** Frontend architektúra tervezése

**PROMPT:**
Te egy frontend fejlesztő vagy. A feladatod egy Python (FastApi) backendhez tartozó kliensoldal elkészítése Vite React környezetben.
A backend a schemas.py-ban definiált adatmodellekkel dolgozik, amik tartalmazzák egy ember főbb testi tulajdonságait. Bemenetnek ezt várja. Ezután kimenetként pedig egy JSON objektumot ad vissza, amelyben az edzésterv szerepel.
Először segíts a frontend struktúrájának felépítésében, adj javaslatokat hozzá. Kódot még ne írj.

**EREDMÉNY:**
A kliensoldali architektúrát átbeszéltük. Az MI komponens alapú fejlesztést javasolt, ami a megjelenítési réteget választja el az oldalszintű logikától. A struktúra implementálja a kliensoldali routing-ot a react-router-dom könyvtár segítségével. Az adatfolyam is tisztább lett:
    . Adatbevitel
    . API kommunikáció állapotjelzéssel
    . Dinamikus routing generált ID alapján

####################################################

8.
**DÁTUM:** 2025.11.28
**AI:** Gemini AI
**RÉSZ:** Frontend
**CÉL:** Szükséges könyvtárak telepítése

**PROMPT:**
Elfogadom az ajánlott architektúrát. Add meg a szükséges kódot a react-router-dom és axios könyvtárak telepítéséhez.

**EREDMÉNY:**
Megadta a terminálból történő telepítéshez szükséges kódokat. Javasolta a bootstrap telepítését is a kézzel irandó css elkerülése érdekében.

####################################################

9.
**DÁTUM:** 2025.11.28.
**AI:** Gemini AI
**RÉSZ:** Frontend
**CÉL:** Bootstrap keretrendszer globális elérhetővé tétele.

**PROMPT:**
Módosítsd most úgy az index.html-t, hogy tartalmazzon css keretrendszert. Ez a keretrendszer Bootstrap legyen.
Az index.html-t alább láthatod:
[index.html akkori tartalma]

**EREDMÉNY:**
Megfelelően módosította az index.html fájlt.

####################################################

10.
**DÁTUM:** 2025.11.28.
**AI:** Gemini AI
**RÉSZ:** Frontend
**CÉL:** Main.jsy és App.jsx megírása, tesztelése

**PROMPT:**
Írd meg a main.jsx és App.jsx fájlokat, amelyek beállítják a routingot két útvonalra:
/: ez lesz a főoldal
/plan/:id: ez pedig az eredmény oldal
Először csak hozz létre két egyszerű placeholder komponenst (HomePage.jsx, ResultPage.jsx) egy-egy komponenssel a gyors tesztelés érdekében.

**EREDMÉNY:**
Létrehozta a main.jsx és App.jsx fájlokat, amelyek teszteléséhez is útmutatót készített. A tesztelés sikeres volt.

####################################################

11.
**DÁTUM:** 2025.11.28.
**AI:** Gemini AI
**RÉSZ:** Frontend
**CÉL:** Űrlap implementálása

**PROMPT:**
Folytasd a feladatot az űrlap implementálásával. A fájl neve legyen TrainingForm, illetve az eredményt a ResultPage nevű komponensben definiáld. A keret legyen a HomePage a komponens architektúránál. Legyenek könnyen navigálhatóak, kódjaik érthetőek. A placeholder komponenseket szintén eltávolíthatod a main.jsx és App.jsx fájlokból.

**EREDMÉNY:**
Implementálta a TrainingForm, ResultPage komponenseket, illetve a HomePage oldalt a specifikációjuk szerint. Emellett eltávolította a tesztelésre használt placeholder elemeket is az App.jsx fájlból.

####################################################

12.
**DÁTUM:** 2025.11.28.
**AI:** Gemini AI
**RÉSZ:** Kompozit: Frontend - Backend
**CÉL:** Frontend - Backend kommunikációs probléma elhárítása

**PROMPT:**
A backend szervert nem sikerült elérnie a react-nak. Mi lehet a probléma?

**EREDMÉNY:**
Nem futott valójában a backend szerver. Tanulság, hogy két terminál szükséges: egy a frontend-nek, egy a backend-nek.

####################################################

13.
**DÁTUM:** 2025.11.28.
**AI:** Gemini AI
**RÉSZ:** MI Integráció
**CÉL:** Generatív MI implementálás megkezdése a személyre szabott edzéstervekhez

**PROMPT:**
Minden működik. Most az MI implementáció lenne a következő, amihez én egy gemini modellben gondolkoztam. Segíts az MI implementációjának tervében. Mondd el, honnan kell az API kulcsot generálni, illetve segíts a kulcs megfelelő tárolásában.

**EREDMÉNY:**
Vázolta a főbb lépéseket az MI implementációhoz, mint az API kulcs használata, gemini telepítése, rendszer és felhasználói promptok megírása, majd végül a main.py módosítása.

####################################################

14.
**DÁTUM:** 2025.11.28.
**AI:** Gemini AI
**RÉSZ:** MI Integráció
**CÉL:** Mock MI lecserélése valóban működő változatra

**PROMPT:**
Egy Python backend fejlesztő vagy, akinek a feladata a meglévő mock MI lecserélése egy valóban működő változatra. Importáld a gemini és .env könyvtárakat. Ez utóbbi tartalmazza a Gemini API kulcsát. A mock_ai_generate függvényt módosítsd generate_with_ai függvényre, ami már valóban működőképes. A működéséhez szükséges promptban add meg a felhasználó életkorát, súlyát, testmagasságát, célját, edzettségi szintjét és ráérését. A választ JSON formátumban kérd.

A válasz formátumára ügyelj, hogy illeszkedjen a frontendben specifikáltakra.

**EREDMÉNY:**
Módosította a main.py-t. Lecserélte a benne lévő mock MI hívásokat valódira, azonban hibába futott. A hiba a Gemini API kulcs nem megfelelő használata volt.

####################################################

15.
**DÁTUM:** 2025.11.28.
**AI:** Gemini AI
**RÉSZ:** MI Integráció
**CÉL:** Az előbbi promptból kapott hiba kijavítása

**PROMPT:**
Az alábbi hibára jutottam tesztelés közben: 
HIBA AZ AI GENERÁLÁS KÖZBEN: 404 models/gemini-1.5-flash-latest is not found for API version v1beta, or is not supported for generateContent. Call ListModels to see the list of available models and their supported methods.

Segíts a hiba kijavításában. Ellenőrizd a kulcsomat és az elérhető modelleket. 

**EREDMÉNY:**
Rövid troubleshooting után az MI generálta a test_gemini.py-ban található script-et, aminek kimenetének elküldésével megfelelően működő lett a kód. A frontend és backend megfelelően kommunikálnak.

####################################################

16.
**DÁTUM:** 2025.11.28.
**AI:** Gemini AI
**RÉSZ:** Frontend
**CÉL:** Nemek szétválasztása, megfelelő kezelése

**PROMPT:**
Módosítsd megfelelően a TrainingForm.jsx, hogy már a nemet is megfelelően használja, így pontosítva a generált tervet.

**EREDMÉNY:**
Az új TrainingForm.jsx fájl megfelelően formázva, implementálva a nemekkel. Emellett javította a main.py-ban lévő kódomat is, hogy az megfelelően adja át a promptot az MI-nek.

####################################################

17.
**DÁTUM:** 2025.11.28.
**AI:** Gemini AI
**RÉSZ:** Dokumentáció
**CÉL:** Dokumentáció generálása

**PROMPT:**
Szoftverfejlesztői tudásoddal készíts nekem az előzőekben generált kódról megfelelően tördelt, igényes és részletes dokumentációt.

Elküldtem neked a specifications.md fájlt is, amelyben a szükséges és elvárt specifikációkat találod. Ellenőrizd, hogy mind megvalósul-e.

Elküldöm neked a házi feladat dokumentálásához tartozó formai követelményeket. Ezeket szigorúan tartsd be.

[HF dokumentáció formai követelmények listája a megadott pdf-ből.]

**EREDMÉNY:**
Generált egy várt részletességű és igényességű szöveget, amit nekem már csak .docx fájlba kellett beillesztenem.

####################################################

18.
**DÁTUM:** 2025.11.30.
**AI:** Gemini AI
**RÉSZ:** Összesített
**CÉL:** Specifikációk és követelmények meglétének validálása a projektben.

**PROMPT:**
Mellékeltem a követelményeket és specifikációt, amely szerint ezt a programot írni kellett. Validáld, hogy amit eddig írtunk az ezeknek megfelel-e. Ha nem, akkor szólj a változtatásokról implementáld őket. Az egész projektet nézd át, egészen a backend megírásától a frontend-en át a dokumentációig.

**EREDMÉNY:**
A validációt megfelelően elvégezte. Kézi ellenőrzéssel nem találtam számottevő hibát. Szólt, hogy nem gpt hanem gemini modellt használunk, illetve az újonnan felvett nem attribútumot szintén át kell adni a generatív MI számára.

####################################################

19.
**DÁTUM:** 2025.11.30.
**AI:** Gemini AI
**RÉSZ:** README.md
**CÉL:** README.md fájl elejére rövid tartalom generálása.

**PROMPT:**
Adj egy rövid bevezető szöveget a readme.md fájl elejére, ahol látható, hogy mit hol lehet megtalálni, illetve egy rövid működési útmutató is szerepel benne.

A readme.md fájl végén lesz a jelenlegi prompts.md tartalma, így az rögtön látható lesz.

**EREDMÉNY:**
Megszerkesztve legenerálta a jelenleg látható szöveget a README.mf fájl elejére.