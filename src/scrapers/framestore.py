from .base import get_soup

BASE_URL = "https://www.framestore.com"

def fetch_framestore_jobs():
    soup = get_soup(f"{BASE_URL}/careers")

    jobs = []

    for a in soup.select("a[href]"):
        title = a.get_text(strip=True)
        href = a["href"]

        if not title or len(title) < 5:
            continue

        bad_keywords = [
            "about", "news", "cookie", "privacy",
            "contact", "read more", "apply now"
        ]

        if any(b in title.lower() for b in bad_keywords):
            continue

        if "job" in href or "career" in href:
            jobs.append({
                "title": title,
                "url": href if href.startswith("http") else BASE_URL + href
            })

    return jobs
