FILE_PATH = './../assets/catalog_sample.csv'  # or catalog_full.csv
price_sum = 0
price_count = 0

with open(FILE_PATH, encoding='utf-8') as f:
    for idx, line in enumerate(f, start=1):
        line = line.strip()
        current_line_list = line.split(',')
        current_price = current_line_list[-1]
        price_sum += float(current_price)  # for money must be use decimal - not learned yet
        price_count = idx

average_price = price_sum / price_count

print('Average price: ', average_price)
