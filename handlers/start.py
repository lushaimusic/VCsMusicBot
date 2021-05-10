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




@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hi there! I can play music in voice chats of Telegeam Groups. I have a lot of cool feature that will amaze you!</b> \n\n♪ Do you want me to play music in your Telegram groups'voice chats? <b>Hit /help to know how you can use me.</b> \n\n♪ The Assistant must be in your group to play music in the voice chat of your group.\n\n♪ More info & commands mentioned in the [Helpful Commands.](https://telegra.ph/Group-Music-Bot-05-03)\n\nℹ️ <b>Please Subscribe @ZauteKm For more Info.</b>""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "➕ Add me to Your Group ➕", url="t.me/zk_GvCBot?startgroup=true")
                  ],[
                    InlineKeyboardButton(
                        "🎙️ Group", url="https://t.me/joinchat/7gSUxv6vgQE3M2Fl"
                    ),
                    InlineKeyboardButton(
                        "Channel 📢", url="https://t.me/ZauteKm")
                    ],[
                    InlineKeyboardButton(
                        "👥 Support", url="https://t.me/joinchat/TBKI3d9nCF8xMBsL"
                    ),
                    InlineKeyboardButton(
                        "Feedback 💭", url="https://t.me/ZauteBot"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "🔰 Music Source Code 🔰", url="https://githup.com/ZauteKm/GroupMusicBot-v2"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ <b>Do you want to search for a YouTube video?</b>",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/ZauteKm"
                    )
                ],    
                [    
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("help")
    & filters.private
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b><u>Helpful Commands!</u>
\n/play <song name> - play song you requested
/dplay <song name> - play song you requested via deezer
/splay <song name> - play song you requested via jio saavn
/playlist - Show now playing list
/current - Show now playing
/song <song name> - download songs you want quickly
/search <query> - search videos on youtube with details
/deezer <song name> - download songs you want quickly via deezer
/saavn <song name> - download songs you want quickly via saavn
/video <song name> - download videos you want quickly
\n<u>Admins only</u>
/player - open music player settings panel
/pause - pause song play
/resume - resume song play
/skip - play next song
/end - stop music play
/userbotjoin - invite assistant to your chat
/admincache - Refresh admin list
 </b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/ZauteKm"
                    )
                ]
            ]
        )
    )    
