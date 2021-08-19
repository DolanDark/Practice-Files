import pyautogui
import time
import keyboard
from PIL import Image
from pytesseract import *

pyautogui.PAUSE=0
pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

while keyboard.is_pressed('z') == False:
        x,y = pyautogui.position()

time.sleep(0.5)

while keyboard.is_pressed('z') == False:
        a,b = pyautogui.position()

selectt = pyautogui.screenshot(region=(x,y,a - x,b - y))
selectt.save(r"C:\Users\gg\Desktop\Akash\autoclick\trans_image.png")

img = Image.open("trans_image.png")

#uncomment for better accuracy
#new_size = tuple(4*x for x in img.size)
#img = img.resize(new_size, Image.ANTIALIAS)

output = pytesseract.image_to_string(img)
print(output)
