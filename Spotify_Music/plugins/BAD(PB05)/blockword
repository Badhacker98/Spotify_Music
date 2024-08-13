import re
import asyncio
from pyrogram import Client, filters
from Spotify_Music import app

NOT_WORDS = [
    "mc",
    "bc",
    "fuck",
    "mf",
    # add more blacklist words
]



def check_words(text, words):
    return any(re.search(rf'\b\w*{word}\w*\b', text, re.IGNORECASE) for word in words)


@app.on_message(filters.text)
async def handler(client, message):
    if check_words(message.text, NOT_WORDS): 
        try:
            await message.delete()
        except Exception as e:
            print(f"Failed to delete message: {e}")
