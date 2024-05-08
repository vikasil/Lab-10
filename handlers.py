import random
import webbrowser

import requests
import pyautogui

from voice import voice


def thanks(text):
    options = [
        'Было несложно!',
        'Вам спасибо',
        'Обращайтесь'
    ]
    voice.text_to_speech(random.choice(options))


def relax(text):
    options = [
        'Ура, смотрим котиков!',
        'Предлагаю ютуб',
        'Лучше бы погулять сходили'
    ]
    # webbrowser.open('https://youtu.be/C72eSqbw6Wk?feature=shared', new=0, autoraise=True)
    payload = {
        'q': 'cats',
        'regionCode': 'RU',
        'maxResults': '100',
        'key': 'AIzaSyCq-ThhgzsZGFZx-5z-CBOis9bY6e2AA6Y'
    }

    res = requests.get('https://www.googleapis.com/youtube/v3/search', params=payload)
    vid = res.json()
    idx = random.randint(0, 99)
    vid = res.json()['items'][idx]['id']['videoId']
    webbrowser.open(f'https://youtu.be/{vid}feature=shared', new=0, autoraise=True)
    voice.text_to_speech(random.choice(options))


def stop(text):
    options = [
        'За работу',
        'Хватит на сегодня, да?',
    ]
    pyautogui.hotkey('ctrl', 'w')
    voice.text_to_speech(random.choice(options))