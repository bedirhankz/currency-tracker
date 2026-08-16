import requests
key="ecc0e9bd93aad724a97eefaa"
apiurl=f"https://v6.exchangerate-api.com/v6/{key}/latest/"
try:
    exchange=input("Enter the currency code you want to convert from: ").upper()
    exchange_to=input("Enter the currency code you want to convert to: ").upper()
    amount=float(input("Enter the amount you want to convert: "))
    response = requests.get(apiurl+exchange)
    data = response.json()
    if data['result'] == 'success' and exchange_to in data.get('conversion_rates', {}):
        print(f"Exchange rate from {exchange} to {exchange_to}: {data['conversion_rates'][exchange_to]}")
        result = amount * data['conversion_rates'][exchange_to]
        print(f"{amount} {exchange} is equal to {result} {exchange_to}")
    else:
        print("Error: Unable to fetch exchange rates.")
except ValueError:
    print("Invalid input. Please enter a valid number for the amount.")
except Exception:
    print("An error occurred while fetching exchange rates. Please check your internet connection and try again.")
