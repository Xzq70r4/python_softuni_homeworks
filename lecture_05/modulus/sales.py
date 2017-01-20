import csv
import iso8601
from lecture_05.task_01.constants\
    import KEY_ITEM_ID, KEY_COUNTRY, KEY_CITY, KEY_PRICE, KEY_TS
from lecture_05.task_01.constants\
    import SALE_COLUMN_ITEM_ID, SALE_COLUMN_COUNTRY, SALE_COLUMN_CITY, SALE_COLUMN_PRICE, SALE_COLUMN_TS



def load_sales(file_path: str) -> dict:
    """
    Expected columns in catalog file:
     1. Id number
     2. Country was carried sale (ISO code)
     3. Town was carried sale
     4. Date/hour on sale with timezone (ISO8601)
     5. Sale price (the price of the same item in different countries are different)

    :param file_path: File path
    :return Return dict
        {
            "item_id": "561712",
            "country": "ES",
            "city": "Murcia",
            "ts": datetime(2015, 12, 11, 17, 14, 05, tz=+01:00),
            "price": 43.21
        }
    """

    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            sale = dict()
            sale[KEY_ITEM_ID] = row[SALE_COLUMN_ITEM_ID]
            sale[KEY_COUNTRY] = row[SALE_COLUMN_COUNTRY]
            sale[KEY_CITY] = row[SALE_COLUMN_CITY]
            sale[KEY_TS] = iso8601.parse_date(row[SALE_COLUMN_TS])
            sale[KEY_PRICE] = float(row[SALE_COLUMN_PRICE])
            yield sale
