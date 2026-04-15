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

    message = "🎬 *VFX JOB ALERT*\n\n"

    for job in jobs[:10]:
        title = job.get("title", "No title")
        url = job.get("url", "")

        message += f"• {title}\n{url}\n\n"

    send_telegram_message(message)

if __name__ == "__main__":
    run()
