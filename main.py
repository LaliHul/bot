from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
import data
from datetime import datetime
import random
import time

#login, password = data.loginAndPassword()
#vk_session = vk_api.VkApi(login, password)
#vk_session.auth()

token = "f7a4b6630f618b01c6bd36ce77152814ff1c6cbca2cbf61c6e26fdbb443f00633db6e8df51380703831c3"
vk_session = vk_api.VkApi(token=token)

session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print('The message came in: ' + str(datetime.strftime(datetime.now(), '%H:%M')))
            print('Message text: ' + str(event.text))
            print(event.user_id)
