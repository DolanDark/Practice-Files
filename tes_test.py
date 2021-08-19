import pyautogui
import time
import keyboard
from PIL import Image
from pytesseract import *

pyautogui.PAUSE=0
pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

while keyboard.is_pressed('z') == False:
        x,y = pyautogui.position()
        x = int(x)
        y = int(y)

time.sleep(0.5)
while keyboard.is_pressed('z') == False:
        a,b = pyautogui.position()
        a = int(a)
        b = int(b)
print(x,y,a,b)