import os
from scrapers.framestore import FramestoreScraper
from scrapers.dneg import DnegScraper
from notifier import send_telegram

KEYWORDS = [
    "producer",
    "production manager",
    "line producer",
    "vfx producer",
]


def is_relevant(title: str) -> bool:
    t = title.lower()
    return any(k in t for k in KEYWORDS)


def format_digest(jobs):
    lines = ["🎬 Daily VFX Production Job Update\n"]
    for job in jobs:
        lines.append(f"• {job['studio']} — {job['title']}")
        lines.append(job["url"])
        lines.append("")
    return "\n".join(lines)


def main():
    scrapers = [FramestoreScraper(), DnegScraper()]
    matches = []

    for scraper in scrapers:
        jobs = scraper.fetch_jobs_sync()
        for job in jobs:
            if is_relevant(job["title"]):
                matches.append(job)

    if matches:
        send_telegram(format_digest(matches))
    else:
        send_telegram("No new VFX production jobs found today.")


if __name__ == "__main__":
    main()
