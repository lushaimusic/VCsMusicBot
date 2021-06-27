from pyrogram import Client

from VCsMusicBot import config

client = Client(config.SESSION_NAME, config.API_ID, config.API_HASH)
run = client.run
