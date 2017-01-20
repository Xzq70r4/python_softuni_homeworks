import lecture_05.moduls.utils as utils


def total_stats(sales: list):
    """

    :param sales: list of dict with info for sales
    :return void
    """
    total_count, total_amount, average_price, min_timestamp, max_timestamp =\
        utils.find_sales_by_total_stats(sales=sales)

    print("""
    Обобщение
    ---------

        Общ брой продажби: {total_count}
        Общо сума продажби: {total_amount:.2f} €
        Средна цена на продажба: {average_price: .2f} €
        Начало на период на данните: {min_ts}
        Край на период на данните: {max_ts}
    """.format(
        total_count=total_count,
        total_amount=total_amount,
        average_price=average_price,
        min_ts=min_timestamp,
        max_ts=max_timestamp,
    ))


def top_by_category(sales: list, catalog: dict, list_len: int):
    """

    :param sales: list of dict with info for sales
    :param catalog: dict of category id and category name
    :param list_len: length of top category to show
    :return void
    """
    category_by_best_sale = utils.find_top_sales_by_category(sales=sales, catalog=catalog)

    print("""
    Сума на продажби по категории (top {})
    -----------------------------
    """.format(list_len))

    for category_name, total_amount, in category_by_best_sale[:list_len]:
        print("        {}: {:.2f} €".format(category_name, total_amount))


def top_by_city(sales: list, list_len: int):
    """

    :param sales: list of dict with info for sales
    :param list_len: length of top city to show
    :return void
    """

    cities_by_best_sale = utils.find_top_sales_by_city(sales=sales)
    print("""
    Сума на продажби по градове (top {})
    -----------------------------
    """.format(list_len))

    for city_name, total_amount, in cities_by_best_sale[:5]:
        print("        {}: {:.2f} €".format(city_name, total_amount))


def top_by_hour(sales: list, list_len: int):
    """

    :param sales: list of dict with info for sales
    :param list_len: length of top hour to show
    :return void
    """
    hours_by_best_sale = utils.find_top_sales_by_hour(sales)
    print("""
    Сума на продажби по час (top {})
    -----------------------------
    """.format(list_len))

    for sale_hour, total_amount, in hours_by_best_sale[:5]:
        print("        {}: {:.2f} €".format(sale_hour, total_amount))