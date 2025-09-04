from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from Banword import Banword as app
from Banword.helper.database import (
    get_chats,
    get_new_chats,
    get_new_users,
    get_users,
)
from config import OWNER_ID


@app.on_message(filters.command("stats") & filters.user(OWNER_ID))
async def stats_handler(client: Client, message: Message):
    user_data = await get_users()
    chat_data = await get_chats()
    new_users = await get_new_users()
    new_chats = await get_new_chats()

    total_users = len(user_data["users"]) if "users" in user_data else 0
    total_chats = len(chat_data["chats"]) if "chats" in chat_data else 0

    text = (
        "**Bot Stats:**\n\n"
        f"**Total Users:** `{total_users}`\n"
        f"**Total Chats:** `{total_chats}`\n"
        f"**New Users (24 hrs):** `{new_users}`\n"
        f"**New Chats (24 hrs):** `{new_chats}`"
    )

    keyboard = InlineKeyboardMarkup(
        [[InlineKeyboardButton("Close", callback_data="close")]]
    )

    await message.reply_text(text, reply_markup=keyboard)
