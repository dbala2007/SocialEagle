from playwright.sync_api import sync_playwright
from urllib.parse import urljoin
import json

with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=False
    )

    page = browser.new_page()

    page.goto("https://www.tn.gov.in/scheme_list.php?dep_id=Mg==")

    links = page.locator("a")
    scheme_links = []
    all_schemes = []

    for i in range(links.count()):
        href = links.nth(i).get_attribute("href")
        if href and "scheme_details" in href:
             full_url = urljoin(
                 page.url,
                 href
             )
             scheme_links.append(full_url)


    for url in scheme_links:
        page.goto(url)
        page.wait_for_selector("table")
        page.wait_for_timeout(2000)
        content = page.locator("body").inner_text()

        tables = page.locator("table")
        rows = tables.locator("tr")
        scheme = {}
        current_section = ""
        for i in range(rows.count()):
            row = rows.nth(i)
            cells = row.locator("td")
            if cells.count() == 0:
                continue

            if cells.count() == 1:
                current_section = cells.nth(0).inner_text().strip()
                continue

            key = cells.nth(0).inner_text().replace(":", "").strip()
            value = cells.nth(1).inner_text().strip()
            scheme[key] = {
                "section": current_section,
                "value": value
            }
        scheme["url"] = url
        scheme["title"] = page.title()

        all_schemes.append(scheme)

    with open("tn_govt_schemes.json", "w", encoding='utf-8') as f:
        json.dump(all_schemes, f, indent=4, ensure_ascii=False)

    browser.close()