first_input = input("Input first text: ")
second_input = input("Input phrase to find: ")

if first_input.find(second_input) == -1:
    print("Not found!!!")
else:
    second_input_index_in_first_input = first_input.find(second_input)
    new_index_position = second_input_index_in_first_input + len(second_input)
    first_input_length = len(first_input)

    print("Result: " + first_input[new_index_position:first_input_length])