from datetime import datetime

FILE_PATH = './../assets/sales.csv'


def extract_data_to_dict(file_path: str) -> tuple:
    """

    :param file_path: Path to csv file.
    :return: Tuple of dicts. First value of tuple sales for day and sum of sales for day, second day hour and sum of
     prices.
    """
    global dict_sales_by_day, dict_sales_by_hour
    dict_sales_by_day = {}
    dict_sales_by_hour = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            split_line = line.split(',')
            sale_date = datetime.strptime(split_line[0], "%Y-%m-%d %H:%M:%S")
            sale_weekday = sale_date.strftime("%A")
            sale_hour = sale_date.strftime("%-H")
            price_of_sale = float(split_line[1])

            dict_sales_by_day[sale_weekday] = dict_sales_by_day.get(sale_weekday, 0) + price_of_sale
            dict_sales_by_hour[sale_hour] = dict_sales_by_hour.get(sale_hour, 0) + price_of_sale

        return dict_sales_by_day, dict_sales_by_hour


def print_best_sale_day_information(dict_of_sales: dict):
    """

    :param dict_of_sales: Collection - dict of sales
    """

    dict_sorted = sorted(dict_of_sales.items(), key=lambda x: x[1], reverse=True)
    for sale_weekday, sum_prices in dict_sorted:
        print('{} were sales for {:.2f}BGN.'.format(sale_weekday,  sum_prices))

    best_sale_day, _ = dict_sorted[0]
    print()
    print('The day with most sales is {}.'.format(best_sale_day))


def print_best_sale_hour_information(dict_of_sales: dict):
    """

    :param dict_of_sales: Collection - dict of sales
    """

    dict_sorted = sorted(dict_of_sales.items(), key=lambda x: x[1], reverse=True)
    for sale_hour, sum_prices in dict_sorted:
        int_sale_hour, int_next_hour  = find_next_hour(sale_hour)

        print('Between {} and {} were sales for {:.2f}BGN.'.format(int_sale_hour, int_next_hour,  sum_prices))

    best_sale_hour, _ = dict_sorted[0]
    int_best_sale_hour, int_next_hour = find_next_hour(best_sale_hour)
    print()
    print('Between {} and {} were more sale.'.format(int_best_sale_hour, int_next_hour))


def find_next_hour(sale_hour: str) -> tuple:

    """
    :param: sale_hour: Hour to find next hour
    :rtype: Return tuple with two value. First value is input hour, second is next our.
    """
    int_sale_hour = int(sale_hour)
    if int_sale_hour == 0:
        int_next_hour = 1
    elif int_sale_hour == 24:
        int_next_hour = 0
    else:
        int_next_hour = int_sale_hour + 1

    return int_sale_hour, int_next_hour


print('='*50)
print('='*50)
dict_sales_by_day, dict_sales_by_hour = extract_data_to_dict(FILE_PATH)
print_best_sale_day_information(dict_sales_by_day)
print('='*50)
print('='*50)
print_best_sale_hour_information(dict_sales_by_hour)
print('='*50)
print('='*50)