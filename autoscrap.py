import pyautogui
import time
import random

val= True

def content():
    time.sleep(1)
    pyautogui.moveTo(611, 856)
    pyautogui.click()
    time.sleep(1)

    #
    pyautogui.moveTo(1233, 48)
    pyautogui.click()
    pyautogui.moveTo(612, 494)
    pyautogui.rightClick()
    time.sleep(1)

    #inspect page
    pyautogui.moveTo(650, 763)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(1071, 301)
    time.sleep(1)
    pyautogui.scroll(20)
    time.sleep(1)
    pyautogui.moveTo(906,188)
    pyautogui.rightClick()
    time.sleep(1)
    pyautogui.moveTo(1001,316)
    time.sleep(1)
    pyautogui.click()
    pyautogui.moveTo(1144,330)
    time.sleep(1)
    pyautogui.click()

    pyautogui.moveTo(1005,847)
    pyautogui.click()

    pyautogui.moveTo(683,98)
    pyautogui.click()

    pyautogui.moveTo(412,138)

    pyautogui.hotkey('command','v')

#content()

def nextpage():
    time.sleep(1)
    pyautogui.moveTo(611, 856)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(706,469)
    pyautogui.scroll(-130)
    time.sleep(1)
    pyautogui.moveTo(539,283)
    pyautogui.click()
    time.sleep(3)
    if pyautogui.position(1439, 0):
        val=False

while val:

    for i in range(0,576,24):
        content()
        nextpage()


#nextpage()
'''url=[]
for i in range(0,576,24):
    url.append(f'https://www.target.com/c/tvs-home-theater-electronics/all-deals/-/N-5xtdwZakkos?Nao={i}')

with open('test.txt','w') as f:
    f.write(str(url))
'''
''' # second tab
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
'''