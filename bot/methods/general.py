import json
from bot import strings
from bot.credintials import PLATFORM
from user.models import User
from .api import *


def join_channel(chat_id):
    send(
        'sendMessage',
        {
            "chat_id": chat_id,
            "text": strings.join_channel,
            "reply_markup": json.dumps({
                "inline_keyboard": [
                    [{"text": strings.check_if_joined, "callback_data": "-"}],
                ]
            })
        }
    )


def guide(chat_id):
    send(
        'sendMessage',
        {
            "chat_id": chat_id,
            "text": strings.guide,
            "reply_markup": MENU,
        }
    )

def information(chat_id):
    send(
        'sendMessage',
        {
            "chat_id": chat_id,
            "text": strings.information,
            "reply_markup": MENU,
        }
    )

def contact_us(chat_id):
    send(
        'sendMessage',
        {
            "chat_id": chat_id,
            "text": strings.contact_us,
            "reply_markup": MENU,
        }
    )


def channel(chat_id):
    send(
        'sendPhoto',
        {
            "chat_id": chat_id,
            "from_chat_id": "@darsyarchannel",
            #"photo": DARSYAR_IMAGE_FILE_ID,
            "caption": strings.channel,
            "reply_markup": MENU
        }
    )


def support(chat_id):
    send(
        'sendPhoto',
        {
            "chat_id": chat_id,
            "from_chat_id": "@darsyarchannel",
            #"photo": DARSYAR_IMAGE_FILE_ID,
            "caption": strings.support,
            "reply_markup": MENU
        }
    )


def start(chat_id, user_id):
    user = User.objects.get(platform = PLATFORM, user_id=user_id)

    send(
        'sendMessage',
        {
            "chat_id": chat_id,
            "text": strings.start.format(user),
            "reply_markup": json.dumps({
                "inline_keyboard": [
                    [{"text": strings.male, "callback_data": "g1"}],
                    [{"text": strings.female, "callback_data": "g0"}]
                ]
            })
        }
    )


def Sticker(chat_id):
    send(
        'sendMessage',
        {
            "chat_id": chat_id,
            "text": strings.unknown,
            "reply_markup": MENU,
        }
    )
