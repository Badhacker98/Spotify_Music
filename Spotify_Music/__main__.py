import asyncio
import importlib
from sys import argv
from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from Spotify import LOGGER, app, userbot
from Spotify.core.call import Spotify
from Spotify.misc import sudo
from Spotify.plugins import ALL_MODULES
from Spotify.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS

from Spotify.plugins.tools.clone import restart_bots




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
        importlib.import_module("Spotify.plugins" + all_module)
    LOGGER("Spotify.plugins").info("Successfully Imported Modules...")
    await userbot.start()
    await Spotify.start()
    try:
        await Spotify.stream_call("https://telegra.ph/file/7f3de9e11bca6274101ea.mp4")
    except NoActiveGroupCall:
        LOGGER("Spotify").error(
            "Please turn on the videochat of your log group\channel.\n\nStopping Bot..."
        )
        exit()
    except:
        pass
    await Spotify.decorators()
    LOGGER("Spotify").info(
        "╔═════ஜ۩۞۩ஜ════╗\n  🌸ᴍᴀᴅᴇ ʙʏᴇ ᴛᴇᴀᴍ ᴘʙx (sᴜᴋʜ) 🌸\n╚═════ஜ۩۞۩ஜ════╝"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("Spotify").info("Stopping Brandrd Music Bot...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
