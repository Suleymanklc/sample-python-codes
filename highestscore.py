def highest_score():
    mylist = input("please enter scores with tab: ").split(" ")
    print(mylist)
    high_score = 0
    for score in mylist:
        if int(score) > int(high_score):
            high_score = score
    print(f"highest score: {high_score}")


highest_score()
