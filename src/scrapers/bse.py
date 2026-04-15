import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def get_soup(url: str):
    res = requests.get(url, headers=HEADERS, timeout=20)
    res.raise_for_status()
    return BeautifulSoup(res.text, "html.parser")
