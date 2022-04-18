import vk_api
from vk_api .keyboard import VkKeyboard, VkKeyboardColor
from vk_api.longpoll import VkLongPoll, VkEventType
from config import TOKEN
from films import FILMS, OPINION, DISRIPTION
from random import randint


def send_message(user_id, message, keyboard=None):
    post = {
        'user_id': user_id,
        'message': message,
        'random_id': 0
    }

    if keyboard != None:
        post['keyboard'] = keyboard.get_keyboard()
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

            if text == 'Любой фильм':
                pass

            if text == 'Выбрать':
                keyboard = VkKeyboard(one_time=True)

                send_message(user_id, 'Какой жанр предпочитаете?')
                keyboard.add_button('Ужасы', VkKeyboardColor.PRIMARY)
                keyboard.add_button('Комедия', VkKeyboardColor.PRIMARY)
                keyboard.add_button('Боевик', VkKeyboardColor.PRIMARY)

                send_message(user_id, 'Выберите интересующий вариант:', keyboard)


            if text == 'Топ 10':
                pass

    print(event.type)

    if event.type == VkEventType.MESSAGE_NEW:
        if event.text == "Любой фильм":
            n = randint(1, 5)
            if n == 1:
                send_message(event.user_id, FILMS.get('Фентези'))
                send_message(event.user_id, OPINION.get(FILMS.get('Фентези')))
                send_message(event.user_id, DISRIPTION.get(FILMS.get('Фентези')))
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
