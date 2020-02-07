from bs4 import BeautifulSoup
from pprint import pprint
import requests

#웹 페이지를 열고 소스코드를 읽어오는 작업
html=requests.get("https://comic.naver.com/webtoon/weekday.nhn")
soup=BeautifulSoup(html.text,'html.parser')
html.close()

#모든 요일웹툰영역 추출하기
data1_list=soup.findAll('div',{'class':'col_inner'})
pprint(len(data1_list))

#전체 웹툰 리스트
week_title_list=[]

for data1 in data1_list:
    # 제목 포함영역 추출하기
    data2=data1.findAll('a',{'class':'title'})
    #pprint(data2)

    #텍스트만 추출
    title_list = [t.text for t in data2]
    # pprint(title_list)
    week_title_list.append(title_list) #이중리스트
    # week_title_list.extend(title_lsit) #리스트에 추가

# print(week_title_list)
print(week_title_list[0]) #월요웹툰만 추출