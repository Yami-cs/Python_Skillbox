from flask import Flask, request, jsonify
import subprocess
import shlex

app = Flask(__name__)

@app.route('/ps', methods=['GET'])
def ps_endpoint():
    args: list[str] = request.args.getlist('arg')

    if not args:
        return jsonify(errors=["No arguments provided"]), 400

    quoted_args = [shlex.quote(arg) for arg in args]

    command = ["ps"] + quoted_args

    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return f"<pre>{result.stdout}</pre>"
    except subprocess.CalledProcessError as e:
        return jsonify(errors=[f"Error executing command: {e.stderr}"]), 500

if __name__ == '__main__':
    app.run(debug=True)
