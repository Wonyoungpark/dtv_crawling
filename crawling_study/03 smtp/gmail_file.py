import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

sendEmail = "googleID@gmail.com"
recvEmail = "Receive Email"
password ="Google Password"

smtpName = "smtp.gmail.com" #smtp 서버 주소
smtpPort =587 #smtp 포트 번호

#여러 MIME을 넣기 위한 MIMEMultipart 객체 생성
msg = MIMEMultipart()

#본문 추가
text ="This is an Email content"
contentPart=MIMEText(text) #MIMEText(text, _charset = "utf8")
msg.attach(contentPart)

#파일 추가
etcFileName = 'test.txt'
with open(etcFileName, 'rb') as etcFD:
    etcPart = MIMEApplication(etcFD.read())
    #첨부파일의 정보를 헤더로 추가
    etcPart.add_header('Content-Disposition','attachment',filename=etcFileName)
    msg.attach(etcPart)

msg['Subject']="This is the Email subject"
msg['From']=sendEmail
msg['To']=recvEmail
#편지 보낼 곳 적음
print(msg.as_string())

s=smtplib.SMTP(smtpName, smtpPort) #메일 서버 연결
s.starttls() #TLS보안 처리
s.login( sendEmail , password )  # 로그인
s.sendmail(sendEmail,recvEmail,msg.as_string()) #메일 전송, 문자열로 반환
# 사실상 우체국을 통해 접수 후 배송되는 과정

s.close() #smtp 서버 연결을 종료
