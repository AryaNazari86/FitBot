from bot.credintials import PLATFORM
from bot.methods.api import *
from user.models import User
import persian

def add_invite(user_id, invitee_id):
    user = User.objects.get(platform=PLATFORM, user_id=user_id)

    try:
        _ = int(invitee_id)
        valid = 1
    except:
        valid = 0

    # print(valid and User.objects.filter(user_id = invitee_id).exists())
    if valid and User.objects.filter(user_id=invitee_id).exists():
        inviter = User.objects.get(platform=PLATFORM, user_id=invitee_id)
        user.inviter = inviter
        user.save()

def set_gender(chat_id, user_id, data):
    user = User.objects.get(platform=PLATFORM, user_id=user_id)

    gender = data[1] == "1"

    user.is_male = gender

    send(
        'sendMessage',
        {
            "chat_id": chat_id,
            "text": strings.confirm_gender.format(strings.male if user.is_male else strings.female),
            "reply_markup": json.dumps({
                "inline_keyboard": [
                    [{"text": strings.back, "callback_data": "/"}],      
                ]
            })
        }
    )

    user.state = 1
    user.save()

def update(chat_id):
    send(
        'sendMessage',
        {
            "chat_id": chat_id,
            "text": strings.update,
            "reply_markup": json.dumps({
                "inline_keyboard": [
                    [{"text": strings.male, "callback_data": "g1"}],
                    [{"text": strings.female, "callback_data": "g0"}]
                ]
            })
        }
    )

def set_age(chat_id, user_id, text):
    user = User.objects.get(platform=PLATFORM, user_id=user_id)

    try:
        text = persian.convert_fa_numbers(text)
        age = int(text)
        user.age = age

        send(
            'sendMessage',
            {
                "chat_id": chat_id,
                "text": strings.confirm_age.format(persian.convert_en_numbers(age)),
                "reply_markup": json.dumps({
                    "inline_keyboard": [
                        [{"text": strings.back, "callback_data": "/"}],      
                    ]
                })
            }
        )

        user.state = 2
        user.save()

    except:
        send(
            'sendMessage',
            {
                "chat_id": chat_id,
                "text": strings.invalid_number,
                "reply_markup": json.dumps({
                    "inline_keyboard": [
                        [{"text": strings.back, "callback_data": "/"}],      
                    ]
                })
            }
        )

def set_height(chat_id, user_id, text):
    user = User.objects.get(platform=PLATFORM, user_id=user_id)

    try:
        text = persian.convert_fa_numbers(text)
        height = eval(text)
        user.height = height

        send(
            'sendMessage',
            {
                "chat_id": chat_id,
                "text": strings.confirm_height.format(persian.convert_en_numbers(height)),
                "reply_markup": json.dumps({
                    "inline_keyboard": [
                        [{"text": strings.back, "callback_data": "/"}],      
                    ]
                })
            }
        )

        user.state = 3
        user.save()

    except:
        send(
            'sendMessage',
            {
                "chat_id": chat_id,
                "text": strings.invalid_number,
                "reply_markup": json.dumps({
                    "inline_keyboard": [
                        [{"text": strings.back, "callback_data": "/"}],      
                    ]
                })
            }
        )

def set_weight(chat_id, user_id, text):
    user = User.objects.get(platform=PLATFORM, user_id=user_id)

    try:
        text = persian.convert_fa_numbers(text)
        weight = eval(text)
        user.weight = weight

        print(send(
            'sendMessage',
            {
                "chat_id": chat_id,
                "text": strings.confirm_weight.format(persian.convert_en_numbers(weight)),
                "reply_markup": MENU,
            }
        ))

        user.state = 0
        user.save()

    except:
        send(
            'sendMessage',
            {
                "chat_id": chat_id,
                "text": strings.invalid_number,
                "reply_markup": json.dumps({
                    "inline_keyboard": [
                        [{"text": strings.back, "callback_data": "/"}],      
                    ]
                })
            }
        )