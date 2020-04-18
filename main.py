from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import vk_api
from datetime import datetime
import random
import time
import get_pictures

token = "f7a4b6630f618b01c6bd36ce77152814ff1c6cbca2cbf61c6e26fdbb443f00633db6e8df51380703831c3"
vk_session = vk_api.VkApi(token=token)

session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

def create_keyboard(response):
    keyboard = VkKeyboard(one_time=False)

    if response == 'test':
        keyboard.add_button('Белая кнопка', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('Зелёная кнопка', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button('Красная кнопка', color=VkKeyboardColor.NEGATIVE)

        keyboard.add_line()
        keyboard.add_button('Синяя кнопка', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('Привет', color=VkKeyboardColor.PRIMARY)


    elif response == 'привет':
        keyboard.add_button('Тест', color=VkKeyboardColor.POSITIVE)

    elif response == 'котики':
        keyboard.add_button('Котики!', color=VkKeyboardColor.POSITIVE)

    elif response == 'закрыть':
        print('закрываем клаву')
        return keyboard.get_empty_keyboard()

    keyboard = keyboard.get_keyboard()
    return keyboard

while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print('The message came in: ' + str(datetime.strftime(datetime.now(), '%H:%M')))
            print('Message text: ' + str(event.text))
            print(event.user_id)
            response = event.text.lower()
            keyboard = create_keyboard(response)
            if event.from_user and not (event.from_me):
                if response == 'hello':
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'PrIvEt', 'random_id': 0})
                elif response == "bye":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'PoKeDa', 'random_id': 0})
