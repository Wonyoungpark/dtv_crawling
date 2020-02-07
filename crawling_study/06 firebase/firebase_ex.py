import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

#Firebase database 인증 및 앱 초기화
cred = credentials.Certificate('mykey.json')
firebase_admin.initialize_app(cred,{
    'databaseURL' : 'https://semicircle-acb93.firebaseio.com/'
})

"""
ref = db.reference() #ref에 db 위치 지정
ref.update({'반원' : '고슴도치'}) # 해당 변수가 없으면 생성한다.

ref = db.reference('강좌/파이썬') #경로가 없으면 자동으로 생성한다.
ref.update({'파이썬 레시피 웹 활용' : 'complete'})
ref.update({'파이썬 괴식 레시피' : 'Proceeding'})

#리스트 전송시
ref = db.reference() #db 위치 지정
ref.update({'수강자' : ['구독자A','구독자B','구독자C','구독자D']}) #해당 변수가 없으면 생성한다.
#VALUE값 안에는 딕셔너리 형태가 아님 따라서 리스트의 index로 자리잡음
"""

#데이터베이스 레퍼런스 생성 후 데이터 읽기
ref = db.reference('없는 경로') #이 당시의 데이터가 확인된다.
print(ref.get()) #특정 값을 갖고 올 수 있음

ref = db.reference('반원')
print(ref.get())

ref = db.reference('강좌/파이썬')
print(ref.get()) #json형태로 받아올 수도 있음

ref = db.reference('수강자')
print(ref.get()) #list로 반환