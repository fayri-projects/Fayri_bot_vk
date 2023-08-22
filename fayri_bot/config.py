#============================================================
import os

from vkbottle import API, BuiltinStateDispenser, CtxStorage
from vkbottle.bot import BotLabeler

from modules import BotDB
#============================================================

EXAMPLE_TOKEN = os.environ["FAYRI_EXAMPLE_TOKEN"]
BOT_TOKEN = os.environ["FAYRI_BOT_TOKEN"]
#APP_TOKEN = 

creator_id = 603843114
#============================================================

example_api = API(EXAMPLE_TOKEN)
bot_api = API(BOT_TOKEN)
#app_api = API(APP_TOKEN)

db = BotDB("modules/db.db")
state_dispenser = BuiltinStateDispenser()
ctx = CtxStorage()
labeler = BotLabeler()
#============================================================