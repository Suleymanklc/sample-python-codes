import random


class GuessNumber:
    def check_number(self, number):
        random_number = random.randint(0, 100)
        if number == random_number:
            print("congratulation you guessed!")
        if number > random_number:
            print("too high number")
        else:
            print("too low number")

    def assign_difficulty(self):
        level = input("please enter a level easy/medium/hard:")
        max_attempts = 0
        if level.lower() == str("easy"):
            max_attempts = 10
        elif level.lower() == str("medium"):
            max_attempt = 5
        else:
            max_attempts = 3
        print(f"you can have {max_attempts} attempts regarding to your difficulty choice")
        return max_attempts

    def guess_number(self):
        max_attempts = self.assign_difficulty()
        for i in range(0, max_attempts):
            max_attempts -= 1
            print(f"remaining attempts: {max_attempts}")
            guessed_number = input("please enter a number between 0 and 100:")
            self.check_number(int(guessed_number))


guess_number = GuessNumber()
guess_number.guess_number()
