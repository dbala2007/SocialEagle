from playwright.sync_api import sync_playwright
from datetime import datetime

print("Starting the Playwright script...")
print(f"Current date and time: {datetime.now()}")
start_time = datetime.now()

#Daily Weather Report Bot
#Chromium -> weather site -> Extract the report -> Screenshot -> Save the report -> Close the browser
with sync_playwright() as p:
    print("Launching the Chromium browser...")
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    print("Navigating to the weather website...")
    page.goto("https://www.accuweather.com/en/in/chennai/206671/weather-forecast/206671?type=locality&city=chennai")
    # page.wait_for_load_state("networkidle", timeout=60000)  # Wait for the page to load completely
    page.screenshot(path="accuweather.png")

    print("Extracting the weather report...")
    locator = page.locator("div.today-forecast-card")

    locator.wait_for(timeout=60000)

    weather_report = locator.inner_text()
    print(f"Current Weather Report: {weather_report}")

    print("Saving the weather report to a text file...")
    with open("weather_report.txt", "w") as file:
        file.write(f"Weather Report for Chennai on {datetime.now()}:\n")
        file.write(weather_report)
    
    print("Closing the browser...")
    browser.close()

print("Playwright script completed successfully.")
print(f"Current date and time: {datetime.now()}")

#Calculate the time taken for the script to run in human readable format
end_time = datetime.now()
run_time = end_time - start_time
print(f"Total time taken for the script to run: {run_time}")