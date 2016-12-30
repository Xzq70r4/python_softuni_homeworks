first_input = input("Input first text: ")
second_input = input("Input phrase to find: ")
index_of_second_input_in_first_input = first_input.find(second_input)

if index_of_second_input_in_first_input == -1:
    print("Not found!!!")
else:
    new_index_position = index_of_second_input_in_first_input + len(second_input)
    print("Result: " + first_input[new_index_position:])