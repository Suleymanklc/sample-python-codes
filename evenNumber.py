def even_number():
    num = input("please enter a number between 1-100: ")
    sum = 0
    for i in range(1, int(num)):
        if int(i) % 2 == 0:
            sum = int(sum) + int(i)
    print(f"total of even numbers: {sum}")


even_number()
