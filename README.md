# Gen AI Architect Program by Social Eagle

[SocialEagle](https://github.com/dbala2007/SocialEagle)

## Week 1 - Day 2 Introduction to Python Assignment

*Assignment 1*

> Take input from the user and calculate the grade system

Refer **grade_system > grade_system.py**

Refer [PythonConcepts](https://github.com/Thirumurugan240/Python_Concepts) for importaint concepts

## Week 1 - Day 3 Introduction to RPA

*Assignment 1*

> Use PyAutoGUI to automate the below task

- Open Chrome and go to any public website (for example: a weather, news, or stock-price site).
- Copy the important piece of information from the page (the temperature, the top headline, or a
stock value).
- Open Microsoft Excel (or Numbers on Mac).
- Create a new row containing three things: today's date & time, the fetched data, and your own
short comment (for example, “Good for outdoor activities”).
- Save the Excel file with today's date in the filename, e.g. daily_report_2025-06-17.xlsx.
- Take a screenshot of the final Excel sheet and save it.

Refer **daily_bot_report > daily_bot_report.py**

*Assignment 2*

> Use Playwright to automate Web Whatsapp Message Bot

- Log in to WhatsApp Web (handle the QR code manually on the first run).
- Read contacts from an Excel file named contacts.xlsx with columns: Name, Phone (with
country code, e.g. +91xxxxxxxxxx), and Message (an optional template).
- For each contact: search the contact or number, send a personalized message (replace {name}
with the actual name), wait for the message to be sent, then take a screenshot of the sent
message.
- Smart data extraction (bonus core part): after sending, open a contact and extract the last 3
messages from them.
- Save everything in a report as both JSON and Excel.
- whatsapp_report_YYYY-MM-DD.json (full details).
- whatsapp_report_YYYY-MM-DD.xlsx (a summary).

Refer **playwright_whatsapp_bot > playwright_whatsapp_bot.py**

Refer [PyAutoGUI & Playwright](https://github.com/manojkanur/genai-automation)

## Week 1 - Day 4 Introduction to API (Backend)

*Assignment 1*

> Use FastAPI to build a basic backend API

- Use the FastAPI framework to build the app.
- Create a root endpoint GET / that returns a simple JSON response (for example, a welcome
message).
- Add at least one more endpoint that takes a value from the URL - either a path parameter (for
example, /greet/{name}) or a query parameter - and returns it inside the response.
- Run the app with the Uvicorn server and confirm it works in the browser.
- Open the automatic interactive docs at /docs and check your endpoints there.
- Keep all your code in a single file named main.py

Refer **fast_api_basicapp > main.py**

*Assignment 2*

> Use Streamlit to build a basic UI for the Grading System

- Use the Streamlit framework to build the user interface. Pure Python for the grading logic.
- Provide an input widget where the user can enter or choose a mark.
- Display the entered mark and the resulting grade clearly on the page.
- Handle the full 0-100 range and cover every grade band above.
- Give the app a title or heading so it looks finished.
- Keep all your code in a single file named grade_app.py.

Refer **grade_system > grade_app.py**

Refer [Stremlit](https://github.com/Thirumurugan240/Streamlit.git)