import sqlite3

from lecture_08.task_01.modulus.catalog import load_catalog
from lecture_08.task_01.modulus.sales import load_sales
from lecture_08.task_01.constants import CATALOG_FILE_PATH, SALES_FILE_PATH, DB_FILENAME
from lecture_08.task_01.constants import KEY_TS, KEY_PRICE, KEY_CITY, KEY_COUNTRY, KEY_ITEM_ID


def main():

    with sqlite3.connect(DB_FILENAME, isolation_level=None) as connection:
        print("Connection opened")
        create_tables(connection)
        print("Tables created")
        import_catalog_into_db(connection, CATALOG_FILE_PATH)
        print("Catalog imported")
        import_sales_into_db(connection, SALES_FILE_PATH)
        print("Sales imported")
        print("DB file is in assets folder")


def create_tables(connection):
    cursor = connection.cursor()
    cursor.execute("""
        create table if not exists sale (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_key varchar(200) NOT NULL,
            country varchar(3),
            city_name varchar(60),
            sale_timestamp TEXT,
            price NUMERIC
        );
    """)

    cursor.execute("""
        create table if not exists catalog (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_key varchar(200),
            category varchar(200)
        );
    """)


def import_catalog_into_db(connection, catalog_file_path):
    catalog = load_catalog(catalog_file_path)
    # key - item_id value: category name

    cursor = connection.cursor()
    for item_id, category_name in catalog.items():
        cursor.execute(
            'insert into catalog (item_key, category) values (?, ?)',
            [item_id, category_name]
        )


def import_sales_into_db(connection, sales_file_path):
    sales = load_sales(file_path=sales_file_path)
    """[
            {
                "item_id": "561712",
                "country": "ES",
                "city": "Murcia",
                "ts": datetime(2015, 12, 11, 17, 14, 05, tz=+01: 00),
                "price": 43.21
            },
            {
             ...
            }
       ]
    """

    cursor = connection.cursor()
    for sale in sales:
        sale_timestamp = sale[KEY_TS]

        cursor.execute(
            'insert into sale (item_key, country , city_name , sale_timestamp , price) values (?, ?, ?, ?, ?)',
            [sale[KEY_ITEM_ID], sale[KEY_COUNTRY], sale[KEY_CITY], sale_timestamp.isoformat(), sale[KEY_PRICE]]
        )

if __name__ == '__main__':
    main()
