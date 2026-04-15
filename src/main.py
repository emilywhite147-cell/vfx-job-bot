from scrapers.dneg import fetch_dneg_jobs
from scrapers.framestore import fetch_framestore_jobs

def run():
    jobs = []

    jobs.extend(fetch_dneg_jobs())
    jobs.extend(fetch_framestore_jobs())

    for job in jobs:
        print(job)

if __name__ == "__main__":
    run()
