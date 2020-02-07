from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests #웹페이지 요청하는 코드

html = requests.get('https://search.naver.com/search.naver?query=날씨')
#특정URL을 적으면 그 페이지의 소스코드를 볼 수 있음
#응답 데이터가 html변수에 저장됨
#pprint(html.text) #html에 대한 text속성을 프린트

soup = bs(html.text,'html.parser')
#pprint(soup)

data1 = soup.find('div',{'class':'detail_box'}) #영역추출
#pprint(data1)

data2=data1.findAll('dd')
#pprint(data2[0])

find_dust=data2[0].find('span',{'class':'num'}).text
print(find_dust)