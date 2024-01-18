line1 = ["#", "#", "#", "#"]
line2 = ["#", "#", "#", "#"]
line3 = ["#", "#", "#", "#"]
line4 = ["#", "#", "#", "#"]
line_map = [line1, line2, line3, line4]
letter_list = ["a", "b", "c", "d"]
location = input("please input location like 'B3':")
input_letter = location[0].lower()
print(input_letter)
letter_index = letter_list.index(input_letter)
print(letter_index)
number_index = int(location[1]) - 1
print(number_index)
line_map[int(number_index)][int(letter_index)] = "X"
print(f"{line1}\n{line2}\n{line3}\n{line4}")
