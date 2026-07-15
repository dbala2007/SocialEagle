from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False) #headless = False will open chrome
    page = browser.new_page()
    page.goto("https://www.google.com")
    page.screenshot(path="google.png")
    browser.close()

