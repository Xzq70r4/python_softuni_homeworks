# Input logic
print('Please, enter product prices. Must be minimum four.')
price_list = []
price_len = len(price_list)
minimum_price_count = 4
user_input = input('Enter a price: ')

while True:
    if (user_input == 'stop') and (len(price_list) > minimum_price_count - 1):
        break
    elif (user_input == 'stop') and not (len(price_list) > minimum_price_count):
        print('Please, enter more product prices. Minimum inputted must be four.')

    #  use replace('.', '', 1), because try catch is not taught
    if user_input.replace('.', '', 1).isdigit() and float(user_input) > 0:
        price_parse_to_float = float(user_input)
        price_list.append(price_parse_to_float)

    if len(price_list) > minimum_price_count -1:
        user_input = input('Enter a price (or \'stop\'): ')
    else:
        user_input = input('Enter a price: ')

# Find average price
price_set = set(price_list)  # remove duplicate values

price_set_to_list = list(price_set)
price_set_to_list.sort()
del price_set_to_list[0]  # remove smallest price
del price_set_to_list[-1]  # remove biggest price

price_average = sum(price_set_to_list)/len(price_set_to_list)
print('Average price: ', price_average)


