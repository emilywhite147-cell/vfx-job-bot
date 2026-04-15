from .universal import scrape_company

def fetch_cinesite_jobs():
    return scrape_company("https://www.cinesite.com", "/careers/")
