from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/uptime', methods=['GET'])
def get_uptime():
    try:
        # Запускаем команду "uptime" и получаем вывод
        uptime_output = subprocess.check_output(['uptime']).decode('utf-8')
        # Извлекаем значение uptime из вывода
        uptime = uptime_output.split(',')[0]
        return f"Current uptime is {uptime}"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
