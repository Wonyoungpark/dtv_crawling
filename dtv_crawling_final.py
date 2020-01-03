from selenium import webdriver
import time
import pandas as pd
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import urllib
import re
from urllib.request import urlopen
import html5lib
from selenium import *
from selenium.common.exceptions import NoSuchElementException
import openpyxl
from tqdm import tnrange

# 전체 카테고리에서 URL 받아오기
def get_URL():
    URL_list=[]
    for page in range(1,10):
        URL ='https://pc.video.dmkt-sp.jp/genre/genre-list/id/' + str(100+page)
        URL_list.append(URL)
    return URL_list

# '각 드라마 모두보기'에서 드라마 클릭하기
def drama_click():
    allFind = driver.find_element_by_css_selector('h2 > span > a > span')
    allFind.click()
    time.sleep(5)

#스크롤 내리기
def page_down_drama():
    body=driver.find_element_by_tag_name('body')
    num_pagedown = 100
    while num_pagedown:
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.3)
        num_pagedown-=1

# href 받아오기
def get_href():
    source = driver.page_source
    soup = BeautifulSoup(source,'html.parser')
    hrefs = soup.select("a[class=titleCard_link]")

    hrefs_lists=[]
    for hre in hrefs:
        h = hre.get('href')
        hrefs_lists.append(h)
    return hrefs_lists

#작품 정보, 제목,에피소드,키워드 추출(완)
drama = []
def get_info():
    global title, episode

    try:
        detail_list=[]
        find_detail = soup.findAll("p",{"class" : "titleDetailInfo_tx titleDetailInfo_tx--wide"})
        for details in find_detail:
            detail_list.append(details.text)
            if len(detail_list) < 1:
                detail_list=None
    except:
        detail_list=[]

    try:
        find_title = soup.findAll("span",{"class" : "titleDetailHeading_title"})
        for title in find_title:
            title=title.text
    except:
        title = None

    try :
        episode = ""
        find_ep = soup.findAll("p",{"class" : "titleDetailChapter_title"})
        for episodes in find_ep:
            episode.append(episodes.text)
            if len(episode) < 1:
                episode = None
    except :
        episode = None

    try:
        keyword=[]
        find_kwd = soup.findAll("span", {"class" : "titleDetailKeyword_string"})
        for keywd in find_kwd:
            keyword.append(keywd.text)
    except:
        keyword=[]

    try:
        category = driver.find_element_by_css_selector('h1 > ul > li:nth-child(2) > a').text
    except:
        None

    drama.append({'category':category,
                'title':title,
                'detail':detail_list,
                 'episode':episode,
                 'keyword':keyword})

    return drama

if __name__=='__main__':

    # 창 열기
    driver = webdriver.Chrome('./chromedriver.exe')
    driver.implicitly_wait(3)

    # 카테고리 별 정보 갖고 오기
    for i in range(10):
        cat_drama_dict = {}
        url = get_URL()[i]
        driver.get(url)

        try:
            drama_click()

            current_URL= driver.current_url
            resource = requests.get(current_URL)
            source = driver.page_source
            soup = BeautifulSoup(source,'html.parser')

            page_down_drama()

            # 갖고 올 모든 정보 출력
            for u in tnrange(5000):
                try:
                    g = get_href()[u]
                    req = requests.get(g)
                    source = req.text
                    soup = BeautifulSoup(source, 'html.parser')
                    info_df = pd.DataFrame(get_info())
                    time.sleep(0.1)

                except IndexError:
                    pass
                    print('index의 값을 가져올 수 없습니다.')

            # 데이터의 중복 제거
            info_df.drop_duplicates('title',keep='first')

        except NoSuchElementException:
            pass

    # 데이터를 엑셀에 저장하기
    fin_table = pd.DataFrame(info_df)
    fin_table.to_excel("test.xlsx")
