import requests
from datetime import datetime

URL_API = 'http://api.fixer.io/'


def main():
    input_date = input('Input date: ')
    input_date = input_date.strip()
    validate_input_date(input_date)
    input_currency = input('Input currency: ')
    input_currency = input_currency.upper()
    input_amount = input('Input amount: ')
    input_currency_to_convert = input('Input currency to convert: ')

    if input_amount.isdigit() and float(input_amount) > 0:
        url = URL_API + input_date
        rates = get_exchange_rate(base_currency=input_currency,
                                  api_url=url)

        equivalence_value = calculate_rate_in_base_currency(rates=rates, currency=input_currency_to_convert,
                                                            amount_in_currency=input_amount)

        print_converted_value(converted_value=equivalence_value, base_currency=input_currency_to_convert)
    else:
        print("Input amount must be positive number > 0")


def validate_input_date(input_date: str):
    try:
        datetime.strptime(input_date, "%Y-%m-%d").date()
    except Exception as e:
        datetime_now = datetime.now()
        print("Incorrect date!!! Correct date example: {}-{:02d}-{:02d}".format(datetime_now.year,
                                                                                datetime_now.month, datetime_now.day))
        print('Error: ', str(e))


def get_exchange_rate(base_currency: str, api_url: str):

    try:
        response = requests.get(api_url, timeout=20,
                                params={'base': base_currency}
                                )

        if response.status_code == 200:
            exchange_rates = response.json()
            rates = exchange_rates.get('rates', {})

            return rates
        else:
            print("Error from server: ", response.status_code)
            return None

    except Exception as e:
        print("Error from server! ", str(e))


def calculate_rate_in_base_currency(rates: dict,
                                    currency: str,
                                    amount_in_currency: str):

    exchange_rate = rates.get(currency, None)
    if exchange_rate is not None:
        return float(amount_in_currency) * float(exchange_rate)
    else:
        return None


def print_converted_value(converted_value: float, base_currency):

    if converted_value is None:
        print("Can`t converts currency , because no have data for rates!!!")
    else:
        print('Equivalence in {}: {:.2f}'.format(base_currency, converted_value))


if __name__ == '__main__':
    main()
