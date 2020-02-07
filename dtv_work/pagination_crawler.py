from bs4 import BeautifulSoup
import requests

maximum = 0
page = 1

# request라이브러리를 활용한 html페이지 요청
URL = 'http://land.naver.com/news/field.nhn?page=1'
response=requests.get(URL)
 # response 객체에 HTML 데이터가 저장되고, res.text로 데이터를 추출 가능

#HTML페이지 파싱 - BeautifulSoup(HTML데이터,파싱방법)
source = response.text
soup = BeautifulSoup(source, 'html.parser')

while 1:
    page_list = soup.findAll("a",{"class":"NP=r:"+str(page)})

    if not page_list:
        maximum=page-1
        break
    page=page+1
# print("총 "+str(maximum)+"개의 페이지가 확인이 되었습니다.")

whole_source = ""
for page_number in range(1,maximum+1):
    URL = 'http://land.naver.com/news/field.nhn?page=' + str(page_number)
    response = requests.get(URL)
    whole_source+= response.text

soup = BeautifulSoup(whole_source,'html.parser')
find_title = soup.select('#content > div.section_headline > ul > li > dl > dt > a')

for title in find_title:
    print(title.text)


