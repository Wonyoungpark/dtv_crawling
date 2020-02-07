from bs4 import BeautifulSoup
import requests
import selenium

URL = "https://pc.video.dmkt-sp.jp/ti/10025227"
resource = requests.get(URL)
source = resource.text
soup = BeautifulSoup(source, 'html.parser')

result={}
detail=[]
find_detail = soup.findAll("p",{"class" : "titleDetailInfo_tx titleDetailInfo_tx--wide"})
# f_detail = find_detail.find_all("a")
for f in find_detail:
    # a = f.find_all('a')
    a=f.text
    print(a)