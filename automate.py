import pyautogui
import time
import random

val= True
def autotab(waitingtime, sc):

    time.sleep(waitingtime)
    pyautogui.moveTo(611, 856, 1, pyautogui.easeInQuad)
    pyautogui.click()
    time.sleep(waitingtime)

    # first tab
    pyautogui.moveTo(485, 51, 0.5, pyautogui.easeInBack)
    pyautogui.click()
    pyautogui.moveTo(422, 475, 0.5, pyautogui.easeInBounce)
    time.sleep(waitingtime)
    pyautogui.scroll(sc)

    # second tab
    pyautogui.moveTo(1043, 49, 0.5, pyautogui.easeInQuad)
    pyautogui.click()
    time.sleep(waitingtime)
    pyautogui.scroll(sc)
    pyautogui.moveTo(422, 475, 0.5, pyautogui.easeInBounce)
    pyautogui.click()

    # third tab
    pyautogui.moveTo(697, 46, 0.5, pyautogui.easeInCirc)
    pyautogui.click()
    time.sleep(waitingtime)
    pyautogui.moveTo(422, 475, 0.5, pyautogui.easeInElastic)
    pyautogui.scroll(sc)

    if pyautogui.position(1439, 0):
        val=False


keyss = "shift"
tm = [1, 1]
src = [-20, 20]
while val:
    time.sleep(90)

    for i in range(0, 2):
        autotab(tm[i], src[i])
