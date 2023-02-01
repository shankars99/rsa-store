from src.helper import *


def encrypt_message(message_string_object: BinaryString = message, e: int = key.e, n: int = key.n) -> list:
    data.plain_text = message_string_object.int_array
    data.encrypted_text = [pow(data, e, n)
                           for data in message_string_object.int_array]

    return data.encrypted_text


def decrypt_message(message_string_object: BinaryString, d=key.d, n=key.n):
    data.decrypted_text = [pow(char, d, n) for char in data.encrypted_text]
    return (data.decrypted_text)
