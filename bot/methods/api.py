import requests
from bot.credintials import PLATFORM, TOKEN, API_URL
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
                "text": strings.MenuStrings.plan
            },
        ],
        [
            {
                "text" : strings.MenuStrings.information
            },
            {
                "text" : strings.MenuStrings.guide
            },
        ],
        [
            {
                "text" : strings.MenuStrings.update
            },
            {
                "text" : strings.MenuStrings.contact_us
            },
        ],
    ]
})


def send(method, data):
    if (PLATFORM == "TG") and (data.get('parse_mode') == None):
        data['parse_mode'] = "Markdown"
    
    req = requests.post(
        API_URL + method,
        data
    ).json()

    #print(json.dumps(req, indent = 4))

    return req
