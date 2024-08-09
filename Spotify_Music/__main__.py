import asyncio
import importlib
from sys import argv
from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from Spotify_Music import LOGGER, app, userbot
from Spotify_Music.core.call import Spotify
from Spotify_Music.misc import sudo
from Spotify_Music.plugins import ALL_MODULES
from Spotify_Music.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS





async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("Spotify_Music.plugins" + all_module)
    LOGGER("Spotify_Music.plugins").info("Successfully Imported Modules...")
    await userbot.start()
    await Spotify.start()
    try:
        await Spotify.stream_call("https://graph.org/file/e999c40cb700e7c684b75.mp4")
    except NoActiveGroupCall:
        LOGGER("Spotify_Music").error(
            "Please turn on the videochat of your log group\channel.\n\nStopping Bot..."
        )
        exit()
    except:
        pass
    await Spotify.decorators()
    LOGGER("Spotify_Music").info(
        "╔═════ஜ۩۞۩ஜ════╗\n  🌸ᴍᴀᴅᴇ ʙʏᴇ ᴛᴇᴀᴍ ᴘʙx (sᴜᴋʜ) 🌸\n╚═════ஜ۩۞۩ஜ════╝"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("Spotify_Music").info("Stopping Brandrd Music Bot...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
    
