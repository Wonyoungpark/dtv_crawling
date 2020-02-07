from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from tqdm import tqdm

def get_images(keyword):
    # # keyword = "방탄소년단"
    # keyword = input("수집할 키워드를 입력하세요")

    # 웹 접속 - 네이버 이미지 접속
    print("접속 중")
    driver = webdriver.Chrome('./chromedriver.exe')
    driver.implicitly_wait(30)

    url = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query={}".format(keyword)
    driver.get(url)

    #페이지 스크롤 다운
    body = driver.find_element_by_css_selector('body')
    for i in range(3):
        body.send_keys(Keys.PAGE_DOWN)
        # time.sleep(1)

    #이미지 링크 수집
    imgs = driver.find_elements_by_css_selector('img._img')
    result=[]
    for img in tqdm(imgs):
        if 'http' in img.get_attribute('src'):
            result.append(img.get_attribute('src'))
    print(result)

    driver.close()
    print("수집 완료")

    #폴더 생성
    print("폴더 생성")
    import os
    if not os.path.isdir('./{}'.format(keyword)):
        os.mkdir('./{}'.format(keyword))

    #다운로드
    print("다운로드")
    from urllib.request import urlretrieve
    for index, link in tqdm(enumerate(result)):
        start = link.rfind('.') #result[0]==link
        end = link.rfind('&')
        # print(link[start:end])
        filetype = link[start:end] #.png

        urlretrieve(link,'./{}/{}{}{}'.format(keyword,keyword,index,filetype))
        time.sleep(1)

    print("다운로드 완료")

    #압축 - 메일
    import zipfile
    zip_file = zipfile.ZipFile('./{}.zip'.format(keyword),'w')

    # print(os.listdir('./{}'.format(keyword)))
    for image in os.listdir('./{}'.format(keyword)): #이 폴더 안에 파일들이 뭔지 알아내는 것 : listdir(=ls)
        print(image,"압축파일에 추가 중")
        zip_file.write('./{}/{}'.format(keyword,image), compress_type=zipfile.ZIP_DEFLATED) # os list를 통해서 악뮤 파일명들이 리스트로 잠김
    zip_file.close()
    print("압축 완료")

if __name__ =='__main__':
    keyword = input("수집할 이미지 키워드 입력 : ")
    get_images(keyword)