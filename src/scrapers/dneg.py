from .universal import scrape_company

def fetch_dneg_jobs():
    return scrape_company("https://www.dneg.com", "/careers/")
