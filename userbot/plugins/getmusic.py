#Copyright (C) 2020 The Sonia Roy companyy LLC.

#

# Licensed under theSonia Roy Public License, Version 1.d (the "License");

# you may not use this file except in compliance with the License
#modified for PHANTOM by @N_f_x_P_h_a_N_T_o_M
import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
import asyncio
from userbot.utils import admin_cmd


@borg.on(admin_cmd("smd (.*)"))
async def _(event):
    if event.fwd_from:
        return
    name = event.pattern_match.group(1)
    chat = "@SpotifyMusicDownloaderBot"
    await event.edit("```Getting Your Music```")
    async with bot.conversation(chat) as conv:
          await asyncio.sleep(2)
          await event.edit("`Thamba Thamba My Master Ji U Ka Gaana Is Raha Hai Ho Download\nIt Thoda Boht Time LagSakta Hai 😉 Compromise Karo Na Pilij Thoda Sa Bs Thoda Sa\n   So Stay Tuned.....`")
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=752979930))
              await bot.send_message(chat, name)
              respond = await response
          except YouBlockedUserError:
              await event.reply("```Please unblock @SpotifyMusicDownloaderBot and try again```")
              return
          await event.delete()
          await bot.forward_messages(event.chat_id, respond.message)
