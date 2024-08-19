my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
starting_position = 0
while starting_position < len(my_list):
    if my_list[starting_position] < 0:
        break
    if my_list[starting_position] > 0:
        print(my_list[starting_position])
        starting_position = starting_position + 1
    else:
        break


