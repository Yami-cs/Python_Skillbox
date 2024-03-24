import re

# Определение соответствия между цифрами и буквами
digit_to_letters = {
    '2': '[abc]',
    '3': '[def]',
    '4': '[ghi]',
    '5': '[jkl]',
    '6': '[mno]',
    '7': '[pqrs]',
    '8': '[tuv]',
    '9': '[wxyz]'
}

def my_t9(digits):
    # Преобразование цифр в регулярное выражение
    pattern = ''.join(digit_to_letters[digit] for digit in digits)

    # Компиляция регулярного выражения
    regex = re.compile(pattern)

    # Открытие файла со словами
    with open('words.txt', 'r') as f:
        # Фильтрация слов, которые соответствуют регулярному выражению
        words = [word.strip() for word in f if regex.fullmatch(word.strip().lower())]

    # Возвращение списка слов
    return words

# Тестирование функции
print(my_t9('22736368'))
