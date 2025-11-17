# if문
weather = "비"
if weather == "비":
    print("우산을 생기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물 필요 없어요")

weather = input("오늘 날씨는 어때요? ")
if weather == "비":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물 필요 없어요")

temp = int(input("기온은 어때요? "))
if 30 <= temp:
    print("너무 더워요")
elif 10 <= temp and temp < 30:
    print("괜찮은 날씨에요")
elif 0 <= temp and temp < 10:
    print("외투를 챙기세요")
else:
    print("너무 추워요. 나가지 마세요")

# for문
for waiting_num in range(5): # 0부터 4까지
    print("대기번호: {0}".format(waiting_num))
starbucks = ["아이언맨", "토르", "그루트"]
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다.".format(customer))

# while문
customer = "토르"
index = 5
while index >= 1:
    print("{0}, 커피가 준비되었습니다. {1}번 남았어요." .format(customer, index))
    index -= 1
    if index == 0:
        print("커피가 폐기되었습니다.")

while True:
    print("{0}, 커피가 준비되었습니다. 호출 {1}번" .format(customer, index))
    index += 1

customer = "토르"
person = "Unknown"
while person != customer:
    print("{0}, 커피가 준비되었습니다." .format(customer))
    person = input("이름이 어떻게 되세요? ")

# continue / break
absent = [2,5]
for student in range(1, 11):
    if student in absent:
        continue # 밑의 문장 실행하지 않고 다음 loop로 넘어감
    print("{0}" .format(student))
no_book = [7]
for student in range(1, 11):
    if student in absent:
        continue # 밑의 문장 실행하지 않고 다음 loop로 넘어감
    elif student in no_book:
        print("no_book : {0}" .format(student))
        break # 반복문 탈출
    print("{0}" .format(student))

# 한 줄 for
students = [1,2,3,4,5]
print(students)
students = [i+100 for i in students] # student 하나씩 불러오면서 100을 더함
print(students)

students = ["Iron man", "Thor", "I am groot"]
students = [len(i) for i in students]
print(students)

students = ["Iron man", "Thor", "I am groot"]
students = [i.upper() for i in students]
print(students)

### 퀴즈 ###
from random import *
count = 0
for num in range(1, 51):
    time = randrange(5, 51)
    if 5 <= time <= 15:
        check = "O"
        count += 1
    else:
        check = " "
    print("[{0}] {1}번째 손님 (소요시간 : {2}분)" .format(check, num ,time))
    if num == 50:
        print("총 탑승 승객 : {0} 분" .format(count))