# Gen AI Architect Program by Social Eagle
# Batch 10 - B10 (1)

[SocialEagle](https://github.com/dbala2007/SocialEagle)

## B10 - Week 1 - Day 2 Introduction to Python Assignment

*Assignment 1*

> Take input from the user and calculate the grade system

Refer **grade_system > grade_system.py**

Refer [PythonConcepts](https://github.com/Thirumurugan240/Python_Concepts) for importaint concepts

## B10 - Week 1 - Day 3 Introduction to RPA

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

## B10 - Week 1 - Day 4 Introduction to API (Backend)

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

Refer [Streamlit](https://github.com/Thirumurugan240/Streamlit.git)

## B10 - Week 2 - Day 1 RTCFR Assignment

*Assignment 1*

> Use ChatGPT (or any AI tool) to test the RTCFR framework

- Write one RTCFR-structured prompt - do not hand-write the meal plan yourself.
- Label or clearly express each of the five elements: Role, Task, Context, Few Shots, Response
Format.
- The plan it produces must be South Indian, vegetarian, and aimed at healthy weight loss.
- It must cover all 7 days of the week.
- Use the Few Shots section to give one or two sample meal recommendations so the model
copies the right style.
- Ask for the answer as a clean day-wise table

Refer **Week2 > Day1 Assignment.md**

## B10 - Week 2 - Day 2 JSON Image and Video Generation Prompting

*Assignment 1*

> Use ChatGPT (or any AI tool) to test the SCALE framework
> Generate Image and Video using the SCALE JSON prompting technique

- Three images (Gemini and ChatGPT) representing Tamil Nadu Culture
- One Video (using Qwen) representing Tamil Nadu Culture

Refer **Week2 > Day2 Assignment.md**
Refer **Week2 > ChatGPT_*.png** for ChatGPT generated images
Refer **Week2 > Gemini_*.png** for Gemini generated images
Refer **Week2 > B10-Week2-Day2-SCALE Video Generation Assignment.mp4** for Qwen generated Video

## B10 - Week 2 - Day 3 Langchain and Langsmith

Refer [LangChain](https://github.com/Thirumurugan240/Langchain)

*Assignment 1*

> Use LangChain and LangSmith to execute an Open AI Chat model and view the execution trace

- Use the LangChain framework to talk to the model (do not call the OpenAI API directly).
- Send an input or prompt to an OpenAI chat model and print the response in the terminal.
- Enable LangSmith tracing so the run is logged and visible in your LangSmith project.
- Read all API keys from environment variables - never hard-code or commit them.
- Keep all your code in a single file named main.py *(Note here I have not used main.py)*

Refer **Week2 > langchain_app.py**

## B10 - Week 2 - Day 4 RAG Assignment

Refer [RAG](https://github.com/Thirumurugan240/Introduction_to_RAG)

*Assignment 1*

> Use Langchain and Streamlit to accept PDF and retrieve information from the uploaded PDF

- Show a Streamlit interface with a PDF file uploader.
- When a PDF is uploaded, load it, split it into chunks, create embeddings, and store them in a
vector database (for example, FAISS or Chroma) so the database is ready to search.
- Give the user a query box to ask questions about the uploaded PDF.
- Use LangChain retrieval together with an OpenAI model to answer from the PDF content.
- Display the answer clearly in the app.
- Read your API key from an environment variable - never hard-code or commit it.
- Keep all your code in a single file named app.py.

Refer **Week2 > rag_assignment > app.py**