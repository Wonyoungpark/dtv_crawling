from selenium import webdriver
import time

options = webdriver.ChromeOptions()
#options.add_argument('headless') #창이 보이지 않음 #날짜가 영어로 나옴


driver = webdriver.Chrome('chromedriver' """, chrome_options=options""")
driver.get("https://www.twitch.tv/soorte214/clip/AgileGracefulCheesecakePeteZarollTie") #특정 클립 링크

time.sleep(3)

#video 태그 확인
url_element = driver.find_element_by_tag_name('video')
vid_url = url_element.get_attribute('src')
# print(vid_url)

#클립 제목과 날짜 확인
title_element1 = driver.find_element_by_class_name('tw-flex')
title_element2 = title_element1.find_elements_by_tag_name('span')
vid_title,vid_date = None, None
for span in title_element2:
    try:
        d_type =span.get_attribute('data-test-selector')
        if d_type == "title":
            vid_title = span.text
        elif d_type == 'date':
            vid_date = span.text
    except:
        pass

print(vid_title,vid_date)

#특수문자와 빈칸 없에기
import re
vid_title = re.sub('[^0-9a-zA-Zㄱ-힗]', '', vid_title)
vid_date = re.sub('[^0-9a-zA-Zㄱ-힗]', '', vid_date)
print(vid_title,vid_date)

#다운로드
from urllib.request import urlretrieve
urlretrieve(vid_url,vid_title+'_'+vid_date+'.mp4')

driver.close()