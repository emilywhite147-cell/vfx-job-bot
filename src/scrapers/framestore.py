import requests
from bs4 import BeautifulSoup

BASE = "https://www.framestore.com"

HEADERS = {"User-Agent": "Mozilla/5.0"}

def fetch_framestore_jobs():
    try:
        res = requests.get(BASE + "/careers", headers=HEADERS, timeout=20)
        soup = BeautifulSoup(res.text, "html.parser")
    except:
        return []

    # STEP 1: collect candidate links
    links = set()

    for a in soup.find_all("a", href=True):
        href = a["href"]

        if any(x in href.lower() for x in ["job", "career", "position"]):
            full = href if href.startswith("http") else BASE + href
            links.add(full)

    results = []

    # STEP 2: deep scan each job page
    for url in links:
        try:
            r = requests.get(url, headers=HEADERS, timeout=20)
            text = r.text.lower()

            # ROLE MATCH (flexible wording)
            role_match = any(rk in text for rk in [
                "vfx producer",
                "production manager",
                "line producer",
                "vfx production"
            ])

            # LOCATION MATCH (loose, realistic)
            location_match = any(loc in text for loc in [
                "london",
                "uk",
                "united kingdom",
                "london, uk"
            ])

            if role_match and location_match:
                page = BeautifulSoup(r.text, "html.parser")
                title = page.title.text.strip() if page.title else "Framestore Job"

                results.append({
                    "title": title,
                    "url": url
                })

        except:
            continue

    return results
