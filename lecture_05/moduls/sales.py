import csv
import iso8601

COLUMN_ITEM_ID = 0
COLUMN_COUNTRY = 1
COLUMN_CITY = 2
COLUMN_TS = 3
COLUMN_PRICE = 4

KEY_ITEM_ID = 'item_id'
KEY_COUNTRY = 'country'
KEY_CITY = 'city'
KEY_TS = 'ts'
KEY_PRICE = 'price'


def load_sales(file_path: str) -> list:
    """
    Expected columns in catalog file:
     1. Id number
     2. Country was carried sale (ISO code)
     3. Town was carried sale
     4. Date/hour on sale with timezone (ISO8601)
     5. Sale price (the price of the same item in different countries are different)

    :param file_path: File path
    :return result:
        [
            {
                "item_id": "561712",
                "country": "ES",
                "city": "Murcia",
                "ts": datetime(2015, 12, 11, 17, 14, 05, tz=+01:00),
                "price": 43.21
            },
            {
                ...
            }
            ..
        ]
    """

    result = []
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            sale = dict()
            sale[KEY_ITEM_ID] = row[COLUMN_ITEM_ID]
            sale[KEY_COUNTRY] = row[COLUMN_COUNTRY]
            sale[KEY_CITY] = row[COLUMN_CITY]
            sale[KEY_TS] = iso8601.parse_date(row[COLUMN_TS])
            sale[KEY_PRICE] = float(row[COLUMN_PRICE])
            result.append(sale)

    return result
