from PIL import ImageGrab, ImageOps
from numpy import *
import pyautogui, time

#전역변수
replayBtn = (488,463)
dino = (190,476)
lookBox = (dino[0]+80, dino[1],dino[0]+130,dino[1]+30)#공룡의 시야

#초기화
pyautogui.click(replayBtn) #리플레이버튼 좌표 클릭

def detectObs():
    image = ImageGrab.grab(lookBox)
    grayImage = ImageOps.grayscale(image)
    # print(array(grayImage.getcolors()).sum())
    return array(grayImage.getcolors()).sum()

while True:
    #장애물이 감지되었을 때
    if 1747 != detectObs():
        pyautogui.press('space') #press는 한번 눌렀다가 뗀 동작이 합쳐진 것
