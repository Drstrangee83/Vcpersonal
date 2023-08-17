import os
import sys
from pyrogram.types import Message
from helpers.command import commandpro
from pyrogram import Client
from os import system, execle, environ
from helpers.decorators import errors, sudo_users_only


@Client.on_message(commandpro(["R", "!restart", "Restart", "/restart"]))
@errors
@sudo_users_only
async def restart_bot(_, message: Message):
    msg = await message.reply("`RESTARTED DONE AB PELO...`")
    args = [sys.executable, "main.py"]
    await msg.edit("» RESTARTED DONE AB PELO...\n» ɴᴏᴡ ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ʙᴏᴛ ᴀғᴛᴇʀ 𝟷 ᴍɪɴᴜᴛᴇ ")
    execle(sys.executable, *args, environ)
    return
