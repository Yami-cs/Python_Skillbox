from datetime import datetime

def get_weekday_greeting(name):
    # Get the current weekday (0 = Monday, 6 = Sunday)
    weekday = datetime.today().weekday()

    # Define the weekdays in Russian with proper declensions
    weekdays = [
        "понедельника",
        "вторника",
        "среды",
        "четверга",
        "пятницы",
        "субботы",
        "воскресенья"
    ]

    if weekday in [0, 1, 3, 6]:
        greeting = f"Хорошего {weekdays[weekday]}, {name}!"
    else:
        greeting = f"Хорошей {weekdays[weekday]}, {name}!"

    return greeting

if __name__ == "__main__":
    # Read the name from the URL (you can replace this with actual URL parsing)
    name = "Саша"  # Example name

    # Get the weekday greeting
    result = get_weekday_greeting(name)
    print(result)
