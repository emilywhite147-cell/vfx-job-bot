import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.framestore.com"

def fetch_framestore_jobs():
    url = BASE_URL + "/careers"
    res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(res.text, "html.parser")

    jobs = []

    for a in soup.find_all("a"):
        title = a.get_text(strip=True)
        href = a.get("href")

        if not title or not href:
            continue

        text = title.lower()

        if any(x in text for x in [
            "vfx producer",
            "production manager",
            "line producer"
        ]) and any(loc in text for loc in ["london", "uk"]):

            jobs.append({
                "title": title,
                "url": href if href.startswith("http") else BASE_URL + href
            })

    return jobs
