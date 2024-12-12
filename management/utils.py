# David Alvarado
# CIS 218 
# 12/11/2024

import requests
from django.core.cache import cache

COIN_ID_MAP = {
    "bitcoin": "bitcoin",
    "ethereum": "ethereum",
    "tether": "tether",
    "binancecoin": "binancecoin",
    "xrp": "ripple",
    "cardano": "cardano",
    "dogecoin": "dogecoin",
    "solana": "solana",
    "tron": "tron",
    "polkadot": "polkadot",
    "polygon": "matic-network",
    "litecoin": "litecoin",
    "shiba": "shiba-inu",
    "dai": "dai",
    "avalanche": "avalanche-2",
    "wrappedbitcoin": "wrapped-bitcoin",
    "uniswap": "uniswap",
    "chainlink": "chainlink",
    "leo": "leo-token",
    "stellar": "stellar",
}

def fetch_batch_crypto_prices():
    """
    Fetch real time prices for all cryptocurrencies in COIN_ID_MAP in a single API call.
    Results are cached for 1 minute to reduce requests.
    returns: A dictionary of coin prices {coin_name: price_in_usd}
    """
    cache_key = "crypto_prices"
    cached_data = cache.get(cache_key)
    if cached_data:
        return cached_data

    coin_ids = ",".join(COIN_ID_MAP.values())  # Create a separated list of coin IDs
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {"ids": coin_ids, "vs_currencies": "usd"}
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            # Reverse map the data back to the coin names
            prices = {name: data.get(api_id, {}).get("usd", None) for name, api_id in COIN_ID_MAP.items()}
            cache.set(cache_key, prices, timeout=60)  # Cache the results for 1 minute
            return prices
    except requests.RequestException as e:
        print(f"Error fetching batch crypto prices: {e}")
    return {}