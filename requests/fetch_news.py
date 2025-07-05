import network

def fetch_latest_news():
    url = "https://cryptopanic.com/api/v1/posts/?auth_token=demo&public=true"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("results", [])
    return []
