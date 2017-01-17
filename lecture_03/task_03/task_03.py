FILE_PATH = './../assets/catalog_sample.csv'  # or catalog_full.csv
UPDATED_FILE_PATH = './../assets/updated_price_catalog_sample.csv'
PERCENT = 0.75  # 75%

with open(FILE_PATH, encoding='utf-8') as f:
    with open(UPDATED_FILE_PATH, 'w', encoding='utf-8') as f_updated:
        for line in f:
            line = line.strip()
            current_line_list = line.split(',')
            updated_price = float(current_line_list[-1]) + float(current_line_list[-1]) * PERCENT
            current_line_list[-1] = updated_price
            updated_line = ','.join(str(e) for e in current_line_list)
            f_updated.write(updated_line + '\n')
