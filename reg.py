import pyautogui
import random
import time

pyautogui.FAILSAFE=False
keyss = "shift"
while True:
    time.sleep(random.randint(90,110))
    for i in range(0,100):
        pyautogui.moveTo(random.randint(400,800),random.randint(400,800))
    for i in range(0,1):
        pyautogui.press(keyss)


#theta-byte-156721