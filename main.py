from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import vk_api
from datetime import datetime
import random
import time
#import get_pictures

token = "f7a4b6630f618b01c6bd36ce77152814ff1c6cbca2cbf61c6e26fdbb443f00633db6e8df51380703831c3"
vk_session = vk_api.VkApi(token=token)

session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

humor = ('— Какая самая нелюбимая группа у евреев? \n— Сектор газа.', 'Почему инвалид остался в прошлом?\n-Потому что он не может идти в ногу со временем', \
'Африканские школьники довели учителя до слёз, чтобы попить', 'Что будет, если долго смотреть на огонь? Тебя уволят из МЧС',\
'Старый нeгр - чёрный бумер', 'Почему хирург не стал оперировать больного раком? Неудобно просто', '-Внучок, а как зовут того немца, от которого я без ума? \n \
-Альцгеймер, бабушка')

hello = ('Приветики', 'Салам алейкум', 'Здравия желаю', 'Салют', 'ЗдАрова, щеглы!', 'Бонжурненько')

how_are_you = ('По тихой грусти', 'C точки зрения банальной эрудиции игнорирую критерии утопического субъективизма, \nконцептуально интерпретируя общепринятые \
дефанизирующие поляризаторы, поэтому консенсус, \nдостигнутый диалектической материальной классификацией всеобщих мотиваций в парадогматических связях предикатов, \n \
решает проблему усовершенствования формирующих геотрансплантационных \n \
квазипузлистатов всех кинетически коррелирующих аспектов, а так нормально.', 'Какие дела? Я не при делах нынче!', 'Дела идут, контора пишет', 'Всё в шоколаде, даже клавиатура!', \
'Затрудняюсь ответить')

def create_keyboard(response):
    keyboard = VkKeyboard(one_time=False)

    if response == 'команды':
        keyboard.add_button('Привет', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('Как дела?', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Шутка', color=VkKeyboardColor.POSITIVE)        

        keyboard.add_line()
        keyboard.add_button('ААААА', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('Тест', color=VkKeyboardColor.PRIMARY)

    elif response == 'как дела?':
        keyboard.add_button('Команды', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('Закрыть', color=VkKeyboardColor.PRIMARY)

    elif response == 'шутка':
        keyboard.add_button('Шутка', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Добавить шутку', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('Закрыть', color=VkKeyboardColor.PRIMARY)

    elif response == 'тест':
        keyboard.add_button('Привет', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('Закрыть', color=VkKeyboardColor.PRIMARY)

    elif response == 'привет':
        keyboard.add_button('Как дела?', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Закрыть', color=VkKeyboardColor.PRIMARY)

    elif response == 'ааааа':
        keyboard.add_button('Закрыть', color=VkKeyboardColor.PRIMARY)

    elif response == 'закрыть':
        print('закрываем клаву')
        return keyboard.get_empty_keyboard()

    keyboard = keyboard.get_keyboard()
    return keyboard

def send_message(vk_session, id_type, id, message=None, attachment=None, keyboard=None):
    vk_session.method('messages.send',{id_type: id, 'message': message, 'random_id': random.randint(-2147483648, +2147483648), "attachment": attachment, 'keyboard': keyboard})

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        print('Написан: ' + str(datetime.strftime(datetime.now(), '%H:%M')))
        print('Текст: ' + str(event.text))
        print(event.user_id)
        response = event.text.lower()
        keyboard = create_keyboard(response)
        if event.from_user and not event.from_me:
            if response == "ааааа":
                send_message(vk_session, 'user_id', event.user_id, message='ША', keyboard=keyboard)
            elif response == "шутка":
                send_message(vk_session, 'user_id', event.user_id, message=humor[random.randint(0, len(humor)-1)] ,keyboard=keyboard)
            elif response == "привет":
                send_message(vk_session, 'user_id', event.user_id, message=hello[random.randint(0, len(hello)-1)] ,keyboard=keyboard)
            elif response == "тест":
                send_message(vk_session, 'user_id', event.user_id, message='Тестовые команды',keyboard=keyboard)
            elif response == 'команды':
                send_message(vk_session, 'user_id', event.user_id, message='Список команд бота:', keyboard=keyboard)
            elif response == 'закрыть':
                send_message(vk_session, 'user_id', event.user_id, message='Крыто',keyboard=keyboard)
            elif response =='как дела?':
                send_message(vk_session, 'user_id', event.user_id, message=how_are_you[random.randint(0, len(how_are_you)-1)] ,keyboard=keyboard)       
            elif response =='*выстрел*':
                send_message(vk_session, 'user_id', event.user_id, message='Неет, я умираю',keyboard=keyboard)
                break

                            
'''

        elif event.from_chat and not event.from_me:
            if response == "котики":
                attachment = get_pictures.get(vk_session, LUL, session_api)
                print(attachment)
                send_message(vk_session, 'chat_id', event.chat_id, message='Держите котиков!', attachment= attachment)
'''                