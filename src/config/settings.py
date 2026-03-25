import os
import sys

# =========================
# Pomoćna funkcija za pronalaženje resursa u PyInstaller paketu
# =========================
def resource_path(relative_path):
    """Vraća apsolutnu putanju do resursa, radi i u PyInstaller exe."""
    try:
        # Kada je pokrenuto iz PyInstaller exe, _MEIPASS je privremeni folder
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# =========================
# Detekcija da li radimo iz PyInstaller bundle-a
# =========================
is_frozen = getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS')

# =========================
# Putanje za podatke (baza, slike, logovi)
# =========================
if is_frozen:
    # Kada smo u .exe, koristimo odgovarajuću korisničku putanju za svaki OS
    if sys.platform == 'win32':
        # Windows: %APPDATA%\CameraApp
        base_dir = os.environ.get('APPDATA', '')
        if not base_dir:
            base_dir = os.path.expanduser('~')
        app_folder = os.path.join(base_dir, 'CameraApp')
    else:
        # Linux / macOS: $XDG_CONFIG_HOME/CameraApp ili ~/.config/CameraApp
        base_dir = os.environ.get('XDG_CONFIG_HOME', os.path.expanduser('~/.config'))
        app_folder = os.path.join(base_dir, 'CameraApp')
    DB_DIR = os.path.join(app_folder, 'database')
    DB_PATH = os.path.join(DB_DIR, 'cameras.db')
    LOG_DIR = os.path.join(app_folder, 'logs')
    LOG_FILE = os.path.join(LOG_DIR, 'app.log')
    IMAGES_DIR = os.path.join(app_folder, 'images')
else:
    # Razvojni mod: koristi lokalne foldere u root-u projekta
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DB_DIR = os.path.join(BASE_DIR, 'database')
    DB_PATH = os.path.join(DB_DIR, 'cameras.db')
    LOG_DIR = os.path.join(BASE_DIR, 'logs')
    LOG_FILE = os.path.join(LOG_DIR, 'app.log')
    IMAGES_DIR = os.path.join(BASE_DIR, 'images')

# Kreiraj potrebne foldere ako ne postoje
os.makedirs(DB_DIR, exist_ok=True)
os.makedirs(LOG_DIR, exist_ok=True)
os.makedirs(IMAGES_DIR, exist_ok=True)

# =========================
# APP
# =========================
APP_NAME = "Pregledač kamera"

# =========================
# STATUSI
# =========================
STATUS_ACTIVE = "active"
STATUS_INACTIVE = "inactive"
STATUS_DISMANTLED = "dismantled"

STATUS_OPTIONS = [
    STATUS_ACTIVE,
    STATUS_INACTIVE,
    STATUS_DISMANTLED
]

# =========================
# UI TEKSTOVI
# =========================
TITLE_SUCCESS = "Uspeh"
TITLE_ERROR = "Greška"
TITLE_CONFIRM = "Potvrda"

MSG_CAMERA_ADDED = "Kamera dodata!"
MSG_CAMERA_UPDATED = "Kamera izmenjena!"
MSG_SELECT_CAMERA = "Izaberite kameru."
MSG_DELETE_CONFIRM = "Da li ste SIGURNI da želite da obrišete kameru?\nOva akcija je nepovratna!"

# =========================
# FORMA
# =========================
FORM_ADD_TITLE = "Dodavanje kamere"
FORM_EDIT_TITLE = "Izmena kamere"
FORM_ADD_BUTTON = "Dodaj kameru"
FORM_EDIT_BUTTON = "Izmeni kameru"

# =========================
# FILES
# =========================
IMAGE_FILTER = "Images (*.png *.jpg *.jpeg)"

# =========================
# LOG LEVEL
# =========================
LOG_LEVEL = "DEBUG"