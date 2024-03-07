from datetime import datetime

def get_weekday_greeting(name):
    # Get the current weekday (0 = Monday, 6 = Sunday)
    weekday = datetime.today().weekday()

    # Define the weekdays in Russian
    weekdays = [
        "понедельник",
        "вторник",
        "среду",
        "четверг",
        "пятницу",
        "субботу",
        "воскресенье"
    ]

    # Construct the greeting message
    greeting = f"Привет, {name}. Хорошей {weekdays[weekday]}!"
    return greeting

if __name__ == "__main__":
    # Read the name from the URL (you can replace this with actual URL parsing)
    name = "Саша"  # Example name

    # Get the weekday greeting
    result = get_weekday_greeting(name)
    print(result)
