from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('chromedriver')
driver.get("https://www.youtube.com/")

time.sleep(3)

search = driver.find_element_by_xpath('//*[@id="search"]')
#검색창에 xpath로 계산된 경로임

#search 변수에 저장된 곳에 값을 전송
search.send_keys('반원 코딩')
time.sleep(1)

#search 변수에 저장된 곳에 엔터를 입력
search.send_keys(Keys.ENTER)