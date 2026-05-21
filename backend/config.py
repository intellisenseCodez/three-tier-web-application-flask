import os
from dotenv import load_dotenv

load_dotenv()  # reads .env in the backend directory


class Config:
    # ── Database ──────────────────────────────────────────────────────────────
    # Reads DATABASE_URL from .env, e.g.:
    #   postgresql://postgres:secret@localhost:5432/demo_db
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "postgresql://postgres:postgres@localhost:5432/demo_db",
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # ── Security ──────────────────────────────────────────────────────────────
    SECRET_KEY = os.getenv("SECRET_KEY", "change-me-in-production")

    # ── CORS ──────────────────────────────────────────────────────────────────
    # Set ALLOWED_ORIGIN in .env to match your frontend URL, e.g. http://localhost:3000
    ALLOWED_ORIGIN = os.getenv("ALLOWED_ORIGIN", "*")