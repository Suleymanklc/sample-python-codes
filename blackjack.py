import random


class blackJack:

    def deal_card(self):
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        card = random.choice(cards)
        return card

    def compare_hand(self, usr_point, comp_point):
        if usr_point < comp_point < 21:
            print(f"user_score, computer_score: {usr_point}, {comp_point}")
            print("opponent wins!")
        elif comp_point < usr_point < 21:
            print("your wins!")
            print(f"user_score, computer_score: {usr_point}, {comp_point}")
        elif comp_point == 21 and usr_point != 21:
            print("opponent wins!")
            print(f"user_score, computer_score: {usr_point}, {comp_point}")
        elif usr_point != 21 and comp_point == 21:
            print("your wins!")
            print(f"user_score, computer_score: {usr_point}, {comp_point}")
        elif comp_point > 21 and usr_point < 21:
            print("your wins")
            print(f"user_score, computer_score: {usr_point}, {comp_point}")
        elif comp_point < 21 and usr_point > 21:
            print("your wins")
            print(f"user_score, computer_score: {usr_point}, {comp_point}")
        elif comp_point == usr_point:
            print("push, next game")
            print(f"user_score, computer_score: {usr_point}, {comp_point}")

    def calculate_score(self):
        user_cards = []
        computer_cards = []
        user_points = 0
        computer_points = 0
        deal_card_user = False
        deal_card_computer = False
        for count in range(2):
            user_cards.append(self.deal_card())
            computer_cards.append(self.deal_card())
        user_points = sum(user_cards)
        computer_points = sum(computer_cards)
        self.compare_hand(user_points, computer_points)
        while user_points < 17 and not deal_card_user:
            deal_card_user = input("Do you want new card? (y/n): ")
            if str(deal_card_user).lower() == "y":
                self.deal_card()
                user_cards.append(self.deal_card())
            user_points = sum(user_cards)
            deal_card_user = True
        while computer_points < 17 and not deal_card_computer:
            deal_card_computer = input("Do you want new card? (y/n): ")
            if str(deal_card_computer).lower() == "y":
                self.deal_card()
                computer_cards.append(self.deal_card())
            computer_points = sum(computer_cards)
            deal_card_computer = True
            self.compare_hand(user_points, computer_points)


blackjack = blackJack()
blackjack.calculate_score()
