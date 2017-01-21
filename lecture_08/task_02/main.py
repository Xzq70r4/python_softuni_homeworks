import sqlite3

DB_FILE_PATH = './assets/sales-database.db'


def main():
    input_city = input("Please, input name of city: ")
    city_data = select_city_data(input_city)
    print_data(city_data)


def select_city_data(input_city):
    result = []
    with sqlite3.connect(DB_FILE_PATH, isolation_level=None) as db_connection:
        cursor = db_connection.cursor()
        sales = cursor.execute("SELECT item_key, sale_timestamp, price FROM sale WHERE city_name = ?",
                               [input_city])

    for sale in sales:
        result.append(sale)

    return result


def print_data(cities_data: list):
    if len(cities_data) == 0:
        print("No have information for this city!")
    else:
        for city in cities_data:
            print('Product #{} date/hour: {} price: {}'.format(
                city[0], city[1], city[2]
            ))


if __name__ == '__main__':
    main()
