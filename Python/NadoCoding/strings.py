# 슬라이싱
jumin = "991116-1234567"
jumin[0:6] # 몇번째까지 : 실제 자리보다 1 더해야함
jumin[6] # 실제로 6번째는 -
print("성별: " + jumin[7]) # 1
print("연: " + jumin[0:2]) # 99
print("월: " + jumin[2:4]) # 11
print("일: " + jumin[4:6]) # 16

print("뒤 7자리 뒤에부터: " + jumin[-7:0]) # 1234567

# 문자열 처리 함수
python = "Python is Amaizing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n") # 첫번째 n을 찾음
print(index)
index = python.index("n", index + 1) # index + 1 : start position. 6번쩨 자리부터 찾는다.
print(index)
print(python.find("n"))
print(python.find("Java")) # 없음 : -1
print(python.index("Java")) # 없음 : Error.
print(python.count("n")) # n이 몇번 등장하는지.

# 문자열 포맷
print("a" + "b") # ab - 붙임
print("a", "b") # a b - 띄어쓰기
## 방법 1
print("나는 %d살입니다." % 20) # integer
print("나는 %s를 좋아해요." % "python") # string
print("Apple 은 %c로 시작해요" % "A") # character
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간")) # 괄호의 값들이 순서대로 들어감.
## 방법 2
print("나는 {}살입니다." .format(20)) # .format() 내의 값을 {}에 투입
print("나는 {}색과 {}색을 좋아해요." .format("파란", "빨간")) # 괄호의 값들이 순서대로 들어감.
print("나는 {1}색과 {0}색을 좋아해요." .format("파란", "빨간")) # 중괄호 숫자에 따라 값이 오는 순서 결정.
# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요." .format(age = 20, color = "빨간")) # 중괄호 안에 변수 사용.
print("나는 {age}살이며, {color}색을 좋아해요." .format(color = "빨간", age = 20)) # 중괄호 안에 변수 사용.
# 방법 4 (v.3.6 이상)
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.") # 중괄호 내 값을 실제 변수에서 사용된 값 사용.

# 탈출문자
print("백문이 불여일견\n백견이 불여일타")
print("저는 '나도코딩'입니다.")
print("저는 \"나도코딩\"입니다.") # "" 내에서 ""를 출력 가능.
# \\ : 문장 내에서 하나의 \로 출력.

## 퀴즈 3.
url = "http://naver.com"
my_str = url.replace("http://", "") # 규칙 1
print(my_str) # naver.com
#index = my_str.find(".")
#my_str2 = my_str[:index]
my_str2 = my_str[:my_str.index(".")] # 규칙 2
print(my_str2) # naver

#length = len(my_str2)
#print(my_str2[:3] + length + my_str2.count("e") + "!")
#print(my_str2[:3] + length)

password = my_str2[:3] + str(len(my_str2)) + str(my_str2.count("e")) + "!" # 규칙 3
print("{0}의 비밀번호는 {1}입니다." .format(url, password))
