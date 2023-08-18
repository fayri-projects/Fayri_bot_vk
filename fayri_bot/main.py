#============================================================
from vkbottle.bot import Bot

from config import bot_api, labeler, state_dispenser, db
from handlers import handlers
#============================================================

for handler in handlers:
    labeler.load(handler)
#============================================================

bot = Bot(
    api=bot_api,
    labeler=labeler,
    state_dispenser=state_dispenser
)
#============================================================

db.start_db()
bot.run_forever()