from scrapers.dneg import fetch_dneg_jobs
from scrapers.framestore import fetch_framestore_jobs
from core.telegram import send_telegram_message

def run():
    print("STEP 1: started")

    jobs = []
    print("STEP 2: fetching dneg")
    jobs += fetch_dneg_jobs()

    print("STEP 3: fetching framestore")
    jobs += fetch_framestore_jobs()

    print(f"STEP 4: total jobs = {len(jobs)}")

    if not jobs:
        print("STEP 5: no jobs found")
        send_telegram_message("No jobs found today.")
        return

    print("STEP 6: building message")

    message = "VFX JOBS:\n\n"

    for job in jobs[:10]:
        message += f"{job['title']}\n{job['url']}\n\n"

    print("STEP 7: sending telegram")
    send_telegram_message(message)

    print("STEP 8: done")

if __name__ == "__main__":
    run()
