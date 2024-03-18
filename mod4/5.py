from flask import Flask, request, jsonify
import subprocess
import shlex

app = Flask(__name__)

@app.route('/ps', methods=['GET'])
def ps_endpoint():
    # Get arguments as a list
    args: list[str] = request.args.getlist('arg')

    # Validate input
    if not args:
        return jsonify(errors=["No arguments provided"]), 400

    # Quote arguments to prevent command injection
    quoted_args = [shlex.quote(arg) for arg in args]

    # Construct the command
    command = ["ps"] + quoted_args

    try:
        # Execute the command
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return f"<pre>{result.stdout}</pre>"
    except subprocess.CalledProcessError as e:
        return jsonify(errors=[f"Error executing command: {e.stderr}"]), 500

if __name__ == '__main__':
    app.run(debug=True)
