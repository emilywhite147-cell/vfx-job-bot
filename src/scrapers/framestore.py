from .base import get_soup
from .filter import is_relevant_job

BASE_URL = "https://www.framestore.com"

def fetch_framestore_jobs():
    soup = get_soup(f"{BASE_URL}/careers")

    jobs = []

    for a in soup.select("a[href]"):
        title = a.get_text(strip=True)
        href = a["href"]

        if not title:
            continue

        full_text = title

        if is_relevant_job(title, full_text):
            jobs.append({
                "title": title,
                "url": href if href.startswith("http") else BASE_URL + href
            })

    return jobs
