from flask import Flask, request

app = Flask(__name__)

@app.route("/max_number/<path:number_list>")
def max_number(number_list):
    # Split the input string into a list of numbers
    try:
        numbers = [int(num) for num in number_list.split("/")]
    except ValueError:
        return "Invalid input: please provide a list of numbers separated by slashes."

    # Find the maximum number
    max_num = max(numbers)

    return f"Максимальное переданное число: {max_num}"

if __name__ == "__main__":
    app.run()
