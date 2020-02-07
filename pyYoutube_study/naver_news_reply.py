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

    #댓글 추출
    contents = driver.find_elements_by_css_selector('span.u_cbox_contents')
    # for content in contents:
    #     print(content.text)
    contents = [content.text for content in contents]

    #작성자
    nicks = driver.find_elements_by_css_selector('span.u_cbox_nick')
    # for nick in nicks:
    #     print(nick.text)
    nicks = [nick.text for nick in nicks]

    #날짜 추출
    dates = driver.find_elements_by_css_selector('span.u_cbox_date')
    # for date in dates:
    #     print(date.text)
    dates = [date.text for date in dates]

    #취합
    replys = list(zip(nicks,dates,contents)) #튜플로 묶임
    # for reply in replys:
    #     print(reply)

    driver.quit()
    return replys

if __name__ == '__main__':
    from datetime import datetime
    start = datetime.now()

    url = 'https://entertain.naver.com/ranking/comment/list?oid=312&aid=0000419006'
    reply_data = get_replys(url,5,0) #reply의 데이터가 나올 것

    import pandas as pd
    col = ['작성자','날짜','내용']
    data_frame = pd.DataFrame(reply_data,columns=col)
    data_frame.to_excel('news.xlsx',sheet_name='위플레이 하성운',startrow=0,header=True)

    end = datetime.now()
    print(end-start)