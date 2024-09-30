secret_message = "This is a hidden message pass-1234"
number = 11
character_list = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"


def caesar_cipher(text: str, shift: int ):
    result = ""

    for char in text:
        if char in character_list:
            result += character_list[(character_list.index(char) + shift ) % len(character_list)]
        else:
            result += char


    return result

def caeser_decipher(text: str, shift:int):
    result=""
    for char in text:
        if char in character_list:
            result += character_list[(character_list.index(char) - shift ) % len(character_list)]
        else:
            result += char
    return result





secret_message2=caesar_cipher(secret_message, number)

print(caeser_decipher(secret_message2, number))

