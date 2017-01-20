from lecture_05.moduls.catalog import load_catalog
from lecture_05.moduls.sales import load_sales
import lecture_05.moduls.print_sales as print_sales

CATALOG_FILE_PATH = './../assets/catalog.csv'
SALES_FILE_PATH = './../assets/sales-10K.csv'
LEN_OF_TOP_TO_SHOW = 5


def main():
    catalog = load_catalog(file_path=CATALOG_FILE_PATH)
    sales = load_sales(file_path=SALES_FILE_PATH)

    print_sales.total_stats(sales=sales)
    print_sales.top_by_category(sales=sales, catalog=catalog, list_len=LEN_OF_TOP_TO_SHOW)
    print_sales.top_by_city(sales=sales, list_len=LEN_OF_TOP_TO_SHOW)
    print_sales.top_by_hour(sales=sales, list_len=LEN_OF_TOP_TO_SHOW)


if __name__ == '__main__':
    main()