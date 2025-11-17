## 전달값과 반환값 

def open_account():
    print("새로운 계좌가 생성되었습니다.")

open_account()

def deposit(balance, money): # 입금
    print("입금이 완료되었습니다. 잔액은 {0} 원입니다." .format(balance + money))
    return balance + money

balance = 0 # 잔액
balance = deposit(balance, 1000)
print(balance)

def withdraw(balance, money): # 출금
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {0}원입니다." .format(balance - money))
        return (balance - money)
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다." .format(balance))
        return balance

balance = 0
balance = deposit(balance, 1000)
balance = withdraw(balance, 2000)
balance = withdraw(balance, 500)
balance = deposit(balance, 1500)

def withdraw_night(balance, money): # 저녁에 출금
    commission = 100 # 수수료 100원
    return commission, balance - money - commission

commission, balance = withdraw_night(balance, 500)
print("수수료는 {0}원이며, 잔액은 {1} 원입니다." .format(commission, balance))

# 기본값
def profile(name, age, main_lang):
    print("이름: {0}\t나이 : {1}\t주 사용 언어: {2}" .format(name, age, main_lang))

profile("유재석", 20, "파이썬")
profile("김태호", 25, "자바")

def profile(name, age = 17, main_lang = "파이썬"): # 기본값 전달.
    print("이름: {0}\t나이 : {1}\t주 사용 언어: {2}" .format(name, age, main_lang))

profile("유재석") # 나이, main_lang 안써도 알아서 기본값으로 출력됨

## 키워드값
def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name = "유재석", main_lang = "파이썬", age = 20)

# 가변인자
def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름 : {0}\t 나이 : {1}\t" .format(name, age), end = " ") # end : 프린트문 끝날 때 줄바꿈 대신 " " 출력으로 끝.
    print(lang1, lang2, lang3, lang4, lang5)

profile("유재석", 20, "Python", "Java", "C", "C++", "C#") # 만약 할 줄 아는 언어가 더 많을 경우?
profile("김태호", 25, "Kotlin", "Swift", "", "", "") # 할 수 있는 게 두 개 뿐인 경우 매번 빈칸으로 써야하나?

def profile(name, age, *language): # *language: 넣고 싶은 만큼 language를 넣을 수 있다. 서로 다른 개수의 인자 넣을 때.
    print("이름 : {0}\t 나이 : {1}\t" .format(name, age), end = " ") # end : 프린트문 끝날 때 줄바꿈 대신 " " 출력으로 끝.
    for lang in language:
        print(lang, end = " ")
    print()

profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "R") # 여러 개 모두 출력됨.
profile("김태호", 25, "Kotlin", "Swift") # 두 개도 잘 출력됨.

# 지역변수와 전역변수 (함수 내에서만 쓸 수 있는 것 / 프로그램 내 어느 공간에서든 쓸 수 있는 것)
gun = 10
def checkpoint(soldiers):
    gun = gun - soldiers
    print(gun) 
print(gun) # 10으로 출력됨.
checkpoint(3) # 오류 : local variable 'gun' referenced before assignment (할당 없이 사용되었다. 함수 내에서 사용되는 gun)

def checkpoint(soldiers):
    gun = 10
    gun = gun - soldiers
    print(gun) 
checkpoint(3) # 함수 내에서 gun을 선언하니 출력됨. gun 전역변수는 함수 내에서 쓰이지 않는다. 함수 내 : 지역변수.

def checkpoint(soldiers):
    global gun
    gun = gun - soldiers
    print(gun) 
checkpoint(3) # gun : 전역변수를 함수 내에서 쓰게 됨. global. but 사용이 권장되지는 않는다. 가급적 parameter 쓰기.

def checkpoint_return(gun, soldiers):
    gun = gun - soldiers
    print(gun)
    return gun

gun = checkpoint_return(10, 3) # 변경된 값이 gun에 return됨
gun

## 퀴즈

def std_weight(height, gender):
    if gender == "남자":
        return height * height * 22
    else :
        return height * height * 21

height = 175
gender = "남자"

print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다." .format(height, gender, round(std_weight(height/100, gender), 2)))
