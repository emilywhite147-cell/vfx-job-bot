from scrapers.dneg import fetch_dneg_jobs
from scrapers.framestore import fetch_framestore_jobs
from scrapers.cinesite import fetch_cinesite_jobs
from core.telegram import send_telegram_message

def run():
    jobs = []

    jobs += fetch_dneg_jobs()
    jobs += fetch_framestore_jobs()
    jobs += fetch_cinesite_jobs()

    if not jobs:
        send_telegram_message("No VFX production roles in London today.")
        return

    message = "🎬 VFX JOBS (London)\n\n"

    for job in jobs:
        message += f"• {job['title']}\n{job['url']}\n\n"

    send_telegram_message(message)

if __name__ == "__main__":
    run()
