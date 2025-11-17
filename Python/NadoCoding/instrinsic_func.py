## 내장함수 : import 없이 바로 사용가능한 함수.

# input : 사용자 입력을 받는 함수
langauge = input("무슨 언어를 좋아하세요?")
print("{0}은 아주 좋은 언어입니다!" .format(langauge))

# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
print(dir())
import random
print(dir())

print(dir(random)) # 랜덤 모듈 내에서 쓸 수 있는 함수들.

lst = [1,2,3]
print(dir(lst)) # 리스트에 대해서 쓸 수 있는 함수들.


## 외장함수 : import를 통해서 사용 가능한 함수.
# glob : 경로 내의 폴더 / 파일 목록을 조회. 
import glob
print(glob.glob("*.py")) # 확장자가 py인 모든 파일

# os : 운영체제에서 제공하는 기본 기능
import os
print(os.getcwd()) # 현재 디렉토리 출력

folder = "sample_dir"
if os.path.exists(folder): # "sample_dir" 폴더가 있는 경우
    print("이미 존재하는 폴더입니다.")
    os.rmdir(folder)
    print(folder, "폴더를 삭제하였습니다.")
else:
    print("폴더를 생성합니다.")
    os.makedirs(folder)

print(os.listdir()) # 현 디렉토리의 파일 출력

# time : 시간 관련 함수
import time
print(time.localtime())
print(time.strftime("%y-%m-%d %H:%M:%S"))

import datetime
print("오늘 날짜는", datetime.date.today(), "입니다.")

# timedelta : 두 날짜 사이의 간격
today = datetime.date.today()
td = datetime.timedelta(days = 100)
print(today + td) # today + 100일 후

