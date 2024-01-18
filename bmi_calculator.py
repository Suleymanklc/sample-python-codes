def bmi_calculator():
    your_height = input("please enter your height:")
    your_weight = input("please enter your weight:")
    try:
     your_height = int(your_height)
     your_weight = int(your_weight)
     your_bmi = your_weight/your_height
     print("your bm1: "+str(your_bmi))
    except ValueError:
     print("That's not an number!")


bmi_calculator()
