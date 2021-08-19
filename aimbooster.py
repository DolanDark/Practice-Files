import time
import pyautogui
import random
import keyboard

pyautogui.PAUSE=0
time.sleep(2)

def clicky_boi(x,y):
    pyautogui.click(x,y)


# 638,330, 1269,761     255, 219, 195
while keyboard.is_pressed("q") == False:
    picture = pyautogui.screenshot(region=(638,330,631,431))
    width,height = picture.size

    for x in range(0,width,5):
        for y in range(0,height,5):

            r,g,b = picture.getpixel((x,y))

            if b == 195 and g == 219:
                clicky_boi(x+638,y+330)
                time.sleep(0.08)
                break


