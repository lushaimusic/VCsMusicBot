from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message

from ..callsmusic.callsmusic import remove
from ..helpers.chat_id import get_chat_id


@Client.on_message(filters.voice_chat_ended)
async def voice_chat_ended(_, message: Message):
    try:
        remove(get_chat_id(message.chat))
    except Exception:
        pass
