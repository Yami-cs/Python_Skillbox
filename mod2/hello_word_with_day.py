from flask import Flask
from datetime import datetime

app = Flask(__name__)

# Определяем словарь для соответствия номеров дней недели и их названий на русском
weekdays_dict = {
    0: "Хорошего понедельника",
    1: "Хорошего вторника",
    2: "Хорошей среды",
    3: "Хорошего четверга",
    4: "Хорошей пятницы",
    5: "Хорошей субботы",
    6: "Хорошего воскресенья"
}

@app.route('/hello-world/<name>')
def hello_world(name):
    weekday = datetime.today().weekday()
    day_name = weekdays_dict[weekday]
    return f"Привет, {name}. {day_name}!"

if __name__ == '__main__':
    app.run(debug=True)