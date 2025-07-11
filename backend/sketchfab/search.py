import requests
import os

SKETCHFAB_API_TOKEN = os.getenv("c9c2df768ab74838a0481c2e6ab9f721")

def search_sketchfab(query):
    print(f"🔍 Searching Sketchfab for: {query}")
    
    url = f"https://api.sketchfab.com/v3/search?type=models&q={query}&downloadable=true"
    headers = {"Authorization": f"Token {SKETCHFAB_API_TOKEN}"}

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("❌ Sketchfab API error:", response.status_code)
        return None

    results = response.json().get("results", [])
    if not results:
        print("⚠️ No downloadable models found.")
        return None

    return results[0]["uri"]  # returns something like /v3/models/XXXXXXX
