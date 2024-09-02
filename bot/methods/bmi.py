from bot.credintials import PLATFORM
from bot.methods.api import *
from user.models import User


def bmi(chat_id, user_id):
    user = User.objects.get(platform=PLATFORM, user_id=user_id)

    bmi = user.weight / (user.height / 100) / (user.height / 100)

    if bmi < 18.5:
        range = strings.BMIRanges.under_weight
    elif bmi < 25:
        range = strings.BMIRanges.normal
    elif bmi < 30:
        range = strings.BMIRanges.over_weight
    else:
        range = strings.BMIRanges.fat

    send(
        'sendMessage',
        {
            "chat_id": chat_id,
            "text": strings.bmi.format(bmi, range),
            "reply_markup": MENU,
        }
    )