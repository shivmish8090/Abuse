from pyrogram import filters
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

from Banword import Banword as app


# Show Help Menu
@app.on_callback_query(filters.regex("^show_help$"))
async def show_help(_, query: CallbackQuery):
    keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("Admin Commands", callback_data="help_admin")],
            [InlineKeyboardButton("« Back", callback_data="back_to_start")],
        ]
    )
    await query.message.edit_text(
        "**Help Menu**\nSelect a category below:", reply_markup=keyboard
    )


# Admin Commands
@app.on_callback_query(filters.regex("^help_admin$"))
async def help_admin(_, query: CallbackQuery):
    await query.message.edit_text(
        """**Admin Commands:**
        Add me to your group i can delete that Messgaes contains the abuse 
        
•𝖯𝗈𝗐𝖾𝗋𝖽 𝖡𝗒 𝖳𝖾𝖺𝗆 𝖣𝗇𝗌 = @Team_Dns_Network""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("« Back", callback_data="show_help")]]
        ),
    )
