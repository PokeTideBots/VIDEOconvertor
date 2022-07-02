from telethon import TelegramClient
from decouple import config
import logging
import time

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID= 17124006
API_HASH= "97e184dc9c07513de148002859aef2b2"
BOT_TOKEN= "5362862681:AAHksypiJVa_UZV78rZqOaGFBDu4BPK-fVg"
BOT_UN= "PokeTideVideoConverterBot"
LOG_CHANNEL= "PokeTideUploads"
ACCESS_CHANNEL= -1001409710934
AUTH_USERS= 1165699179
MONGODB_URI= "mongodb+srv://Mailmirror:fake100@cluster0.5ystf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
FORCESUB= -1001726913223
FORCESUB_UN= "PokeTide"
LOG_ID= -1001645644921

Drone = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 
