import os

from dotenv import load_dotenv

load_dotenv()
# ------------------------------------------------

API_ID = int(os.environ.get("API_ID", "28795512"))
API_HASH = os.environ.get("API_HASH", "c17e4eb6d994c9892b8a8b6bfea4042a")

# ------------------------------------------------

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

# -----------------------------------------------

OWNER_ID = int(os.environ.get("OWNER_ID", "6955568347"))
LOGGER_ID = int(os.environ.get("LOGGER_ID", "-100"))

# ------------------------------------------------

MONGO_URL = os.environ.get("MONGO_URL", "")

# ------------------------------------------------
