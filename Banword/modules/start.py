from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from pyrogram.enums import ChatType
from config import OWNER_ID, BOT_USERNAME
from Banword import Banword as app
from Banword.helper.database import add_user, add_chat

START_IMG = "https://files.catbox.moe/iem38x.jpg"

def get_start_caption(user):
    return f"""
**𝖧𝖾𝗒** {user.mention} 

🤖 I am a **Abuse Remover Bot**.
I delete messages with Abuse word and restrict users who have Banword .

🚫 I also delete messages with **Banword**.
"""

START_BUTTONS = InlineKeyboardMarkup([
    [InlineKeyboardButton("𝖠𝖽𝖽 𝖬𝖾", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
    [InlineKeyboardButton("𝖧𝖾𝗅𝗉 𝖠𝗇𝖽 𝖢𝗈𝗆𝗆𝖺𝗇𝖽", callback_data="show_help")],
    [
        InlineKeyboardButton("𝖲𝗎𝗉𝗉𝗈𝗋𝗍", url="https://t.me/dns_support_group"),
        InlineKeyboardButton("𝖴𝗉𝖽𝖺𝗍𝖾", url="https://t.me/Team_Dns_Network")
    ],
    [InlineKeyboardButton("𝖮𝗐𝗇𝖾𝗋", url="https://t.me/II_RAJPUT_SHIV_OP_II")]
])

PRIVATE_START_BUTTON = InlineKeyboardMarkup([
    [InlineKeyboardButton("𝖯𝗋𝗂𝗏𝖺Ban𝗍𝖺𝗋𝗍", url=f"https://t.me/{BOT_USERNAME}?start=help")]
])

@app.on_message(filters.command("start") & (filters.private | filters.group))
async def start_command(_, message: Message):
    user = message.from_user
    chat = message.chat

    await add_user(user.id)
    if chat.type in [ChatType.GROUP, ChatType.SUPERGROUP]:
        await add_chat(chat.id)

    if chat.type == ChatType.PRIVATE:
        await message.reply_photo(
            photo=START_IMG,
            caption=get_start_caption(user),
            has_spoiler=True,
            reply_markup=START_BUTTONS
        )
    else:
        await message.reply_text(
            f"**𝖧𝖾𝗒 {user.mention}, 𝖳𝗁𝖺𝗇𝗄𝗌 𝖥𝗈𝗋 𝖠𝖽𝖽𝗂𝗇𝗀 𝖬𝖾!**",
            reply_markup=PRIVATE_START_BUTTON
        )

@app.on_callback_query(filters.regex("^back_to_start$"))
async def back_to_start(_, query: CallbackQuery):
    user = query.from_user
    chat_id = query.message.chat.id

    await query.message.delete() 

    await app.send_photo(
        chat_id=chat_id,
        photo=START_IMG,
        caption=get_start_caption(user),
        has_spoiler=True,
        reply_markup=START_BUTTONS
    )
    
