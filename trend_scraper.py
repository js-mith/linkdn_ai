import requests
from bs4 import BeautifulSoup

def get_trends(industry):
    try:
        query = industry.replace(" ", "+")
        url = f"https://news.google.com/search?q={query}"
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        headlines = [h.text for h in soup.find_all("a", class_="DY5T1d", limit=5)]
        return headlines if headlines else ["No trends found."]
    except:
        return ["Error fetching trends."]
