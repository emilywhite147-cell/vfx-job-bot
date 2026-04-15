import requests
from bs4 import BeautifulSoup

def fetch_dneg_jobs():
    url = "https://www.dneg.com/careers/"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")

    jobs = []

    for a in soup.find_all("a"):
        title = a.get_text(strip=True)
        href = a.get("href")

        if title and len(title) > 3:
            jobs.append({
                "title": title,
                "url": href
            })

    return jobs
