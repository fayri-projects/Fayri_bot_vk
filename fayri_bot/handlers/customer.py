#============================================================
from vkbottle.bot import BotLabeler, Message

from config import state_dispenser, creator_id, ctx, db
from modules import MyKeyboard, GetTZ, Example
#============================================================

customer = BotLabeler()
customer.vbml_ignore_case = True
customer.message_view.replace_mention = True
#============================================================

@customer.private_message(payload={"command":"start"})
async def start(m:Message):
    user = await m.ctx_api.users.get(m.from_id)
    name = user[0].first_name
    await m.answer(
        f"Здравствуйте {name}!"
    )
    await menu(m)


@customer.private_message(payload={"cmd":"menu"})
@customer.private_message(text=["menu", "меню"])
async def menu(m:Message):

    if await state_dispenser.get(m.from_id):
        await state_dispenser.delete(m.from_id)

    await m.answer("чем я могу вам помочь?", keyboard=MyKeyboard.menu)
#============================================================

@customer.private_message(lev="заказать")
async def get_tz(m:Message):

    await state_dispenser.set(m.from_id, GetTZ.get)
    await m.answer("Прикрепите файл с техническим заданием", keyboard=MyKeyboard.back)
    return


@customer.private_message(state=GetTZ.get)
async def get_tz(m:Message):
    
    if not m.get_attachment_strings():
        await m.answer("Прикреплённый файл не обнаружен")
    else:

        user = await m.ctx_api.users.get(m.from_id)
        name = user[0].first_name
        surname = user[0].last_name

        message=f"НОВЫЙ ЗАКАЗ\n[id{m.from_id}|{name} {surname}]\n{m.text}"

        await m.ctx_api.messages.send(
            creator_id,
            random_id=m.date,
            message=message,
            keyboard=MyKeyboard.get_chat(m)
        )

        await m.answer("Техническое задание отправлено, скоро с вами свяжется администратор")
        await menu(m)
#============================================================

@customer.private_message(lev="настроить пример")
async def customize_example(m:Message):

    user = db.get_example(m)
    
    if user:
        await m.answer("У вас уже есть настроенный пример", keyboard=MyKeyboard.example)
        return

    await state_dispenser.set(m.from_id, Example.number_of_buttons)
    await m.answer("Введите количество кнопок (1-9)", keyboard=MyKeyboard.back)
    return


@customer.private_message(state=Example.number_of_buttons)
async def customize_example_button(m:Message):

    try:
        buttons = int(m.text)
    except ValueError:
        await m.answer("Введите число")
    else:
        if buttons > 9:
            return "Слишком много кнопок"
        ctx.set(f"{m.from_id}_buttons", buttons)
        await state_dispenser.set(m.from_id, Example.button_names)
        return "Введите название кнопок через запятую"
    

@customer.private_message(state=Example.button_names)
async def customize_example_names(m:Message):

    buttons:int = ctx.get(f"{m.from_id}_buttons")
    names = m.text.split(",")
    number_of_names = len(names)

    if buttons > number_of_names:
        await m.answer("Вы ввели названия не ко всем кнопкам")
    elif buttons < number_of_names:
        await m.answer("недостаточно кнопок")
    else:
        db.safe_example(m, buttons, m.text)
        ctx.delete(f"{m.from_id}_buttons")
        await m.answer("Ваш пример готов", keyboard=MyKeyboard.example)
        await state_dispenser.delete(m.from_id)
#============================================================

@customer.private_message(text="удалить пример")
async def del_example(m:Message):

    if db.del_example(m):
        await m.answer("Пример удалён")
    else:
        await m.answer("У вас нет настроенного примера")
#============================================================

@customer.private_message(text="информация")
async def info(m:Message):
    await m.answer(
        """
В нашем чат-боте доступны такие действия:

1. Заказать:
    нажав на эту кнопку вы можете отправить нам своё техническое задание и в ближайшее время с вами свяжется наш администратор для уточнения подробностей заказа.
2. Пример тз:
    тут вы можете посмотреть пример технического задания.
3. Настроить пример:
    Тут уже сейчас вы можешь увидеть как будет выглядеть меню вашего бота.
        """
    )
#============================================================

@customer.private_message()
async def help(m:Message):
    if (await m.ctx_api.messages.get_history(user_id=m.from_id, count=10)).count < 2:
        await menu(m)
    else:
        await m.answer("я не знаю что на это ответить, уже сообщил администратору, ожидайте.")
#============================================================