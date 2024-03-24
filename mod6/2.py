import re

def load_english_words(file_path):
    english_words = set()
    with open(file_path, 'r') as file:
        for line in file:
            word = line.strip().lower()
            if len(word) > 4:
                english_words.add(word)
    return english_words

english_words_set = load_english_words('/usr/share/dict/words')

def is_strong_password(password):
    words_in_password = re.findall(r'\b\w+\b', password.lower())
    
    for word in words_in_password:
        if word in english_words_set:
            return False
    
    return True

password1 = "MySecureP@ssw0rd"
password2 = "SuperSecret123"
print(f"Is '{password1}' a strong password? {is_strong_password(password1)}")
print(f"Is '{password2}' a strong password? {is_strong_password(password2)}")
