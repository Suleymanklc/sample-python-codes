import random
import string

# Create a list of letters from 'a' to 'z'
lower_letter_list = [chr(ord('a') + i) for i in range(26)]
upper_letter_list = [chr(ord('A') + i) for i in range(26)]
number_list = [int(i) for i in range(0, 9)]
special_characters = [char for char in string.printable if not char.isalnum() and char not in string.whitespace]


def password_generator(num_count, lower_letter_count, upper_letter_count, special_char_count):
    final_password = ''
    password = []
    print("Welcome to the password generator!")

    for num in range(1, num_count + 1):
        password.append(random.choice(number_list))
    for lower_letter in range(1, lower_letter_count + 1):
        password.append(random.choice(lower_letter_list))
    for upper_letter in range(1, upper_letter_count + 1):
        password.append(random.choice(upper_letter_list))
    for special_char in range(1, special_char_count + 1):
        password.append(random.choice(special_characters))

    for item in password:
        final_password += str(item)

    #print(f"your final password: {final_password}")
    return final_password


