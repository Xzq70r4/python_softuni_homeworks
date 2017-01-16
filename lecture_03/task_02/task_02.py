FILE_PATH = './../assets/catalog_sample.csv'  # or catalog_full.csv
men_price_sum = 0
women_price_sum = 0
kid_price_sum = 0
men_count = 0
women_count = 0
kid_count = 0

with open(FILE_PATH, encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        current_line_list = line.split(',')
        current_price = current_line_list[-1]
        current_gender_age_group = current_line_list[-2]

        if current_gender_age_group == 'Men' or current_gender_age_group == 'Unisex':
            men_price_sum += float(current_price)   # for money must be use decimal - not learned yet
            men_count += 1
        if current_gender_age_group == 'Women' or current_gender_age_group == 'Unisex':
            women_price_sum += float(current_price)
            women_count += 1
        if current_gender_age_group == 'Kid':
            kid_price_sum += float(current_price)
            kid_count += 1

men_average_price = men_price_sum / men_count
women_average_price = women_price_sum / women_count
kid_average_price = kid_price_sum / kid_count

print('Men average price: ', men_average_price)
print('Women average price: ', women_average_price)
print('Kid average price: ', kid_average_price)