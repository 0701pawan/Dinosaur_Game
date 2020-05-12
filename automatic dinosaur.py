import pyautogui
from PIL import Image, ImageGrab
import time

### The below function automatically presses the key which is given to it as an argument #### 
def hit(key):
    pyautogui.keyDown(key)

### The below function takes the screenshot of the desktop ##
def takescreenshot():
    image = ImageGrab.grab()
    return image

#### This function checks if data in the frame is black or not if it is black it automatically jumps ####
def isCollid(data):
    for i in range(760,780):
        for j in range(220,260):
            if data[i,j]<100:
                return True
    return False

if __name__=="__main__":
    time.sleep(2)
    hit("up")

### this is a continues loop ####
    while True:
        image = ImageGrab.grab().convert('L')
        data=image.load()
        if isCollid(data):
            hit("up")
       
