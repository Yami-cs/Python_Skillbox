from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/preview/<int:SIZE>/<path:RELATIVE_PATH>")
def file_preview(SIZE, RELATIVE_PATH):
    # Get the absolute path to the file
    abs_path = os.path.abspath(RELATIVE_PATH)

    try:
        # Read the first SIZE characters from the file
        with open(abs_path, "r") as file:
            file_content = file.read(SIZE)
            result_size = len(file_content)
    except FileNotFoundError:
        return "File not found."

    # Construct the response
    response = f"{abs_path} {result_size}<br>\n{file_content}"
    return response

if __name__ == "__main__":
    app.run()
