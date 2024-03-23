import os
import signal
import subprocess

def start_server_on_port(port):
    try:
        subprocess.run(["python", "server.py", f"--port={port}"])
        print(f"Сервер запущен на порту {port}")
    except subprocess.CalledProcessError:
        try:
            result = subprocess.run(["lsof", "-i", f":{port}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            process_info = result.stdout.strip().split("\n")[1]
            process_id = int(process_info.split()[1])
            os.kill(process_id, signal.SIGTERM)
            print(f"Процесс с PID {process_id} завершен")
            subprocess.run(["python", "server.py", f"--port={port}"])
            print(f"Сервер запущен на порту {port}")
        except Exception as e:
            print(f"Ошибка: {e}")

start_server_on_port(5000)
