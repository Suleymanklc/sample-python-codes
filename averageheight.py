def collect_height():
    mylist = input("please enter heights with tab").split(" ")
    print(mylist)
    total_height = 0
    average_height = 0
    for height in mylist:
        total_height += int(height)
    average_height = int(total_height) / len(mylist)
    print(f"Average: {average_height}\nTotal: {total_height}\n People Count: {len(mylist)} ")


collect_height()
