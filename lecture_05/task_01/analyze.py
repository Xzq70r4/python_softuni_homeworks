from lecture_05.task_01.modulus.amouts_by_category_analyzer import AmountsByCategoryAnalyzer
from lecture_05.task_01.modulus.amouts_by_city_analyzer import AmountsByCityAnalyzer
from lecture_05.task_01.modulus.catalog import load_catalog
from lecture_05.task_01.modulus.sales import load_sales
from lecture_05.task_01.modulus.totals_analyzer import TotalsAnalyzer

from lecture_05.task_01.constants import CATALOG_FILE_PATH, SALES_FILE_PATH
from lecture_05.task_01.modulus.amouts_by_hour_analyzer import AmountsByHourAnalyzer


def main():
    catalog = load_catalog(file_path=CATALOG_FILE_PATH)
    analyzers = [
        TotalsAnalyzer(),
        AmountsByCategoryAnalyzer(catalog=catalog),
        AmountsByCityAnalyzer(),
        AmountsByHourAnalyzer()
    ]

    load_sales_generator_object = load_sales(file_path=SALES_FILE_PATH)

    for sale in load_sales_generator_object:
        for analyzer in analyzers:
            analyzer.analyze_sale(sale)

    for analyzer in analyzers:
        analyzer.print_results()

if __name__ == '__main__':
    main()