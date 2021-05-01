import pyautogui    # Used to automate keyboard, mouse, etc.
import time

while True:
    pyautogui.typewrite('Hello')
    time.sleep(5)
    pyautogui.press('enter')
