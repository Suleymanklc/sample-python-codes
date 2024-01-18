def size_calculator():
    size = str(input("Pizza size S/M/L?: "))
    pepperoni = str(input("Extra pepperoni Y/N?: "))
    cheese = str(input("Extra cheese Y/N?: "))
    price = 0
    if size == 'S':
        price = 15
    elif size == 'M':
        price = 20
    elif size == 'L':
        price = 25
    total_price = price + extra_cheese(cheese) + extra_pepperoni(size, pepperoni)
    print(f"total price: ${total_price}")


def extra_pepperoni(size, pepperoni):
    if pepperoni == 'Y':
        if size == 'S':
            extra_price = 2
            return extra_price
        else:
            extra_price = 3
            return extra_price
    else:
        return 0


def extra_cheese(cheese):
    if cheese == 'Y':
        extra_price = 1
        return extra_price
    else:
        return 0


size_calculator()
