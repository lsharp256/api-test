import requests

URL = 'https://v6.exchangerate-api.com/v6/1fc80820c72b0163bc9c7536/latest/USD'

def test_status_code():
    # Verify the HTTP status is 200
    response = requests.get(URL)
    assert response.status_code == 200

def test_total_currencies():
    # Count the total number of currencies returned within the response
    response = requests.get(URL)
    currencies = response.json()['conversion_rates']
    # Assumption is that currencies will stay the same
    assert len(currencies) == 162

def test_gbp_rate():
    # Verify the currency 'GBP' is show within the response
    response = requests.get(URL)
    gbp_to_dollar = response.json()['conversion_rates']['GBP']
    print(f'\nThe British Pound is trading at {gbp_to_dollar} to the US Dollar')
    assert 'GBP' in response.json()['conversion_rates']