import pyautogui
import random
import time
import keyboard
import win32api, win32con

while True:
    if pyautogui.locateOnScreen('stick.png', region=(0,0,700,700), grayscale=True, confidence=0.8) != None:
        print("I can see it")
        time.sleep(0.5)
    else:
        print("I cant see it")
        time.sleep(0.5)
.