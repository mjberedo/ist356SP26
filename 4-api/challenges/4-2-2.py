## Challenge 4-2-2

#Come up with a caching strategy for the Azure sentiment API. Use the `requests_cache.py` module. You will need to decided on the cache key.

#For the following input:

#for each text in the list:  
#output the text, the sentiment, and if the results came from the API or cache.

#```
#texts = [
#    "I love IST356. It is the best course I've ever taken.", 
#    "I hate the New York Giants.",
#    "I love IST356. It is the best course I've ever taken.", 
#    "I don't like the New York Giants."
#]
#```


import requests
import requests_cache as rq

# --- Config ---
API_KEY     = "c53fc19d90f8ab0541886d4f"
API_URL     = "https://cent.ischool-iot.net/api/azure/sentiment"
PICKLE_FILE = "sentiment.pkl"

# --- Input ---
texts = [
    "I love IST356. It is the best course I've ever taken.",
    "I hate the New York Giants.",
    "I love IST356. It is the best course I've ever taken.",   # duplicate → cache hit
    "I don't like the New York Giants."
]

# --- Clear/create cache file at the start ---
cache = rq.clear_cache(PICKLE_FILE)

# --- Process each text ---
for text in texts:
    cache_key = text.strip().lower()   # normalize so casing/whitespace doesn't cause misses

    if cache_key in cache:
        sentiment = cache[cache_key]
        source    = "cache"
    else:
        response = requests.post(
            API_URL,
            headers={"x-api-key": API_KEY, "Content-Type": "application/json"},
            json={"text": text}
        )
        response.raise_for_status()
        sentiment = response.json()          # store the full response dict
        cache[cache_key] = sentiment         # write to in-memory cache
        rq.save_cache(cache, PICKLE_FILE)       # persist immediately
        source = "API"

    print(f"Text      : {text}")
    print(f"Sentiment : {sentiment}")
    print(f"Source    : {source}")
    print("-" * 60)


