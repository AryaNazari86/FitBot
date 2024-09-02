from bot.credintials import PLATFORM
from bot.methods.ai import ai_plan
from bot.methods.api import *
from user.models import User
import persian

def ask_description(chat_id, user_id):
    user = User.objects.get(platform=PLATFORM, user_id=user_id)

    send(
        'sendMessage',
        {
            "chat_id": chat_id,
            "text": strings.ask_description_plan,
            "reply_markup": MENU,
        }
    )

    user.state = 4
    user.save()

def plan(chat_id, user_id, text):
    user = User.objects.get(platform=PLATFORM, user_id=user_id)

    message_id = send(
        'sendMessage',
        {
            "chat_id": chat_id,
            "text": strings.processing_plan,
            #"reply_markup": MENU,
        }
    )['result']['message_id']
    
    send(
        'sendChatAction',
        {
            "chat_id": chat_id,
            "action": "typing",
        }
    )

    req = ai_plan(text)
    print(req)
    send(
        'sendMessage',
        {
            "chat_id": chat_id,
            "text": req,
        }
    )

    send(
        'sendMessage',
        {
            "chat_id": chat_id,
            "text": strings.complete_plan,
            "reply_markup": MENU,
        }
    )

    send(
        'deleteMessage',
        {
            "chat_id": chat_id,
            "message_id": message_id,
        }
    )

    user.state = 0
    user.save()

