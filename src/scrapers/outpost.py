import requests
from bs4 import BeautifulSoup

BASE = "https://www.outpost-vfx.com/en"

def fetch_dneg_jobs():
    try:
        r = requests.get(BASE + "/careers/", headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(r.text, "html.parser")
    except:
        return []

    jobs = []

    for a in soup.find_all("a", href=True):
        title = a.get_text(strip=True)
        href = a["href"]

        if not title:
            continue

        if any(k in title.lower() for k in ["producer", "production manager", "line producer"]):
            jobs.append({
                "title": f"outpost – {title}",
                "url": href if href.startswith("http") else BASE + href
            })

    return jobs
