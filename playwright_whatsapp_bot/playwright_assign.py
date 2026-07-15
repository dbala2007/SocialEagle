from playwright.sync_api import sync_playwright
from datetime import datetime
import pandas as pd

print("Starting the Playwright script...")
print(f"Current date and time: {datetime.now()}")
start_time = datetime.now()

#Steps to automate:
#1. Launch the Chromium Browser
#2. Navigate to https://web.whatsapp.com/
#3. Read the "contacts.xlsx" and read the Name, Number and Personalized message from the sheet
#4. Search the contact in the whatsapp web and generate the personalized message for the contact
#5. Extract the last 3 sent messages in the chat
#6. Save it in a JSON and excel file for all the contacts read from the excel sheet
with sync_playwright() as p:
    print("Launching the Chromium browser...")
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    print("Navigating to WhatsApp Web...")
    page.goto("https://web.whatsapp.com/")
    page.wait_for_load_state("networkidle")
    page.wait_for_timeout(60000)  # Wait for the user to scan the QR code and log in
    # print(page.content())

    #Read the contacts from the excel sheet and send the personalized message to each contact
    contacts_df = pd.read_excel("contacts.xlsx")
    for index, row in contacts_df.iterrows():
        contact_name = row['Name']
        contact_number = row['Number']
        personalized_message = row['Message']

        print(f"Searching for contact: {contact_name} ({contact_number})")
        # search_box = page.locator("div[contenteditable='true'][data-tab='3']")
        search_box = page.get_by_placeholder("Search or start a new chat")
        search_box.fill(contact_name)
        page.wait_for_timeout(2000)  # Wait for the search results to load

        # Click on the contact from the search results
        contact_locator = page.locator(f"span[title='{contact_name}']")
        if contact_locator.count() > 0:
            contact_locator.first.click()
            print(f"Contact {contact_name} found. Sending message...")
            # message_box = page.locator("div[contenteditable='true'][data-tab='6']")
            message_box = page.locator("div[contenteditable='true']").last
            page.wait_for_timeout(2000)
            message_box.fill(personalized_message)
            message_box.press("Enter")
            print(f"Message sent to {contact_name}.")
        else:
            print(f"Contact {contact_name} not found.")
    
    browser.close()

print("Playwright script completed successfully.")
print(f"Current date and time: {datetime.now()}")
end_time = datetime.now()
run_time = end_time - start_time
print(f"Total time taken for the script to run: {run_time}")