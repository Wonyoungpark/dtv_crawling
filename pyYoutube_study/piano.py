import pyautogui as pg
import time
from PIL import ImageGrab
import keyboard

taps = [(1522,459),(1554,459),(1363,459),(1410,459)]



while True:

    screen = ImageGrab.grab() # screen은 전체 화면
    print(screen.getpixel(taps[0]))


