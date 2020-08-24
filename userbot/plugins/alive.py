"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
#IMG CREDITS: @WhySooSerious
import asyncio
from telethon import events
from uniborg.util import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = "https://telegra.ph/file/4fca63b472e86ecb7ae3d.jpg"
pm_caption = "`PHANTOM IS:` **ONLINE**\n\n"
pm_caption += "**SYSTEM STATUS**\n"
pm_caption += "`TELETHON VERSION:` **6.0.9**\n`Python:` **3.7.4**\n"
pm_caption += "`DATABASE STATUS:` **Functional**\n"
pm_caption += "**Current Branch** : `Nfx`\n"
pm_caption += "**Phantom OS** : `3.14`\n"
pm_caption += "**Current Sat** : `NfxGangSet-2.25`\n"
pm_caption += f"¥¥ Mh Owner ¥¥ : {DEFAULTUSER} \n"
pm_caption += "**Heroku Database** : `AWS - Working Properly`\n\n"
pm_caption += "**License** : [Github ID](https://github.com/Nfx-phantom)\n"
pm_caption += "Copyright : By [NfxPhantomGang@github](NfxPhantomGang@github.com)\n"
pm_caption += "**Msg Reply Waiting Time** : `Depends Up On Mh Master `\n"

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

    
