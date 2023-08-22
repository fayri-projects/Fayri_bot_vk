#============================================================
from vkbottle.bot import Bot, Message
from config import example_api, db
from modules import MyKeyboard
#============================================================

bot = Bot(api=example_api)
bot.labeler.vbml_ignore_case = True
#============================================================

@bot.on.message(text="Начать")
async def example(m:Message):

    user = db.get_example(m)
    if user:
        names = user[3].split(",")
        
        await m.answer(
            "Здравствуй", 
            keyboard=MyKeyboard.create_example_keyboard(names)
            )
    else:
        await m.answer(
            "У вас нет настроенного примера", 
            keyboard=MyKeyboard.add_example
        )
#============================================================

@bot.on.message(payload={"cmd":"order"})
async def order(m:Message):
    
    await m.answer(
        "Закажи бота чтобы получить полный функционал.", 
        keyboard=MyKeyboard.buy_bot
    )
#============================================================

@bot.on.message(text="nk")
async def example(m:Message):

    await m.answer("ok", keyboard=MyKeyboard.EMPTY_KEYBOARD)
#============================================================

bot.run_forever()