import pyautogui
import time
count = 0
text = input("What text do you want to spam? ")
time.sleep(4)

while count <= 1000:
    pyautogui.typewrite(text)
    pyautogui.press("enter")
    count=count