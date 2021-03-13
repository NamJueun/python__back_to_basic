# 지역변수 local: 함수 내에서만 사용가능, 함수 호출될 때 만들어져 함수 기능 끝나면 사라짐 
# 전역변수 global: 모든 프로그램 내에서 사용가능, 권장하지는 않음

gun = 10   # 전역
 
def checkpoint(soldiers): # 경계근무
    global gun # 전역 공간에 있는 gun 사용 
    gun = gun - soldiers
    print("[함수 내] 남은 총: {0}".format(gun))

def checkpoint_ret(gun, soldiers): # 여기서 gun은 지연변수
    gun = gun - soldiers
    print("[함수 내] 남은 총: {0}".format(gun))
    return gun # 변화된 gun 값이 전달됨

print("전체 총: {0}".format(gun))
#checkpoint(2) #2명이 경계 근무 나감
gun = checkpoint_ret(gun, 2)
print("남은 총: {0}".format(gun))
