import requests
from bs4 import BeautifulSoup

BASE = "https://www.weacceptyou.com/"

def fetch_OneofUs_jobs():
    try:
        r = requests.get(BASE + "/careers/", headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(r.text, "html.parser")
    except:
        return []

    jobs = []

    for a in soup.find_all("a", href=True):
        title = a.get_text(strip=True)
        href = a["href"]

        if any(k in title.lower() for k in ["producer", "production manager", "line producer"]):
            jobs.append({
                "title": f"One of Us – {title}",
                "url": href if href.startswith("http") else BASE + href
            })

    return jobs
