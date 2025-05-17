print("Getting Started on Python with the Caesar Cypher!!")

# Here's an interesting note:
# It works perfectly in reverse, and you can set any integer as
# the encryption key (making it a lot like an actual encryption key.)
#
# In the future, maybe I could implement a complicated logic for
# securing the key's value (key character count seems like a nice option)
# 🤔😏

your_message = input("Please enter your message for encryption:\n")
key = int(input("\nPlease enter the encryption key:\n"))


def caesar_cipher(message, shift_key):
    result = ""
    for char in message:
        if char.isupper():
            index_value = ord(char) - ord('A')
            new_index_value = (index_value + shift_key) % 26
            new_char = chr(new_index_value + ord('A'))
            result += new_char
        elif char.islower():
            index_value = ord(char) - ord('a')
            new_index_value = (index_value + shift_key) % 26
            new_char = chr(new_index_value + ord('a'))
            result += new_char
        else:
            result += char
    return result


encrypted_message = caesar_cipher(your_message, key)
print("Here's your encrypted message: ", encrypted_message)

decrypted_message = caesar_cipher(encrypted_message, -key)
print("Here's your message again: ", decrypted_message)
