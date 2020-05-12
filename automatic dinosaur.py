import pyautogui
from PIL import Image, ImageGrab
import time

def hit(key):
    pyautogui.keyDown(key)


def takescreenshot():
    image = ImageGrab.grab()
    return image

def isCollid(data):
    for i in range(760,780):
        for j in range(220,260):
            if data[i,j]<100:
                return True
    return False

if __name__=="__main__":
    time.sleep(2)
    hit("up")


    while True:
        image = ImageGrab.grab().convert('L')
        data=image.load()
        if isCollid(data):
            hit("up")
        # for i in range(740, 750):
        #     for j in range(220, 260):
        #         data[i, j] =0
        #
        # image.show()






    # if isCollid(data):
    #     hit("up")