# ZauteMusic (Telegram bot project )
# Copyright (C) 2021  ZauteKm 

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.



from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn




@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        f"""Hi there! I can play music in voice chats of Telegeam Groups. I have a lot of cool feature that will amaze you!\n\n♪ Do you want me to play music in your Telegram groups'voice chats? Please click the \'ℹ️ Helpful Commands ℹ️\' button below to know how you can use me.\n\n♪ The Assistant must be in your group to play music in the voice chat of your group.\n\n♪ More info & commands mentioned in the [ℹ️ Helpful Commands ℹ️](https://telegra.ph/Group-Music-Bot-05-03)\n\nℹ️Please Subscribe @ZauteKm For more Info.""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "ℹ️ Helpful Commands ℹ️", url="https://telegra.ph/Group-Music-Bot-05-03")
                  ],[
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/joinchat/7gSUxv6vgQE3M2Fl"
                    ),
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/ZauteKm"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "YouTube Channel", url="https://youtube.com/c/MizoHelpDesK"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Group Music player is online**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎙️ Support Group 🎙️", url="https://t.me/joinchat/7gSUxv6vgQE3M2Fl")
                ]
            ]
        )
   )

