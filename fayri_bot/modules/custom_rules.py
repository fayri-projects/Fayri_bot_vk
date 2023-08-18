#============================================================
from vkbottle.bot import Message
from vkbottle.dispatch.rules import ABCRule
#============================================================

adm_list = [603843114]
class AdminRule(ABCRule[Message]):

    async def check(self, event: Message) -> bool:
        return event.from_id in adm_list