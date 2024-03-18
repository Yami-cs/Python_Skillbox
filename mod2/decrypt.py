def decrypt(ciphertext):
    # Initialize an empty result string
    result = ""

    # Iterate through the characters in the ciphertext
    i = 0
    while i < len(ciphertext):
        char = ciphertext[i]

        # If the character is a dot, check the next character
        if char == ".":
            i += 1
            # Check if there are enough characters left
            if i < len(ciphertext):
                next_char = ciphertext[i]

                # If there are two dots, skip the previous character
                if next_char == ".":
                    result = result[:-1]
                else:
                    result += next_char
        else:
            result += char

        i += 1

    return result

if __name__ == "__main__":
    # Read input from stdin (pipe)
    ciphertext = input().strip()

    # Decrypt the ciphertext
    plaintext = decrypt(ciphertext)
    print(plaintext)
