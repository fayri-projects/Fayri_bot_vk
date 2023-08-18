#============================================================
import os

from vkbottle import API, BuiltinStateDispenser, CtxStorage
from vkbottle.bot import BotLabeler

from modules import BotDB
#============================================================

EXAMPLE_API = ""
BOT_TOKEN = ""
#APP_TOKEN = 

adm_list = [603843114]
creator_id = 603843114
#============================================================

example_api = API(EXAMPLE_API)
bot_api = API(BOT_TOKEN)
#app_api = API(APP_TOKEN)

db = BotDB("modules/db.db")
state_dispenser = BuiltinStateDispenser()
ctx = CtxStorage()
labeler = BotLabeler()
#============================================================