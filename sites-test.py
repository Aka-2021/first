import time

import pyautogui


while True:
    x,y=pyautogui.position()

    print(f"x : {x}, y : {y}")
    time.sleep(1)