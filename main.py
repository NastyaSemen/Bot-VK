import vk_api
from vk_api .keyboard import VkKeyboard, VkKeyboardColor
from vk_api.longpoll import VkLongPoll, VkEventType
from config import TOKEN


def send_message(user_id, message, keyboard=None):
    post = {
        'user_id': user_id,
        'message': message,
        'random_id': 0
    }

    if None != keyboard:
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
            send_message(user_id, 'Something text...')

        if text == 'start':
            keyboard = VkKeyboard()

            keyboard.add_button('button', VkKeyboardColor.PRIMARY)

            send_message(user_id, 'The first button!')