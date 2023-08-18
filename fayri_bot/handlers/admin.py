#============================================================
from vkbottle.bot import BotLabeler, Message

from modules import AdminRule
#============================================================

admin = BotLabeler()
admin.vbml_ignore_case = True
admin.message_view.replace_mention = True

admin.auto_rules.append(AdminRule())
#============================================================

@admin.message(text="hello")
async def hello(m:Message):
    await m.answer("hello")