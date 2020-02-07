from selenium import webdriver

driver = webdriver.Chrome('chromedriver')
driver.get('http://zzzscore.com/1to50')
driver.implicitly_wait(300)

#전역변수
#현재 찾아야될 숫자
num=1

def clickBtn():
    global num #num을 전역변수로 바꿈
    btns = driver.find_elements_by_xpath('//*[@id="grid"]/div[*]')
    # '*'은 모든 값이 들어갈 수 있다.
    # print(len(btns))

    # print(btns[0].text) #첫번째 값을 출력

    for btn in btns:
        print(btn.text, end='\t')
        if btn.text==str(num): #그냥 num쓰면 안눌림-문자가 아니어서
            btn.click()
            print(True)
            num+=1
            return

##메인코드
while num<=50:
    clickBtn()