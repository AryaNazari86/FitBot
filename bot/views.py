import json
import requests
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from bot.credintials import TOKEN, API_URL, URL
from bot.methods.settings import *
from user.models import User
from bot.methods.general import *
from bot.methods.bmi import *
from bot.methods.bmr import *
from .credintials import BOT_USERNAME, CHANNEL_ID, PLATFORM

@csrf_exempt
def bot(request):
    try:
        if request.method == 'POST':
            message = json.loads(request.body.decode('utf-8'))
            #print(json.dumps(message, indent=4))        

            # Fetch data related to the message
            try:
                user_id = message['message']['from']['id']
                chat_id = message['message']['chat']['id']
                msg = message['message']
                type = 0
            except:
                user_id = message['callback_query']['from']['id']
                chat_id = message['callback_query']['message']['chat']['id']
                msg = message['callback_query']['message']
                type = 1

            if (user_id != chat_id) and (type == 0) and not (BOT_USERNAME in message['message'].get('text')):
                return HttpResponse('ok')
                

            state = 0

            if (not User.objects.filter(user_id=user_id, platform=PLATFORM).exists()):
                user = User.objects.create(
                    id = PLATFORM + "_" + str(user_id) if (PLATFORM == "TG") else str(user_id) ,
                    platform = PLATFORM,
                    user_id=user_id,
                    first_name=msg['from']['first_name'],
                )
                user.save()

                if type == 0 and msg.get('text')[:6] == '/start':
                    add_invite(user_id, msg.get('text')[7:])

            else:
                user = User.objects.get(
                    platform = PLATFORM,
                    user_id=user_id
                )

                state = user.state

            # Check is user has joined the channel
            req = requests.post(
                API_URL + "getChatMember",
                {
                    "chat_id": CHANNEL_ID,
                    "user_id": user_id
                }
            ).json()

            if req['ok'] == False or (req['result']['status'] in ("left", "banned", "restricted")):
                join_channel(chat_id)
                return HttpResponse('ok')
            
            print(state)
            if (not type) and (state == 1):
                set_age(chat_id, user_id, message['message'].get('text'))
            elif (not type) and (state == 2):
                set_height(chat_id, user_id, message['message'].get('text'))
            elif (not type) and (state == 3):
                set_weight(chat_id, user_id, message['message'].get('text'))
            
            elif (not type) and (message['message'].get('text')[:6] == "/start"):
                start(chat_id, user_id)

            elif (not type) and (message['message'].get('text') == strings.MenuStrings.bmi):
                bmi(chat_id, user_id)
            elif (not type) and (message['message'].get('text') == strings.MenuStrings.bmr):
                bmr(chat_id, user_id)
            elif (not type) and (message['message'].get('text') == strings.MenuStrings.update):
                update(chat_id)

            elif type and message['callback_query'].get('data')[0] == 'g':
                set_gender(chat_id, user_id, message['callback_query'].get('data'))

            else:
                Sticker(chat_id)

        return HttpResponse('ok')

    except Exception as e:
        print(e)
        return HttpResponse('ok')


def setwebhook(request):
    response = requests.post(
        API_URL + "setWebhook?url=" + request.build_absolute_uri('/').replace('http', 'https')
    ).json()

    # print(API_URL + "setWebhook?url=" + request.build_absolute_uri('/'))

    return HttpResponse(f"{response}")

