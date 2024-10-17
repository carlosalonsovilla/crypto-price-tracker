import requests

def get_btc():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        'ids': 'bitcoin',
        'vs_currencies': 'usd'
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data['bitcoin']['usd']
    else:
        return None
    
if __name__ == '__main__':
    price = get_btc()
    if price:
        print(f"The current price of Bitcoin is: ${price} USD.")
    else:
        print("Failed to fetch the data.")

