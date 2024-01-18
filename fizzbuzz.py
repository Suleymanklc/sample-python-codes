for num in range(1, 100):
    if int(num) % 3 == 0 and int(num) % 5 != 0:
        print("Fizz")
    elif int(num) % 5 == 0 and int(num) % 3 != 0:
        print("Buzz")

    elif int(num) % 5 == 0 and int(num) % 3 == 0:
        print("FizzBuzz")

    else:
        print(str(num))
