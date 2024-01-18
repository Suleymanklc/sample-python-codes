import random
list1 = input("please enter names with comma:")
name_list = list1.split(',')
length = len(name_list)
random_number = random.randint(0, length - 1)
random_choice = name_list[random_number]
print(f"randomly chosen person to pay the bill: {random_choice}")


