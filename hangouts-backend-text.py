import os
from pprint import pprint

import requests
from requests.models import Response

# You need to pass WEBHOOK_URL as an environment variable.
WEBHOOK_URL = "https://chat.googleapis.com/v1/spaces/AAAA4j4EfaY/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=S4mNhWa8r5wLWbUx-kG-Lkfah-DJlnt_N_EpVdU8Zlk%3D"
WEBHOOK_URL_JJFRIENDS = "https://chat.googleapis.com/v1/spaces/AAAADlQesiY/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=hpqUCx53GQ1V42LPy59kD7vMmBPrPYXtWHd2MqJDnBI%3D"

def main():
    #res = send_text(text='')
    content = input("What is the quote? ")
    res = send_text(text="\"" + content + "\" -Ember")
    #res2 = send_text_jjfriends(text=content)
    #res = send_text_card(
    #    title="\"" + content + "\"",
    #    subtitle='',
    #    paragraph='<font color=\"#FF0000\">%s-Emo Writer</font>' % ("&emsp;"*20),
    #)
    #res2 = send_text_card_jjfriends(
    #    title="\"" + content + "\"",
    #    subtitle='',
    #    paragraph="<font color=\"#FF0000\">%s-Emo Writer</font>" % ("&emsp;"*20),
    #)
    #pprint(res.json())
    pass


def send_text(text: str) -> Response:
    return requests.post(WEBHOOK_URL, json={'text': text})

def send_text_jjfriends(text: str) -> Response:
    return requests.post(WEBHOOK_URL_JJFRIENDS, json={"text": text})

def send_text_card(title: str, subtitle: str, paragraph: str) -> Response:
    header = {
        'title': title,
        'subtitle': subtitle,
    }
    widget = {'textParagraph': {'text': paragraph}}
    return requests.post(
        WEBHOOK_URL,
        json={
            'cards': [
                {
                    'header': header,
                    'sections': [{'widgets': [widget]}],
                }
            ]
        },
    )

def send_text_card_jjfriends(title: str, subtitle: str, paragraph: str) -> Response:
    header = {
        "title": title,
        "subtitle": subtitle,
    }
    widget = {"textParagraph": {"text": paragraph}}
    return requests.post(
        WEBHOOK_URL_JJFRIENDS,
        json={
            "cards": [
                {
                    "header": header,
                    "sections": [{"widgets": [widget]}],
                }
            ]
        },
   )

if __name__ == '__main__':
    main()
