import requests
from bs4 import BeautifulSoup

BASE = "https://www.dneg.com"

def fetch_dneg_jobs():
    res = requests.get(BASE + "/careers/", headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(res.text, "html.parser")

    links = []

    for a in soup.find_all("a", href=True):
        href = a["href"]

        if "career" in href or "job" in href:
            full = href if href.startswith("http") else BASE + href
            links.append(full)

    results = []

    for url in set(links):
        try:
            r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
            page = r.text.lower()

            if any(role in page for role in [
                "vfx producer",
                "production manager",
                "line producer"
            ]) and any(loc in page for loc in [
                "london",
                "uk",
                "united kingdom"
            ]):

                soup = BeautifulSoup(r.text, "html.parser")
                title = soup.title.text if soup.title else url

                results.append({
                    "title": title,
                    "url": url
                })

        except:
            continue

    return results
