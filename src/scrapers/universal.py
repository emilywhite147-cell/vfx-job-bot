import requests
from bs4 import BeautifulSoup

HEADERS = {"User-Agent": "Mozilla/5.0"}

ROLE_KEYWORDS = [
    "vfx producer",
    "production manager",
    "line producer",
    "vfx production"
]

LOCATION_KEYWORDS = [
    "london",
    "uk",
    "united kingdom"
]


def scrape_company(base_url, careers_path="/careers"):
    try:
        res = requests.get(base_url + careers_path, headers=HEADERS, timeout=20)
        soup = BeautifulSoup(res.text, "html.parser")
    except:
        return []

    links = set()

    for a in soup.find_all("a", href=True):
        href = a["href"]

        if any(x in href.lower() for x in ["job", "career", "position"]):
            full = href if href.startswith("http") else base_url + href
            links.add(full)

    results = []

    for url in links:
        try:
            r = requests.get(url, headers=HEADERS, timeout=20)
            text = r.text.lower()

            if any(rk in text for rk in ROLE_KEYWORDS) and any(lk in text for lk in LOCATION_KEYWORDS):
                soup = BeautifulSoup(r.text, "html.parser")
                title = soup.title.text if soup.title else base_url

                results.append({
                    "title": title,
                    "url": url
                })

        except:
            continue

    return results
