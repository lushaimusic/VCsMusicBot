from pyrogram.types import Chat


def get_chat_id(chat: Chat):
    if chat.title.startswith('Calls Music: ') and chat.title[14:].isnumeric():
        return int(chat.title[13:])
    return chat.id
