import requests
from bs4 import BeautifulSoup

BASE = "https://www.blue-bolt.com/"

def fetch_BlueBolt_jobs():
    try:
        r = requests.get(BASE + "/hiring", headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(r.text, "html.parser")
    except:
        return []

    jobs = []

    for a in soup.find_all("a", href=True):
        title = a.get_text(strip=True)
        href = a["href"]

        if any(k in title.lower() for k in ["producer", "production manager", "line producer"]):
            jobs.append({
                "title": f"BlueBolt – {title}",
                "url": href if href.startswith("http") else BASE + href
            })

    return jobs
