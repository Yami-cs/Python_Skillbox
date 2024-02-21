from calendar import c
from flask import Flask
from random import choice
from datetime import timedelta
from datetime import datetime
import os

app = Flask(__name__)

@app.route("/")
def Main():
    return "Главная страница"

@app.route("/hello_world")
def Hello():
    return "Привет, мир!"

@app.route("/cars")
def Cars_list():
    return "Chevrolet, Renault, Ford, Lada"

cats = ["корниш-рекс", "русская голубая", "шотландская вислоухая", "мейн-кун", "манчкин"] 

@app.route("/cats")
def Random_cats():
    return choice(cats)

@app.route("/get_time/now")
def Now_time():
    current_time = datetime.now()
    return f"Точное время: {current_time}"

@app.route("/get_time/future")
def Future_time():
    current_time_after_hour = datetime.now() + timedelta(hours=1)
    return f"Точное время через час будет {current_time_after_hour}"

def Get_text():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__)) 
    BOOK_FILE = os.path.join(BASE_DIR, "war_and_peace.txt") 
    book = open(BOOK_FILE, "r", encoding='utf-8').read().lower().split()
    book = [word.strip('\'\"!@#$%^&*()_+–\-{=\[\]};\\|,.<>\/?') for word in book]
    return book


@app.route("/get_random_word")
def Random_word(): 
    return choice(Get_text())

counter = 0

@app.route("/counter")
def Count(): 
    global counter
    counter += 1
    return f"Страница была открыта {counter} раз(а)."

if __name__ == "__main__":
        app.run()