#Copyright (C) 2020 The Sonia Roy companyy LLC.
#
# Licensed under theSonia Roy Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
"""Check if userbot alive. Codes by Nfx Phantom . Anybody if tries to change would be taken under serious custody and legal action would definately be taken."""
#IMG CREDITS: @N_f_x_P_h_a_N_T_o_M
import asyncio
from telethon import events
from uniborg.util import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = "https://telegra.ph/file/03aa25cc8d362d0e936e6.jpg"
pm_caption = "`PHANTOM IS:` **ONLINE**\n\n"
pm_caption += "**SYSTEM STATUS**\n"
pm_caption += "`TELETHON VERSION:` **8.0.8**\n`Python:` **6.5.7**\n"
pm_caption += "`DATABASE STATUS:` **Working**\n"
pm_caption += "**Current Branch** : `Nfx`\n"
pm_caption += "**Phantom OS** : `6.62`\n"
pm_caption += "**Current Sat** : `NfxGangSet-9.12`\n"
pm_caption += f"**Mh Owner** : {DEFAULTUSER} \n"
pm_caption += "**Heroku Database** : `AWS - Zinda Hai`\n\n"
pm_caption += "**License** : [Github ID](https://github.com/Nfx-phantom)\n"
pm_caption += "Copyright : [NfxPhantomGang@github](NfxPhantomGang@github.com)\n"
pm_caption += "**Msg Reply Waiting Time** : `Depends Up On My Master `\n"

@borg.on(admin_cmd(pattern=r"alive"))
async def phantom(alive):
    chat = await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete()

    
@borg.on(admin_cmd(pattern=r"Alive", allow_sudo=True))
async def phantom(alive):
    chat = await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)

    
