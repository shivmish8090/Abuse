from pyrogram import filters
from pyrogram.types import CallbackQuery

from Banword import Banword as app


@app.on_callback_query(filters.regex("close"))
async def close_menu(_, query: CallbackQuery):
    try:
        await query.answer()
        await query.message.delete()
    except Exception:
        pass
