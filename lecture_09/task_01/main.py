import requests

URL_API_LATEST = 'http://api.fixer.io/latest'
DEFAULT_CURRENCY_TO_CONVERT = 'BGN'


def main():

    input_currency = input('Input currency: ')
    input_currency = input_currency.upper()
    input_amount = input('Input amount: ')

    if input_amount.isdigit() and float(input_amount) > 0:
        rates = get_exchange_rate(input_currency=input_currency, base_currency=DEFAULT_CURRENCY_TO_CONVERT,
                                  api_url=URL_API_LATEST)

        equivalence_value = calculate_rate_in_base_currency(rates=rates, currency=input_currency,
                                                            amount_in_currency=input_amount)

        print_converted_value(converted_value=equivalence_value, base_currency=DEFAULT_CURRENCY_TO_CONVERT)
    else:
        print("Input amount must be positive number > 0")


def get_exchange_rate(input_currency: str,
                      base_currency: str,
                      api_url: str=URL_API_LATEST):

    try:
        response = requests.get(api_url, timeout=20,
                                params={'symbols': '{},{}'.format(
                                    base_currency, input_currency
                                )})

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
                                    amount_in_currency: str) -> float:

    exchange_rate = rates.get(currency, None)
    if exchange_rate is not None:
        return float(amount_in_currency) / float(exchange_rate)
    else:
        return None


def print_converted_value(converted_value: float, base_currency=DEFAULT_CURRENCY_TO_CONVERT):

    if converted_value is None:
        print("Can`t converts currency , because no have data for rates!!!")
    else:
        print('Equivalence in {}: {:.2f}'.format(base_currency, converted_value))


if __name__ == '__main__':
    main()
