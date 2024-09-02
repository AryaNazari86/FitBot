import requests
from bot.credintials import PLATFORM, TOKEN, API_URL, URL
from bot import strings
import json

MENU = json.dumps({
    "keyboard": [
        [
            {
                "text": strings.MenuStrings.bmi
            },
        ],
        [
            {
                "text": strings.MenuStrings.bmr
            },
        ],
        [
            {
                "text" : strings.MenuStrings.update
            },
        ],
    ]
})


def send(method, data):
    if PLATFORM == "TG":
        data['parse_mode'] = "Markdown"
    
    req = requests.post(
        API_URL + method,
        data
    ).json()

    #print(json.dumps(req, indent = 4))

    return req
