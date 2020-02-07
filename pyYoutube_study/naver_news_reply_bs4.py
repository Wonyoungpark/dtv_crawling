from selenium import webdriver
import time
def get_replys(url,imp_time=5,delay_time=0.1):

    #웹 드라이버
    driver = webdriver.Chrome('./chromedriver.exe')
    driver.implicitly_wait(imp_time)
    driver.get(url)

    #더보기 계속 클릭하기
    while True:
        try:
            더보기 = driver.find_element_by_css_selector('a.u_cbox_btn_more')
            더보기.click()
            time.sleep(delay_time)
        except:
            break

    html = driver.page_source
    print(html)

    #모듈 참조
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html,'lxml') #html.parser는 파이썬에 기본적으로 있음, lsml이 속도가 더 빠름

    # 댓글 추출
    contents = soup.select('span.u_cbox_contents')
    contents = [content.text for content in contents]

    # 작성자
    nicks = soup.select('span.u_cbox_nick')
    nicks = [nick.text for nick in nicks]

    # 날짜 추출
    dates = soup.select('span.u_cbox_date')
    dates = [date.text for date in dates]


    #취합
    replys = list(zip(nicks,dates,contents)) #튜플로 묶임

    driver.quit()
    return replys

if __name__ == '__main__':
    from datetime import datetime
    start = datetime.now()

    # url = 'https://entertain.naver.com/ranking/comment/list?oid=312&aid=0000419006'
    url = 'https://entertain.naver.com/ranking/comment/list?oid=477&aid=0000216834'
    reply_data = get_replys(url,5,0.1) #reply의 데이터가 나올 것

    import pandas as pd
    col = ['작성자','날짜','내용']
    data_frame = pd.DataFrame(reply_data,columns=col)
    data_frame.to_excel('news.xlsx',sheet_name='몬스타엑스',startrow=0,header=True)

    end = datetime.now()
    print(end-start)

## 웹자동화할 때 selenium을 하되, 데이터를 크롤링할 때 selenium을 쓸 때는
# 접근을 해서 보는 것까지는 selenium으로, 데이터구문 분석하고 원하는걸 추출할 떄는 beautifulsoup을 같이 사용한다.
# 이렇게 동적페이지를 크롤링할 떄는 selenium과 beautifulsoup를 같이 쓰는게 난이도와 속도를 조절할 수 있다.
