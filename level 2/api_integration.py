import requests

def fetch_crypto_prices():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin,ethereum,dogecoin",
        "vs_currencies": "usd,inr"
    }
    
    print("🔄 Fetching live crypto prices...")
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        print("\n💰 --- LIVE CRYPTO PRICES ---")
        for coin, prices in data.items():
            print(f"• {coin.capitalize()}:")
            print(f"   USD: ${prices['usd']:,}")
            print(f"   INR: ₹{prices['inr']:,}\n")
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Failed to fetch API data: {e}")
    except Exception as e:
        print(f"❌ Error parsing response: {e}")

if __name__ == "__main__":
    fetch_crypto_prices()