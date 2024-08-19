import asyncio

from Spotify_Music import app
from pyrogram import filters
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from config import MUSIC_BOT_NAME

@app.on_message(filters.command(["donate, qr, scanner"]))
async def start(client: Client, message: Message):
    await message.reply_video(
        video=f"https://te.legra.ph/file/7fa3be2dbc0e3d63d2c0d.jpg",
        caption=f"❤️ ʜᴇʏ {message.from_user.mention}",
    )
