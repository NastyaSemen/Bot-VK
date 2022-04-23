import vk_api
from vk_api .keyboard import VkKeyboard, VkKeyboardColor
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api import VkUpload
import requests
from vkwave.bots.storage.storages import vk
import json
from typing import Optional

from vkwave.api.methods import APIOptionsRequestContext
from vkwave.bots.storage.base import NO_KEY, AbstractStorage, NoKeyOrValue
from vkwave.bots.storage.types import Dumper, Key, Loader, Value


from config import TOKEN
from films import FILMS, OPINION, DISRIPTION, TOP_10, TOP_10_OPINION, TOP_10_DISRIPTION, TOP_10_GENRE
from random import randint

attachment = None


def send_image(image):
    global attachment
    upload = vk_api.VkUpload(vk)
    photo = upload.photo_messages(image)
    owner_id = photo[0]['owner_id']
    photo_id = photo[0]['id']
    access_key = photo[0]['access_key']
    attachment = f'photo{owner_id}_{access_key}'


def send_message(user_id, message, keyboard=None, attacment=None):
    post = {
        'user_id': user_id,
        'message': message,
        'random_id': 0
    }

    if keyboard != None:
        post['keyboard'] = keyboard.get_keyboard()
    if attacment != None:
        post['attacment'] = ','.join(attacment)
    else:
        post = post

    session.method('messages.send', post)


session = vk_api.VkApi(token=TOKEN)

for event in VkLongPoll(session).listen():

    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        user_id = event.user_id
        text = event.text.lower()

        if text == 'привет':
            send_message(user_id, 'Чем займемся сегодня?')

        if text == 'start':
            send_message(user_id, 'Привет, начинаем?')
            keyboard = VkKeyboard(one_time=True)

            keyboard.add_button('Любой фильм', VkKeyboardColor.PRIMARY)
            keyboard.add_button('Выбрать', VkKeyboardColor.SECONDARY)
            keyboard.add_button('Топ 10', VkKeyboardColor.NEGATIVE)

            send_message(user_id, 'Выберите интересующий вариант:', keyboard)

    print(event.type)

    if event.type == VkEventType.MESSAGE_NEW:
        if event.text == "Любой фильм":
            n = randint(1, 5)

            if n == 1:
                send_message(event.user_id, FILMS.get('Фентези'))
                send_message(event.user_id, OPINION.get(FILMS.get('Фентези')))
                send_message(event.user_id, DISRIPTION.get(FILMS.get('Фентези')))
                send_image("Веном.jpeg")

            elif n == 2:
                send_message(event.user_id, FILMS.get('Романтика'))
                send_message(event.user_id, OPINION.get(FILMS.get('Романтика')))
                send_message(event.user_id, DISRIPTION.get(FILMS.get('Романтика')))

            elif n == 3:
                send_message(event.user_id, FILMS.get('Боевик'))
                send_message(event.user_id, OPINION.get(FILMS.get('Боевик')))
                send_message(event.user_id, DISRIPTION.get(FILMS.get('Боевик')))

            else:
                send_message(event.user_id, FILMS.get('Комедия'))
                send_message(event.user_id, OPINION.get(FILMS.get('Комедия')))
                send_message(event.user_id, DISRIPTION.get(FILMS.get('Комедия')))

        elif event.text == 'Топ 10':

            send_message(event.user_id, '1')
            send_message(event.user_id, TOP_10.get('1'))
            send_message(event.user_id, TOP_10_OPINION.get(TOP_10.get('1')))
            send_message(event.user_id, TOP_10_GENRE.get(TOP_10.get('1')))
            send_message(event.user_id, TOP_10_DISRIPTION.get(TOP_10.get('1')))

            send_message(event.user_id, '2')
            send_message(event.user_id, TOP_10.get('2'))
            send_message(event.user_id, TOP_10_OPINION.get(TOP_10.get('2')))
            send_message(event.user_id, TOP_10_GENRE.get(TOP_10.get('2')))
            send_message(event.user_id, TOP_10_DISRIPTION.get(TOP_10.get('2')))

            send_message(event.user_id, '3')
            send_message(event.user_id, TOP_10.get('3'))
            send_message(event.user_id, TOP_10_OPINION.get(TOP_10.get('3')))
            send_message(event.user_id, TOP_10_GENRE.get(TOP_10.get('3')))
            send_message(event.user_id, TOP_10_DISRIPTION.get(TOP_10.get('3')))

            send_message(event.user_id, '4')
            send_message(event.user_id, TOP_10.get('4'))
            send_message(event.user_id, TOP_10_OPINION.get(TOP_10.get('4')))
            send_message(event.user_id, TOP_10_GENRE.get(TOP_10.get('4')))
            send_message(event.user_id, TOP_10_DISRIPTION.get(TOP_10.get('4')))

            send_message(event.user_id, '5')
            send_message(event.user_id, TOP_10.get('5'))
            send_message(event.user_id, TOP_10_OPINION.get(TOP_10.get('5')))
            send_message(event.user_id, TOP_10_GENRE.get(TOP_10.get('5')))
            send_message(event.user_id, TOP_10_DISRIPTION.get(TOP_10.get('5')))


            send_message(event.user_id, '6')
            send_message(event.user_id, TOP_10.get('6'))
            send_message(event.user_id, TOP_10_OPINION.get(TOP_10.get('6')))
            send_message(event.user_id, TOP_10_GENRE.get(TOP_10.get('6')))
            send_message(event.user_id, TOP_10_DISRIPTION.get(TOP_10.get('6')))

            send_message(event.user_id, '7')
            send_message(event.user_id, TOP_10.get('7'))
            send_message(event.user_id, TOP_10_OPINION.get(TOP_10.get('7')))
            send_message(event.user_id, TOP_10_GENRE.get(TOP_10.get('7')))
            send_message(event.user_id, TOP_10_DISRIPTION.get(TOP_10.get('7')))

            send_message(event.user_id, '8')
            send_message(event.user_id, TOP_10.get('8'))
            send_message(event.user_id, TOP_10_OPINION.get(TOP_10.get('8')))
            send_message(event.user_id, TOP_10_GENRE.get(TOP_10.get('8')))
            send_message(event.user_id, TOP_10_DISRIPTION.get(TOP_10.get('8')))

            send_message(event.user_id, '9')
            send_message(event.user_id, TOP_10.get('9'))
            send_message(event.user_id, TOP_10_OPINION.get(TOP_10.get('9')))
            send_message(event.user_id, TOP_10_GENRE.get(TOP_10.get('9')))
            send_message(event.user_id, TOP_10_DISRIPTION.get(TOP_10.get('9')))

            send_message(event.user_id, '10')
            send_message(event.user_id, TOP_10.get('10'))
            send_message(event.user_id, TOP_10_OPINION.get(TOP_10.get('10')))
            send_message(event.user_id, TOP_10_GENRE.get(TOP_10.get('10')))
            send_message(event.user_id, TOP_10_DISRIPTION.get(TOP_10.get('10')))

        elif event.text == 'Выбрать':

            send_message(event.user_id, 'Какой жанр предпочитаете?')

            keyboard = VkKeyboard(one_time=True)
            keyboard.add_button('Фэнтези', VkKeyboardColor.PRIMARY)
            keyboard.add_button('Романтика', VkKeyboardColor.PRIMARY)
            keyboard.add_button('Боевик', VkKeyboardColor.PRIMARY)
            keyboard.add_button('Комедия', VkKeyboardColor.PRIMARY)

            send_message(event.user_id, 'Выберите интересующий вариант:', keyboard)

        if event.type == VkEventType.MESSAGE_NEW:

            if event.text == 'Фентези':
                send_message(event.user_id, FILMS.get('Фентези'))
                send_message(event.user_id, OPINION.get(FILMS.get('Фентези')))
                send_message(event.user_id, DISRIPTION.get(FILMS.get('Фентези')))

            elif event.text == 'Романтика':
                send_message(event.user_id, FILMS.get('Романтика'))
                send_message(event.user_id, OPINION.get(FILMS.get('Романтика')))
                send_message(event.user_id, DISRIPTION.get(FILMS.get('Романтика')))

            elif event.text == 'Боевик':
                send_message(event.user_id, FILMS.get('Боевик'))
                send_message(event.user_id, OPINION.get(FILMS.get('Боевик')))
                send_message(event.user_id, DISRIPTION.get(FILMS.get('Боевик')))

            elif event.text == 'Комедия':
                send_message(event.user_id, FILMS.get('Комедия'))
                send_message(event.user_id, OPINION.get(FILMS.get('Комедия')))
                send_message(event.user_id, DISRIPTION.get(FILMS.get('Комедия')))
