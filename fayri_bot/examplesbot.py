#============================================================
from vkbottle import Keyboard, Text, OpenLink, EMPTY_KEYBOARD
from vkbottle.bot import Bot, Message
from config import example_api, db
#============================================================

bot = Bot(api=example_api)
bot.labeler.vbml_ignore_case = True
#============================================================

def gen_list(lst: list, num: int):
    for i in range((len(lst) + num-1) // num):
        yield lst[i*num:(i+1)*num]
#============================================================

@bot.on.message(text="Начать")
async def example(m:Message):

    user = db.get_example(m)
    if user:
        names = user[3].split(",")
        keyboard = Keyboard(False)
        
        for name in gen_list(names, 3):
            for button in name:
                keyboard.add(Text(button, {"cmd":"order"}))
            keyboard.row()
        
        await m.answer("Здравствуй", keyboard=keyboard)
    else:
        keyboard = (
            Keyboard(inline=True)
            .add(OpenLink("https://vk.me/fayri_bots", "создать"))
        )
        await m.answer("У вас нет настроенного примера",keyboard=keyboard)
#============================================================

@bot.on.message(payload={"cmd":"order"})
async def order(m:Message):
    
    keyboard = (
        Keyboard(inline=True)
        .add(OpenLink("https://vk.me/fayri_bots", "заказать"))
    )
    await m.answer("Закажи бота чтобы получить полный функционал.", keyboard=keyboard)
#============================================================

@bot.on.message(text="nk")
async def example(m:Message):

    await m.answer("ok", keyboard=EMPTY_KEYBOARD)

bot.run_forever()
#============================================================