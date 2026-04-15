from scrapers.dneg import fetch_dneg_jobs
from scrapers.framestore import fetch_framestore_jobs
from core.telegram import send_telegram_message

def run():
    jobs = []
    jobs += fetch_dneg_jobs()
    jobs += fetch_framestore_jobs()

    if not jobs:
        send_telegram_message("No VFX jobs found today.")
        return

    msg = "🎬 VFX Jobs Found:\n\n"

    for job in jobs[:10]:
        msg += f"{job['title']}\n{job['url']}\n\n"

    send_telegram_message(msg)

if __name__ == "__main__":
    run()
