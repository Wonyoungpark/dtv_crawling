import os
import sys
import urllib.request
import json
from pprint import pprint

#번역할 메모장 불러오기
with open('source.txt','r',encoding='utf8') as f:
    srcText = f.read()

client_id = "_e6nsW65Qd5expS1Nt7k" #개발자센터에서 발급받은 Client ID값
client_secret = "2j_aJRVLmr" #개발자센터에서 발급받은 Client Secret값
encText = urllib.parse.quote(srcText) #변역할 내용
data = "source=ko&target=ja&text=" + encText
url = "https://openapi.naver.com/v1/papago/n2mt"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)
response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    # print(response_body.decode('utf-8'))

    res = json.loads(response_body.decode('utf-8'))
    pprint(res)

    #파일 생성
    with open('translate.txt','w',encoding='utf8') as f:
        f.write(res['message']['result']['translatedText'])

else:
    print("Error Code:" + rescode)