from scrapers.dneg import fetch_dneg_jobs
from scrapers.framestore import fetch_framestore_jobs
from scrapers.cinesite import fetch_cinesite_jobs
from scrapers.milk import fetch_milk_jobs
from scrapers.oneofus import fetch_oneofus_jobs
from scrapers.bluebolt import fetch_bluebolt_jobs
from scrapers.untold import fetch_untold_jobs
from scrapers.electric import fetch_electric_jobs
from scrapers.outpost import fetch_outpost_jobs
from scrapers.jfx import fetch_jfx_jobs

from core.telegram import send_telegram_message


def run():
    jobs = []

    jobs += fetch_dneg_jobs()
    jobs += fetch_framestore_jobs()
    jobs += fetch_cinesite_jobs()
    jobs += fetch_milk_jobs()
    jobs += fetch_oneofus_jobs()
    jobs += fetch_bluebolt_jobs()
    jobs += fetch_untold_jobs()
    jobs += fetch_electric_jobs()
    jobs += fetch_outpost_jobs()
    jobs += fetch_jfx_jobs()

    if not jobs:
        send_telegram_message("No VFX Producer / PM / Line Producer jobs in London today.")
        return

    message = "🎬 VFX JOBS (London)\n\n"

    for job in jobs:
        message += f"{job['title']}\n{job['url']}\n\n"

    send_telegram_message(message)


if __name__ == "__main__":
    run()
