import time
from datetime import datetime

try:
    import pyautogui
except ImportError as e:
    raise SystemExit(f"Install the missing dependency {e}. Install requirements with 'pip install -r requirements.txt'") from e

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5

# Step 1 - Open Chrome
print("Opening Chrome...")
time.sleep(2)

pyautogui.hotkey('win','r',interval=0.2)
time.sleep(2)

pyautogui.write('chrome',interval=0.2)
time.sleep(2)

pyautogui.hotkey('enter',interval=0.2)
time.sleep(2)

#Step 2 - Creating a new tab
print("Opening a new tab...")

pyautogui.hotkey('ctrl','t',interval=0.2)
time.sleep(2)

#Step 3 - Open the website
print("Open the website...")

pyautogui.write('https://www.screener.in/company/NIFTY/#constituents',interval=0.2)
time.sleep(5)

pyautogui.scroll(-500)
time.sleep(3)

pyautogui.hotkey('enter',interval=0.2)
time.sleep(2)

#Step 4 - Copy the data
print("Copying the data...")

pyautogui.hotkey('ctrl','a', interval=0.2)
time.sleep(2)

pyautogui.hotkey('ctrl','c',interval=0.2)
time.sleep(2)

pyautogui.hotkey('ctrl','w',interval=0.2)
time.sleep(2)

pyautogui.hotkey('ctrl','w',interval=0.2)
time.sleep(2)

#Step 5 - Open the excel
print("Opening the Excel")
pyautogui.hotkey('win','r',interval=0.2)
time.sleep(2)

pyautogui.write('excel',interval=0.2)
time.sleep(2)

pyautogui.hotkey('enter',interval=0.2)
time.sleep(2)

pyautogui.hotkey('enter',interval=0.2)
time.sleep(2)

#Step 6 - Writing timestamp in the first row
print("Writing the timestamp...")
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

pyautogui.press('f2',interval=0.2)
time.sleep(2)

pyautogui.write(timestamp, interval=0.2)
time.sleep(2)

pyautogui.press('enter',interval=0.2)
time.sleep(2)

#Step 7 - Writing my comment
print("Writing the comment...")
pyautogui.press('f2',interval=0.2)
time.sleep(2)

pyautogui.write('Nifty 50 details for today',interval=0.2)
time.sleep(2)

pyautogui.press('enter',interval=0.2)
time.sleep(2)

#Step 8 - Pasting the content
print("Pasting the data...")
pyautogui.hotkey('ctrl','v',interval=0.2)
time.sleep(2)


#Step 9 - Saving the file
print("Saving the Excel file...")
date_now = datetime.now().strftime("%Y-%m-%d")
file_name = f'daily_report_{date_now}'

pyautogui.hotkey('ctrl','s',interval=0.2)
time.sleep(2)

pyautogui.write(file_name, interval=0.2)
time.sleep(2)

pyautogui.press('enter',interval=0.2)
time.sleep(2)

#Step 10 - Screenshot the final excel
screenshot = pyautogui.screenshot()
screenshot.save(f"{file_name}.png")

pyautogui.hotkey('ctrl','x',interval=0.2)
time.sleep(2)