import requests

URL_API_LATEST = 'http://api.fixer.io/latest'
DEFAULT_CURRENCY_TO_CONVERT = 'BGN'
NO_DATA_VALUE = 'NO DATA'

try:
    input_currency = input('Input currency: ')
    input_currency = input_currency.upper()
    input_amount = input('Input amount: ')

    if input_amount.isdigit() and float(input_amount) > 0:
        response = requests.get('http://api.fixer.io/latest', timeout=20,
                                params={'symbols': '{},{}'.format(
                                    DEFAULT_CURRENCY_TO_CONVERT, input_currency
                                )})

        if response.status_code == 200:
            exchange_rates = response.json()
            rates = exchange_rates.get('rates', {})
            currency_rate = rates.get(input_currency, NO_DATA_VALUE)
            print("Current rates for {}/{}: ".format(DEFAULT_CURRENCY_TO_CONVERT, input_currency),
                  currency_rate)

            if currency_rate == NO_DATA_VALUE:
                print("Can`t converts currency , because no have data for rate !!!")
            else:
                converted_currency = float(input_amount)/float(currency_rate)
                print('Equivalence in {}: {:.2f}'.format(DEFAULT_CURRENCY_TO_CONVERT, converted_currency))
        else:
            print("Error from server: ", response.status_code)
    else:
        print("Input amount must be positive number > 0")

except Exception as e:
    print("Error from server! ", str(e))
