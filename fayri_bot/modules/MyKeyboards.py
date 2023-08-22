#============================================================
from vkbottle import (
    Keyboard,
    KeyboardButtonColor,
    Text,
    OpenLink,
    EMPTY_KEYBOARD
)
from vkbottle.bot import Message
#============================================================

def gen_list(lst: list, num: int):
    for i in range((len(lst) + num-1) // num):
        yield lst[i*num:(i+1)*num]
#============================================================

class MyKeyboard:

    EMPTY_KEYBOARD = EMPTY_KEYBOARD

    menu = (
        Keyboard(one_time=False)
        .add(Text("заказать"), KeyboardButtonColor.POSITIVE)
        .row()
        .add(OpenLink("https://vk.com/@fayri_bots-shablon-tz", "шаблон тз"))
        .row()
        .add(Text("настроить пример"), KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("информация"), KeyboardButtonColor.POSITIVE)
    )
    
    back = (
        Keyboard(one_time=False)
        .add(Text("назад", {"cmd":"menu"}), KeyboardButtonColor.NEGATIVE)
    )

    example = (
        Keyboard(inline=True)
        .add(Text("удалить пример"), KeyboardButtonColor.NEGATIVE)
        .row()
        .add(OpenLink("https://vk.me/fayri_example", "посмотреть"))
    )

    def get_chat(m:Message):
        keyboard = (
            Keyboard(inline=True)
            .add(
                OpenLink(
                    f"https://vk.com/gim{m.group_id}?sel={m.from_id}",
                    "диалог"
                )
            )
        )
        return keyboard
    

    add_example = (
        Keyboard(inline=True)
        .add(OpenLink("https://vk.me/fayri_bots", "создать"))
    )

    buy_bot = (
        Keyboard(inline=True)
        .add(OpenLink("https://vk.me/fayri_bots", "заказать"))
    )

    def create_example_keyboard(names:str):

        keyboard = Keyboard(False)
        
        for name in gen_list(names, 3):
            for button in name:
                keyboard.add(Text(button, {"cmd":"order"}))
            keyboard.row()
        return keyboard