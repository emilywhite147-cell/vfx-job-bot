from .universal import scrape_company

def fetch_framestore_jobs():
    return scrape_company("https://www.framestore.com", "/careers")
