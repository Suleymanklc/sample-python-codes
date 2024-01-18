from coffee_data import data
from coffee_data import resources


class CoffeeMaker:
    def turn_on_off(self, user_input):
        if user_input:
            print("Machine is running")
            return True
        else:
            print("Machine is powering down")
            return False

    def calculate_coin(self, quarters, dimes, nickles, pennies):
        coins = {
            'quarters_v': float(0.25),
            'dimes_v': float(0.10),
            'nickles_v': float(0.05),
            'pennies_v': float(0.01),
        }

        return float(round(quarters * coins.get('quarters_v') + dimes * coins.get('dimes_v') + nickles * coins.get(
            'nickles_v') + pennies * coins.get('pennies_v'), 2))

    def print_resources(self, coffee, water, milk):
        print("Remained resources:")
        resources['water'] = resources.get('water') - water
        resources['milk'] = resources.get('milk') - milk
        resources['coffee'] = resources.get('coffee') - coffee
        print("{}= {}".format('water', resources.get('water')))
        print("{}= {}".format('milk', resources.get('milk')))
        print("{}= {}".format('coffee', resources.get('coffee')))

    def calculate_change(self, order, amount):
        change = 0.00
        balance = "Insufficient funds!"
        if amount >= round(float(data.get(order).get('cost'))):

            print("your coffee is being prepared... ")
            if float(amount - round(float(data.get(order).get('cost')))) > 0:
                tip = float(input('Do you want to tip, if yes enter quantity(ex: 0.15): '))
                if 0 < tip <= float(amount - round(float(data.get(order).get('cost')))):
                    change = amount - round(float(data.get(order).get('cost')), 2) - round(float(tip), 2)
                else:
                    change = amount - round(float(data.get(order).get('cost')), 2)
            return round(change, 2)
        else:
            return balance

    def take_order(self):
        user_input = self.turn_on_off(True)
        print("###########################")
        self.print_resources(0, 0, 0)
        order = str(input('Please make your choice between espresso/latte/cappuccino: '))
        quarters = int(input("please enter quarter count: "))
        dimes = int(input("please enter quarter count: "))
        nickles = int(input("please enter nickles count: "))
        pennies = int(input("please enter pennies count: "))
        ingredients = data.get(order).get('ingredients')
        coffee = ingredients.get('coffee')
        water = ingredients.get('water')
        milk = int(0)
        while user_input and coffee <= resources.get('coffee') and water <= resources.get('water'):

            print("your order:{}".format(order))
            if str(data.get(order)) != str("espresso"):
                milk = ingredients.get('milk')

                if str(data.get(order)) != str("espresso"):
                    if coffee <= resources.get('coffee') and milk <= resources.get('milk') and water <= resources.get('water'):
                        print("you entered= {}$".format(self.calculate_coin(quarters, dimes, nickles, pennies)))
                        print("Your Change: {}".format(self.calculate_change(order, self.calculate_coin(quarters, dimes, nickles, pennies))))
                        self.print_resources(coffee, water, milk)

                    else:
                        print("No enough resources!")
                        self.turn_on_off(False)

            else:
                if coffee <= resources.get('coffee') and water <= resources.get('water'):
                    print("you entered= {}$".format(self.calculate_coin(quarters, dimes, nickles, pennies)))
                    print(self.calculate_change(order, self.calculate_coin(quarters, dimes, nickles, pennies)))
                    self.print_resources(coffee, water, milk)
                else:
                    print("No enough resources!")
                    self.turn_on_off(False)


coffeeMaker = CoffeeMaker()
coffeeMaker.take_order()
