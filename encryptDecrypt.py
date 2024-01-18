import random
import base64

import passwordGenerator


def encrypter():
    num_count = int(input("number count: "))
    lower_letter_count = int(input("lower letter count: "))
    upper_letter_count = int(input(" higher letter count: "))
    special_char_count = int(input("special character count: "))
    password = passwordGenerator.password_generator(num_count, lower_letter_count, upper_letter_count,
                                                    special_char_count)

    encoded_bytes = base64.b64encode(password.encode('utf-8'))
    print(f"Your encrypted password is: {encoded_bytes}")


def decrypter(password):
    encoded_bytes = base64.b64decode(password)
    return encoded_bytes


def main():
    print("Please type 'I' for invoke an password or type 'D' decrypt a password")
    answer = input("Please enter letter: ")
    if str(answer.upper()) == "I":
        encrypter()
    elif str(answer.upper()) == "D":
        password = input("Type your password")

        print(decrypter(password))


main()
