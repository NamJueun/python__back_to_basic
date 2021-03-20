# 1. 에러 발생시키기
# 2. 사용자 정의 예외처리
# 3. finally: 에외 처리 구문중 정상처리/에러처리 무슨 결과든 무조건 실행됨

class BigNumberError(Exception): # 2. 사용자 정의 예외처리
    def __init__(self,msg):
        self.msg= msg

    def __str__(self):
        return self.msg

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요: "))
    num2 = int(input("두 번째 숫자를 입력하세요: "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("입력값: {0}, {1}".format(num1,num2)) # 1. 에러 발생시키기
    print("{0} / {1} = {2}".format(num1,num2,int(num1/num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
except BigNumberError as err:
    print("BigNumberError")
    print(err)
finally:
    print("thanks")