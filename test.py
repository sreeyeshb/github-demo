import requests

def get_usd_inr_rate():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)
    data = response.json()
    return data['rates']['INR']

# Example usage
if __name__ == "__main__":
    rate = get_usd_inr_rate()
    print(f"Current USD to INR rate: {rate}")