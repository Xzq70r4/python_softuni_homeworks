from datetime import timezone

KEY_TS = 'ts'
KEY_PRICE = 'price'
KEY_ITEM_ID = 'item_id'
KEY_CITY = 'city'


def find_sales_by_total_stats(sales: list) -> tuple:
    """

    Print information of total stats for sales
    :param sales: list of dict with info for sales
    :rtype: tuple: (total_count: int, total_amount: float, average_price: float,
     min_timestamp: datetime, max_timestamp: datetime)
    """
    total_count = len(sales)
    total_amount = 0

    min_timestamp = None
    max_timestamp = None

    for sale in sales:  # see sales.load_sales() for details
        total_amount += sale[KEY_PRICE]
        ts = sale[KEY_TS]

        if min_timestamp is None or ts < min_timestamp:
            min_timestamp = ts
        if max_timestamp is None or ts > max_timestamp:
            max_timestamp = ts

    if total_count > 0:
        average_price = total_amount / total_count
    else:
        average_price = None

    return total_count, total_amount, average_price, min_timestamp, max_timestamp


def find_top_sales_by_category(sales: list, catalog: dict) -> list:
    """

    Print information of top categories by most sales
    :param sales: list of dict with info for sales
    :param catalog: dict of category id and category name
    :return: amounts_by_category_sorted: return list tuples with first value - Name of category, second value sum of
    prices for this category.
    """

    amounts_by_category = {}  # key : category name  ,  value : accumulated sum of sales

    for sale in sales:
        item_id = sale[KEY_ITEM_ID]
        price = sale[KEY_PRICE]
        category_name = catalog.get(item_id, None)
        if category_name not in amounts_by_category:
            amounts_by_category[category_name] = 0
        amounts_by_category[category_name] += price

    amounts_by_category_sorted = sorted(amounts_by_category.items(), key=lambda x: x[1], reverse=True)

    return amounts_by_category_sorted


def find_top_sales_by_city(sales: list) -> list:
    """

    Print information of top cities by most sales
    :param sales: list of dict with info for sales
    :return: amounts_by_city_sorted: return list tuples with first value - Name of city, second value sum of
    prices for this city.
    """

    amounts_by_city = {}  # key : city name  ,  value : accumulated sum of sales

    for sale in sales:
        city_name = sale[KEY_CITY]
        price = sale[KEY_PRICE]
        if city_name not in amounts_by_city:
            amounts_by_city[city_name] = 0
        amounts_by_city[city_name] += price

    amounts_by_city_sorted = sorted(amounts_by_city.items(), key=lambda x: x[1], reverse=True)

    return amounts_by_city_sorted


def find_top_sales_by_hour(sales: list) -> list:
    """

    Print information of top hours by most sales
    :param sales: list of dict with info for sales
    :return: amounts_by_hour_sorted: return list tuples with first value - hour(UTC) of sale, second value sum of
    prices for this hour.
    """

    amounts_by_hour = {}  # key : city name  ,  value : accumulated sum of sales

    for sale in sales:
        sale_timestamp = sale[KEY_TS]
        sale_timestamp_reset_minute = sale_timestamp.astimezone(timezone.utc).replace(minute=0, second=0, microsecond=0)
        price = sale[KEY_PRICE]
        if sale_timestamp_reset_minute not in amounts_by_hour:
            amounts_by_hour[sale_timestamp_reset_minute] = 0
        amounts_by_hour[sale_timestamp_reset_minute] += price

    amounts_by_hour_sorted = sorted(amounts_by_hour.items(), key=lambda x: x[1], reverse=True)

    return amounts_by_hour_sorted
