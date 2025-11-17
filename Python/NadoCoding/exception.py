# 예외처리
print("나누기 전용 계산기입니다.")
num1 = int(input("첫 번째 숫자를 입력하세요 : "))
num2 = int(input("두 번째 숫자를 입력하세요 : "))
print("{0} / {1} = {2}" .format(num1, num2, int(num1/num2)))

try:
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
    #nums.append(int(nums[0]/nums[1]))
    print("{0} / {1} = {2}" .format(nums[0], nums[1], nums[2]))
except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.") # try 내에서 문제 발생시 except를 찾아서 오류에 해당하는 부분을 출력.
except ZeroDivisionError as err:
    print(err)
except Exception as err:
    print("알 수 없는 에러가 발생하였습니다.")

# 에러 발생시키기
try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise ValueError
    print("{0} / {1} = {2}" .format(num1, num2, int(num1/num2)))
except ValueError:
    print("에러! 잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.") # try 내에서 문제 발생시 except를 찾아서 오류에 해당하는 부분을 출력.
except ZeroDivisionError as err:
    print(err)
except Exception as err:
    print("알 수 없는 에러가 발생하였습니다.")

# 사용자 정의 예외처리
class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("입력값 : {0}, {1}" .format(num1, num2))
    print("{0} / {1} = {2}" .format(num1, num2, int(num1/num2)))
except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.") # try 내에서 문제 발생시 except를 찾아서 오류에 해당하는 부분을 출력.
except ZeroDivisionError as err:
    print("에러!" + err)
except BigNumberError as err:
    print(err)
    print("에러 ! 한 자리 숫자만 입력하세요.")

# finally : 예외처리 구문에서 오류에 상관없이 무조건 실행.

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("입력값 : {0}, {1}" .format(num1, num2))
    print("{0} / {1} = {2}" .format(num1, num2, int(num1/num2)))
except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.") # try 내에서 문제 발생시 except를 찾아서 오류에 해당하는 부분을 출력.
except ZeroDivisionError as err:
    print("에러!" + err)
except BigNumberError as err:
    print(err)
    print("에러 ! 한 자리 숫자만 입력하세요.")
finally:
    print("계산기를 이용해 주셔서 감사합니다.")



## 퀴즈
chicken = 10
waiting = 1

class SoldOutError(Exception):
    pass

while (True):
    try:
        print("[남은 치킨 : {0}]" .format(chicken))
        order = int(input("치킨 몇 마리 주문하시겠습니까?"))
        if order > chicken:
            print("재료가 부족합니다.")
        elif order < 1:
            raise ValueError
        else:
            print("[대기번호 {0}] {1}마리 주문이 완료되었습니다." .format(waiting, order))
            waiting += 13
            chicken -= order
        if chicken == 0:
            raise SoldOutError
    except ValueError:
        print("잘못된 값을 입력하였습니다.")
    except SoldOutError:
        print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
        break
    finally:
        print("치킨집 영업 종료")