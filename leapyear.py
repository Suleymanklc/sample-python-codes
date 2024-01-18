def leap_year_calculator():
    year = int(input("please enter year"))
    if year % 4 == 0:
        if year % 100 != 0:
            if year % 400 == 0:
                return True


def print_leap_year():
    if leap_year_calculator():
        print("leap year!")
    else:
        print("not leap year!")


print_leap_year()
