import pyautogui as pg
import time
from PIL import ImageGrab
import keyboard

taps = [(1522,459),(1554,459),(1363,459),(1410,459)]
state = False

width, height = pg.size()
box = (0, 0, width/2, height)
def play():
    screen = ImageGrab.grab() # screen은 전체 화면
    for tap in taps:
        if (0,0,0) == screen.getpixel(tap):
            pg.click(*tap)

while True:
    # print(pg.position())
    # time.sleep(.5)
    if not state and keyboard.is_pressed('a'):
        state = True
        print("Start!")

    elif state and keyboard.is_pressed('s'):
        state = False
        print("Stop!")

    if state:
        play()
