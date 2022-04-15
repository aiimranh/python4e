import pyautogui
import time
time.sleep(10)
x=0
while x<=5:
    pyautogui.typewrite('Hello')
    pyautogui.press('enter')
    x=x+1



