import requests
from config import SERPER_API_KEY

def perform_web_search(query: str) -> dict:
    try:
        response = requests.post(
            "https://google.serper.dev/search",
            headers={"X-API-KEY": SERPER_API_KEY},
            json={"q": query}
        )
        return response.json()
    except Exception as e:
        print("❌ Erreur recherche Web :", str(e))
        return {}
