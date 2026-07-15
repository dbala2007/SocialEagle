from playwright.sync_api import sync_playwright

browser = sync_playwright().start().chromium.launch(headless=False) #headless = False will open chrome
page =browser.new_page()

page.goto("https://www.screener.in/company/NIFTY/#constituents")
page.screenshot(path="screener.png")

page.click("text=50")

browser.close()
