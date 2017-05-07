import os

PORT = os.getenv("PORT", "8000")
SERVER_DESCRIPTION = os.getenv("SERVER_DESCRIPTION", f"tcp:{PORT}")
DATABASE_URL = os.getenv("DATABASE_URL", "")
