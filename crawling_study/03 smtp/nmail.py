import smtplib
from email.mime.text import MIMEText

sendEmail = "네이버ID@naver.com"
recvEmail = "받는 이메일"
password ="네이버 비밀번호"

smtpName = "smtp.naver.com" #smtp 서버 주소
smtpPort =587 #smtp 포트 번호

text ="Email content"
msg = MIMEText(text) #MIMEText(text, _charset = "utf8")
#편지 봉투 생성

msg['Subject']="This is the Email subject"
msg['From']=sendEmail
msg['To']=recvEmail
#편지 보낼 곳 적음
print(msg.as_string())

s=smtplib.SMTP( smtpName , smtpPort ) #메일 서버 연결
s.starttls() #TLS보안 처리
s.login( sendEmail , password )  # 로그인
s.sendmail( sendEmail, recvEmail, msg.as_string() ) #메일 전송, 문자열로 반환
# 사실상 우체국을 통해 접수 후 배송되는 과정

s.close() #smtp 서버 연결을 종료
