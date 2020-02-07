from bs4 import BeautifulSoup
import requests

URL = "https://pc.video.dmkt-sp.jp/ti/10025227"
resource = requests.get(URL)
source = resource.text
soup = BeautifulSoup(source, 'html.parser')
# soup = BeautifulSoup(source, 'lxml')

result={}
# find_title = soup.findAll("span",{"class" : "titleDetailHeading_title titleDetailHeading_title--rental"})
# for title in find_title:
#     result["title"] = title.text
#
#
# find_ep = soup.findAll("p",{"class" : "titleDetailChapter_title"})
# for episode in find_ep:
#     result["episode"] = episode.text
#
# keyword=[]
# find_kwd = soup.findAll("span", {"class" : "titleDetailKeyword_string"})
# for keywd in find_kwd:
#     keyword.append(keywd.text)
#     result["keyword"] = (keyword)



# find_detail = soup.findAll("p",{"class" : "titleDetailInfo_tx titleDetailInfo_tx--wide"})

detail_data = str(soup.select('div:nth-child(1) > p')[4]).split('<br/>')

for i in range(len(detail_data)):
    detail = BeautifulSoup(detail_data[i]).text

    print(detail)

    #for h in det_data:


    # if i.isdigit():
    #     result["date"] = det_data[0]


# print(result)


