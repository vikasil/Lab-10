from recognition import  Ears
from calc import Main
from voice import voice
import time
import webbrowser
import random
from tkinter import *

ACTIVATION = 'привет'


def calc():
    if __name__ == '__main__':
        root = Tk()
        root["bg"] = "#000"
        root.geometry("485x550+200+200")
        root.title("Калькулятор")
        root.resizable(False, False)
        app = Main(root)
        app.pack()
        root.mainloop()
        voice.text_to_speech('считайте сколько влезет!')


def search(txt):
    webbrowser.open(f'https://www.yandex.ru/search/?text={txt}&lr=2')
    voice.text_to_speech(f'вот что нашлось по запросу {txt}')


def compliment():
    options = [
        'Вы замечательно выглядите сегодня! ',
        'вы замуррррррррчательны!',
        'Вы освещаете этот мир!',
        'У вас такие красивые и большие глаза, как у котика'
    ]
    voice.text_to_speech(random.choice(options))


def cats():
    webbrowser.open('https://www.youtube.com/watch?v=A-xGjA4TiKo')
    voice.text_to_speech('Включаю котиков!')


listener = Ears()
text_gen = listener.listen()
voice.text_to_speech('Привет! Я голосовой помощник котик!')
for text in text_gen:
    print(text)
    listener.stream.stop_stream()
    time.sleep(0.5)
    listener.stream.start_stream()
    if text.startswith(ACTIVATION):
            text = text.replace(ACTIVATION, '').strip()
            if text.startswith('ты красивая'):
                compliment()
            elif text.startswith('покажи котиков'):
                cats()
            elif text.startswith('найди'):
                text = text.replace('найди', '').strip()
                search(text)
            elif text.startswith('открой калькулятор'):
                calc()
            else:
                voice.text_to_speech('Я не знаю такой команды, простите!')
