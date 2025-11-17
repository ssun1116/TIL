# 표준입출력
print("python", "java", sep = "_")
print("python", "java", sep = " vs ", end = "?\n")

import sys
print("python", "java", file = sys.stdout) # 표준 출력으로 문장 찍힘
print("python", "java", file = sys.stderr) # 표준 에러로 처리됨 (수정 필요하도록 로깅 / 추적에 좋다)

scores = {"수학" : 0, "영어" : 50, "코딩" : 100}
for subject, score in scores.items():
    #print(subject, score)
    print(subject.ljust(5), str(score).rjust(6), sep = ":") # 숫자 정렬 편집하는 옵션

# 은행 대기순번표
# 001, 002, 003, ...
for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3)) # 0XX 형식으로 숫자를 출력

answer = input("아무 값이나 입력하세요 : ") # 사람을 통해서 입력된 값 : 무조건 문자로 전달된다.
print(type(answer)) # answer = 10 (numeric) 이었어도 str이라고 뜸.

## 출력 포맷
# 빈 자리는 빈 공간으로 두고 오른쪽 정렬하되, 총 10자리 공간을 확보하는 문장.
print("{0: >10}".format(500)) # 10칸 중 오른쪽부터 숫자를 채우고 나머지 앞칸은 비어있음.
# 숫자의 부호를 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))
# 왼쪽 정렬하고, 빈칸을 _로 채움.
print("{0:_<+10}".format(500))
print("{0:_<10}".format(500))
# 큰 숫자 -> 세자리마다 ,를 찍어주기
print("{0:,}".format(10000000000))
# 세자리마다 ,를 찍어주고 부호도 표기
print("{0:+,}".format(10000000000))
# 세자리마다 ,를 찍어주고 부호도 표기, 자릿수도 확보, 빈자리는 ^로 채우기
print("{0:^<+30,}".format(10000000000))
# 소수점 출력
print("{0:f}".format(5/3))
# 소수점을 특정 자리까지만 표기
print("{0:.2f}".format(5/3)) # 소수점 둘째자리까지 표기 -> 셋째 자리에서 반올림.

## 파일 입출력
score_file = open("score.txt", "w", encoding = "utf8") # 쓰기 용도
print("수학 : 0", file = score_file)
print("영어 : 50", file = score_file)
score_file.close()

score_file = open("score.txt", "a") # 뒤에 이어 쓰기. 
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")
score_file.close()

score_file = open("score.txt", "r") # read
print(score_file.read())
score_file.close()

score_file = open("score.txt", "r")
print(score_file.readline()) # 한줄 읽고 커서는 다음 줄로 이동
print(score_file.readline()) # 다음 줄이 출력됨
print(score_file.readline())
print(score_file.readline())
score_file.close()

score_file = open("score.txt", "r", encoding = "utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end = "")
score_file.close()

score_file = open("score.txt", "r", encoding = "utf8")
lines = score_file.readlines() # list 형태로 저장하기
for line in lines:
    print(line, end = "")

## pickle : 사용하는 데이터를 파일 형태로 저장.
import pickle
profile_file = open("profile.pickle", "wb") # wb : binary write.
profile = {"name" : "abc", "age" : 30, "hobby" : ["soccer", "golf", "coding"]}
print(profile)
pickle.dump(profile, profile_file) # profile에 있는 정보를 profile_file에 저장
profile_file.close()

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file)
print(profile)

## with
import pickle 
with open("profile.pickle", "rb") as profile_file: # pickle 파일을 열어서 profile_file이라는 변수로 저장
    print(pickle.load(profile_file)) # close할 필요 없이 with 내에서 자동 종료.

with open("study.txt", "w", encoding = "utf8") as study_file:
    study_file.write("python studying") # close 없이 파일 작성 완료됨.

with open("study.txt", "r") as study_file:
    print(study_file.read())

## 퀴즈 7
for weeks in range(1,4):
    with open(str(weeks) + "주차.txt", "w", encoding = "utf8") as report_file:
        report_file.write(" - {0} 주차 주간보고 - " .format(weeks))
        report_file.write("\n부서 :")
        report_file.write("\n이름 :")
        report_file.write("\n업무 요약 :")