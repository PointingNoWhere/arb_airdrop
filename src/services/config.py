from pathlib import Path
from dotenv import load_dotenv
import os

# === Project Root Directory ===
# This dynamically resolves the root of repo no matter where the script is run from
ROOT_DIR = Path(__file__).resolve().parents[2]

# === Data Paths ===
DATA_DIR = ROOT_DIR / "data" / "processed"
MODELS_DIR = ROOT_DIR / "models"
NOTEBOOKS_DIR = ROOT_DIR / "notebooks"
OUTPUTS_DIR = ROOT_DIR / "data" / "outputs"
SRC_DIR = ROOT_DIR / "src"

# === Load Secrets from .env File ===
load_dotenv(dotenv_path=ROOT_DIR / ".env")

# === API Keys & Environment Variables ===
API_KEY = os.getenv("FLIP_API_KEY")
DB_URI = os.getenv("DB_URI")  # Optional, if needed
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")  # default to "development"
