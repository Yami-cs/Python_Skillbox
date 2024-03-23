from flask import Flask, request, jsonify
import subprocess
import signal

app = Flask(__name__)

@app.route('/execute_code', methods=['POST'])
def execute_code():
    try:
        # Получаем код и тайм-аут из запроса
        code = request.form.get('code')
        timeout = int(request.form.get('timeout'))

        # Запускаем процесс с указанным кодом
        process = subprocess.Popen(['python', '-c', code], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Ожидаем выполнения процесса с тайм-аутом
        try:
            stdout, stderr = process.communicate(timeout=timeout)
            return jsonify({'result': stdout.decode('utf-8')})
        except subprocess.TimeoutExpired:
            # Если тайм-аут истек, завершаем процесс
            process.kill()
            return jsonify({'error': 'Execution timed out'})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
