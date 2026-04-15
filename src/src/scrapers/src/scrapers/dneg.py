from playwright.sync_api import sync_playwright


class DnegScraper:
    def fetch_jobs_sync(self):
        jobs = []

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto("https://www.dneg.com/careers/", wait_until="networkidle")

            links = page.locator("a").all()

            for link in links:
                text = link.inner_text().strip()
                href = link.get_attribute("href")

                if text and href and len(text) < 120:
                    if href.startswith("/"):
                        href = "https://www.dneg.com" + href
                    jobs.append({
                        "studio": "DNEG",
                        "title": text,
                        "url": href,
                    })

            browser.close()

        return jobs
