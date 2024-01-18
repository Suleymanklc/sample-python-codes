import random


def word_chose():
    words = ["python", "hangman", "programming", "challenge", "developer", "computer"]
    chosen_word = random.choice(words)
    return chosen_word


def display_word(guessed_letter, word_list):
    new_list = []
    for i in word_list:
        new_list.append('_')
    for num in range(0, len(word_list)):
        if str(word_list[num]) == str(guessed_letter):
            new_list[num] = guessed_letter
    return new_list


def guess_checker(guessed_letter, mylist):
    if guessed_letter in mylist:
        return True
    else:
        return False


def points_calculator(mylist):
    points = 0
    for num in range(0, len(mylist)):
        if str(mylist[num]) == str("_"):
            points += 100
    return points


def hangman():
    exit_game = False
    fail_attempts = 3
    word = str(word_chose())
    word_list = list(word)
    print(word_list)
    total_attempts = int(len(word_list)) - 1
    attempted_list = []
    for i in word_list:
        attempted_list.append('_')

    while fail_attempts > 0 and total_attempts > 0 and exit_game == False:
        guessed_letter = input("please guess a letter: ")

        if not guess_checker(guessed_letter, word_list):
            fail_attempts -= 1
            print(f'Wrong Guess! {fail_attempts} fail attempts left')
            if fail_attempts == 0:
                exit_game = True
        else:
            for num in range(0, len((display_word(guessed_letter, word_list)))):
                if str(display_word(guessed_letter, word_list)[num]) == str(guessed_letter):
                    attempted_list[num] = guessed_letter

            print(attempted_list)
            print("Congrats!")
            want_guess = ""
            if total_attempts < int(len(word_list)) - 1:
                want_guess = input("Do you want to guess th word? Y/N ?")
            if str(want_guess).lower() == str("y"):
                guess_word = input("Okay! Enter the word: ")
                if str(guess_word) == str(word):
                    print("Wow! You guessed!")
                    print(f'You got {points_calculator(attempted_list)} points')
                    new_try = input("Do you want one more time? Y/N:")
                    if str(new_try).lower() == str('n'):
                        exit_game = True
                    else:
                        fail_attempts = 3
                        word = str(word_chose())
                        word_list = list(word)
                        print(word_list)
                        total_attempts = int(len(word_list)) - 1
                        attempted_list = []

        total_attempts -= 1


hangman()
