full_name = input("Input Your Full Name: ")

splitted_names = full_name.split()
first_chars_of_splitted_names = [name[0] for name in splitted_names]
separator = "."
name_abbreviation = separator.join(first_chars_of_splitted_names)

print("Result: " + name_abbreviation)
