PregledacKamera

Desktop aplikacija za pregled, upravljanje i organizaciju podataka o kamerama.

Aplikacija je razvijena u Pythonu koristeći PySide6 za grafički interfejs i SQLite za lokalno čuvanje podataka.

Features

Pregled spiska kamera

Pregled detalja kamera

Dodavanje kamera

Upravljanje podacima o kamerama

Lokalno čuvanje podataka u SQLite bazi

Rad sa slikama kamera

Desktop GUI aplikacija

Standalone executable build

Automatski build za Windows, Linux i macOS putem GitHub Actions

Tech Stack

Python 3.12

PySide6 — desktop GUI framework

Pillow — obrada slika

SQLite — lokalna baza podataka

PyInstaller — packaging i kreiranje standalone executable-a

Project Structure

PregledacKamera/
├── .github/
│   └── workflows/
│       └── build.yaml
│
├── src/
│   ├── config/
│   ├── controllers/
│   ├── database/
│   ├── images/
│   ├── logs/
│   ├── models/
│   ├── repositories/
│   ├── services/
│   ├── ui/
│   ├── utils/
│   │
│   ├── main.py
│   ├── PregledacKamera.spec
│   ├── app.ico
│   └── version_info.txt
│
├── .gitignore
├── README.md
└── requirements.txt

Architecture

Aplikacija koristi slojevitu organizaciju koda sa razdvajanjem odgovornosti između različitih delova sistema.

┌─────────────────────┐
│         UI          │
│      PySide6        │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│    Controllers      │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│      Services       │
│   Business Logic    │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│    Repositories     │
│    Data Access      │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│      Database       │
│       SQLite        │
└─────────────────────┘

Controllers

Kontrolišu interakciju između korisničkog interfejsa i aplikacione logike.

Services

Sadrže aplikacionu i poslovnu logiku.

Repositories

Zaduženi su za pristup i rad sa podacima.

Models

Predstavljaju strukturu podataka koji se koriste u aplikaciji.

Database

Sadrži SQLite bazu i logiku potrebnu za lokalno čuvanje podataka.

UI

Sadrži korisnički interfejs napravljen pomoću PySide6/Qt.

Utils

Sadrži pomoćne komponente i funkcionalnosti koje koriste različiti delovi aplikacije.

Requirements

Za pokretanje aplikacije iz izvornog koda potrebno je:

Python 3.12+

pip

Python virtual environment

Dependency verzije korišćene za projekat nalaze se u requirements.txt.

Running From Source

1. Clone repository

git clone https://github.com/vasovicmilan/PregledacKamera.git
cd PregledacKamera

2. Create virtual environment

Linux / macOS

python3 -m venv .venv

Windows

py -m venv .venv

3. Activate virtual environment

Linux / macOS

source .venv/bin/activate

Windows PowerShell

.venv\Scripts\Activate.ps1

4. Install dependencies

python -m pip install -r requirements.txt

5. Run application

cd src
python main.py

Building the Application

Projekat koristi PyInstaller za kreiranje standalone executable-a.

Iz root direktorijuma projekta:

cd src
python -m PyInstaller --clean PregledacKamera.spec

Nakon uspešnog build-a executable se nalazi u:

src/dist/

Linux

./dist/PregledacKamera

Windows

Windows build generiše:

PregledacKamera.exe

macOS

macOS build se generiše na macOS GitHub Actions runner-u.

PyInstaller pravi platform-specific executable. Zbog toga se Windows executable mora buildovati na Windows-u, Linux executable na Linux-u, a macOS executable na macOS-u.

GitHub Actions

Projekat koristi GitHub Actions za automatsko kreiranje executable buildova.

Workflow se nalazi u:

.github/workflows/build.yaml

Build se automatski pokreće prilikom push-a na main branch, a može se pokrenuti i ručno putem GitHub Actions.

Trenutno se kreiraju buildovi za:

Windows

Linux

macOS

Svaki operativni sistem se build-uje u zasebnom GitHub Actions job-u.

Dependency verzije se učitavaju iz:

requirements.txt

što omogućava konzistentniji build između lokalnog razvoja i CI okruženja.

Generisani executable fajlovi se objavljuju kao GitHub Actions artifacts.

Local Data

Aplikacija koristi SQLite za lokalno čuvanje podataka.

Baza se nalazi u:

src/database/

Logovi aplikacije se čuvaju u:

src/logs/

Slike i ostali lokalni resources nalaze se u odgovarajućim direktorijumima unutar src/.

Development

Projekat je razvijen kao lagana desktop aplikacija sa fokusom na:

jednostavno korisničko iskustvo

lokalno upravljanje podacima

razdvajanje odgovornosti između komponenti

jednostavno održavanje

cross-platform packaging

automatski build putem GitHub Actions

Projekat predstavlja praktičnu implementaciju desktop aplikacije koristeći Python, PySide6, SQLite i PyInstaller.

Project Status

Projekat je funkcionalan i može se pokretati iz izvornog koda ili kao standalone executable.

Trenutni CI/CD setup omogućava automatsko kreiranje buildova za Windows, Linux i macOS.

License

Licenca za projekat trenutno nije definisana.

Dok licenca nije dodata, izvorni kod se ne treba smatrati slobodnim za kopiranje, menjanje ili redistribuciju.