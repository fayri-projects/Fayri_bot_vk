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

class MyKeyboard:

    EMPTY_KEYBOARD = EMPTY_KEYBOARD

    menu = (
        Keyboard(one_time=False)
        .add(Text("отправить тз"))
        .row()
        .add(OpenLink("https://vk.com/@fayri_bots-shablon-tz", "посмотреть шаблон тз"))
        .row()
        .add(Text("настроить пример"))
    )
    
    back = (
        Keyboard(one_time=False)
        .add(Text("назад", {"cmd":"menu"}), KeyboardButtonColor.NEGATIVE)
    )


    example = (
        Keyboard(inline=True)
        .add(Text("удалить пример"))
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