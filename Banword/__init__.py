import asyncio
import logging
import time
from importlib import import_module
from os import listdir, path

from pyrogram import Client

from config import API_HASH, API_ID, BOT_TOKEN, OWNER_ID

loop = asyncio.get_event_loop()
boot = time.time()


logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s",
    level=logging.INFO,
)


Banword = Client(
    ":Banword:",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)
