import asyncio
from os import remove
from pyrogram import Client, filters
from pyrogram.enums import ChatType
from pyrogram.types import Message
from datetime import datetime
from time import time
from Spotify_Music import app
from pyrogram.errors import MessageDeleteForbidden, RPCError
from asyncio import sleep
from pyrogram import Client, enums
from pyrogram.types import Message, User
from pyrogram import Client, enums, filters
from pyrogram import Client, enums, filters, raw
from pyrogram.errors.exceptions.bad_request_400 import ChatNotModified
from pyrogram.types import ChatPermissions, Message
from os import getenv
from dotenv import load_dotenv
import random

CMDS = ["@ll_BAD_BBY_ll"]

@app.on_message(filters.command(CMDS, prefixes=[""]))
async def handle_incoming_messages(client, message):
    reactions = ['👍','❤️','🔥','🥰','👏','😁','🤩','👌','🥱','😍','❤️‍🔥','💯','🤣','⚡️','😴','👀','🙈','🤝','🤗','🤪','💘','😘','😎']
    if not await react_to_message(client, message, random.choice(reactions)):
        print("All positive reactions failed.")
        return

async def react_to_message(client, message, reactions):
    for reaction in reactions:
        try:
            if hasattr(message, 'id'):
                await client.send_reaction(message.chat.id, message.id, reactions)
                return True
            else:
                print("Message object does not have id attribute.")
                return False
        except Exception as e:
            print(f"An error occurred: {e}")
            continue
    return False
