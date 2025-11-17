# 리스트
subway = [10, 20, 30]
print(subway)
subway = ["유재석", "조세호", "박명수"]
print(subway)
print(subway.index("조세호"))
subway.append("하하")
print(subway)
subway.insert(1, "정형돈")
print(subway) # 정형돈 끼워넣기
print(subway.pop())
print(subway)
print(subway.pop(2))

subway.append("유재석")
print(subway)
print(subway.count("유재석")) # 같은 이름의 사람이 몇 명인지 확인
print(subway.index("유재석", 1))

num_list = [5, 2, 4, 3, 1]
num_list.sort() # 정렬도 가능
print(num_list)
num_list.reverse() # 순서 뒤집기도 가능
print(num_list)

num_list.clear() # 모두 지우기
print(num_list)

# 리스트 -> 다양한 자료형을 함께 사용 가능
mix_list = ["조세호", 20, True]
print(mix_list)
num_list = [5, 2, 4, 3, 1]
num_list.extend(mix_list) # 리스트 확장
print(num_list)

# 사전
cabinet = {3:"유재석", 100:"김태호"} # 딕셔너리 -> A:B 구조
print(cabinet[3])
print(cabinet[100])
print(cabinet.get(3)) # 대괄호 쓰기의 다른 방법.
print(cabinet[5]) # 5가 없어서 error 뜸.
print(cabinet.get(5)) # None 이라고 뜸 (error 아님)
print(cabinet.get(5, "사용 가능")) # None 대신 내가 지정한 문자를 출력함.

print(3 in cabinet) # True
print(5 in cabinet) # False

cabinet[20] = "정준하" # 딕셔너리 값을 추가.
print(cabinet)

del cabinet[3] # 딕셔너리 값을 지움.
print(cabinet)

print(cabinet.keys()) # key들만 출력
print(cabinet.values()) # value들만 출력
print(cabinet.items()) # key, value를 쌍으로 출력

cabinet.clear() # 딕셔너리 내 값을 지움.
print(cabinet)

# 튜플 -> 내용 변경/추가 못함. 속도는 리스트보다 빠르다.
menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])
menu.append("생선까스") # 튜플은 추가 못함.

(name, age, hobby) = ("김종국", 20, "코딩") # 튜플로 값을 한번에 선언.
print(name, age, hobby)

# 집합 (set) -> 중복 안됨, 순서 없음
my_set = {1, 2, 3, 3, 3}
print(my_set)
java = {"유재석", "김태호", "양세형"} # 중괄호를 가지고 set를 만들 수 있음.
python = set(["유재석", "박명수"]) # 리스트를 가지고 set를 만들 수 있음.
print(java & python) # 교집합
print(java.intersection(python))
print(java | python) # 합집합
print(java.union(python))
print(java - python)
print(java.difference(python))
python.add("김태호")
print(python)
java.remove("김태호")

# 자료구조의 변경
menu = {"커피", "우유", "주스"}
print(menu, type(menu)) # class 'set'
menu = list(menu)
print(menu, type(menu))
menu = tuple(menu)
print(menu, type(menu))
menu = set(menu)
print(menu, type(menu))

### 퀴즈 ###
from random import *
#lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
lst = range(1, 21) # 1부터 20까지 숫자를 생성
print(lst, type(lst))
lst = list(lst) # list형으로 변환
print(lst, type(lst))

shuffle(lst)
print(lst)

winner = sample(lst, 4)
print("치킨 당첨자: {0}".format(winner[0]))
print("커피 당첨자: {0}".format(winner[1:4]))

