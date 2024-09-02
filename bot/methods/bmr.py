from bot.credintials import PLATFORM
from bot.methods.api import *
from user.models import User


def bmr(chat_id, user_id):
    user = User.objects.get(platform=PLATFORM, user_id=user_id)

    if user.is_male:
        bmr = (10 * user.weight) + (6.25 * user.height) - (5 * user.age) + 5
    else:
        bmr = (10 * user.weight) + (6.25 * user.height) - (5 * user.age) - 161

    if bmr < (1500 if user.is_male else 1200):
        range = strings.BMRRanges.below_average
    elif bmr <= (2200 if user.is_male else 1800):
        range = strings.BMRRanges.average
    elif bmr <= (2800 if user.is_male else 2400):
        range = strings.BMRRanges.above_average
    else:
        range = strings.BMRRanges.high

    send(
        'sendMessage',
        {
            "chat_id": chat_id,
            "text": strings.bmr.format(bmr, range),
            "reply_markup": MENU,
        }
    )