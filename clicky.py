import pyautogui
import time
import keyboard
import random
import win32api,win32con


# Title Position: X:587 Y:430 RGB (79,81,116)
# Title Position: X:682 Y:430 RGB (79,81,116)
# Title Position: X:780 Y:430 RGB (79,81,116)
# Title Position: X:871 Y:430 RGB (79,81,116)

'''def click(x,y):                          #using the win32api
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
'''
pyautogui.PAUSE = 0
pyautogui.sleep(3)

def clicky(x,y):
    time.sleep(0.1)
    pyautogui.click(x,y)


while keyboard.is_pressed('q') == False:

    if pyautogui.pixel(587,430)[0] == 0:
        clicky(587,430)
    if pyautogui.pixel(682,430)[0] == 0:
        clicky(682,430)
    if pyautogui.pixel(780,430)[0] == 0:
        clicky(780,430)
    if pyautogui.pixel(871,430)[0] == 0:
        clicky(871,430)


