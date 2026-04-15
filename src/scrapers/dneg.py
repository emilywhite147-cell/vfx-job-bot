from .base import get_soup

BASE_URL = "https://www.dneg.com"

def fetch_dneg_jobs():
    soup = get_soup(f"{BASE_URL}/careers/")

    jobs = []

    # DNEG usually uses meaningful links under /careers or /jobs
    for a in soup.select("a[href]"):
        title = a.get_text(strip=True)
        href = a["href"]

        # 🔥 FILTER 1: must look like a job
        if not title:
            continue

        if len(title) < 5:
            continue

        # 🔥 FILTER 2: ignore navigation junk
        bad_keywords = [
            "about", "news", "contact", "privacy",
            "cookie", "login", "register", "view all"
        ]

        if any(b in title.lower() for b in bad_keywords):
            continue

        # 🔥 FILTER 3: keep likely job links
        if "career" in href or "job" in href or "position" in href:
            jobs.append({
                "title": title,
                "url": BASE_URL + href if href.startswith("/") else href
            })

    return jobs
