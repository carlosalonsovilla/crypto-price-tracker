import requests

def get_crypto_price(crypto):
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        'ids': crypto,
        'vs_currencies': 'usd'
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data[crypto]['usd']
    else:
        return None
    
while True:
    crypto = input("Enter the name of the cryptocurrency you would like to track(e.g., bitcoin, ethereum): ").lower()
    price = get_crypto_price(crypto)
    if price:
        print(f"The current prince for {crypto.capitalize()} is currently ${price}.")
    else:
        print(f"Failed to get the price for {crypto.capitalize()}.")
    
    another = input("Would you like to get the price for another cryptocurrenty? (y/n)")
    if another == 'n':
        print('Goodbye')
        break




