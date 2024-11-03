import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from Spotify_Music import HELPABLE, LOGGER, app, userbot
from Spotify_Music.core.call import Spotify
from Spotify_Music.plugins import ALL_MODULES
from Spotify_Music.utils.database import get_banned_users, get_gbanned


async def init():
    if len(config.STRING_SESSIONS) == 0:
        LOGGER("Spotify_Music").error(
            "No Assistant Clients Vars Defined!.. Exiting Process."
        )
        return
    if not config.SPOTIFY_CLIENT_ID and not config.SPOTIFY_CLIENT_SECRET:
        LOGGER("Spotify_Music").warning(
            "No Spotify Vars defined. Your bot won't be able to play spotify queries."
        )
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except Exception:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        imported_module = importlib.import_module(all_module)

        if hasattr(imported_module, "__MODULE__") and imported_module.__MODULE__:
            if hasattr(imported_module, "__HELP__") and imported_module.__HELP__:
                HELPABLE[imported_module.__MODULE__.lower()] = imported_module
    LOGGER("Spotify_Music.plugins").info("Successfully Imported All Modules ")
    await userbot.start()
    await Spotify.start()
    LOGGER("Spotify_Music").info("Assistant Started Sucessfully")
    try:
        await Spotify.stream_call(
            "https://graph.org/file/e999c40cb700e7c684b75.mp4"
        )
    except NoActiveGroupCall:
        LOGGER("Spotify_Music").error(
            "Please turn on the videochat of your log group\channel.\n\nStopping Bot..."
        )
        sys.exit()

    await Spotify.decorators()
    LOGGER("Spotify_Music").info("╔═════ஜ۩۞۩ஜ════╗\n  🌸ᴍᴀᴅᴇ ʙʏᴇ ᴛᴇᴀᴍ ᴘʙx (sᴜᴋʜ) 🌸\n╚═════ஜ۩۞۩ஜ════╝")
    await idle()
    await app.stop()
    await userbot.stop()


if __name__ == "__main__":
    app.run(init())
    LOGGER("Spotify_Music").info("Stopping Spotify_Music! GoodBye")
        
