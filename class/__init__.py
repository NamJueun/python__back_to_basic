# 1. __init__ 
# : python에서 쓰이는 생성자, 객체가 만들어 질때 자동으로 호출됨. 클래스로 부터 만들어 지는 거 -> 객체

class Unit:
    def __init__(self,name,hp,damage):  # __init__ ->기본
        self.name = name  
        self.hp = hp
        self.damage = damage
        print("{0}유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린2", 40, 5)
# tank = Unit("탱크", 150,35)
# marine2 = Unit("마린2", 40, 5) # Unit에서 정의된 인수 개수에 맞게 넣어야함

# ---------------------------------------------------------------------

# 2. 멤버변수
# : 클래스 내에서 정의된 변수

# 레이스 유닛
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름: {0} 공격력 {1}".format(wraith1.name, wraith1.damage))

# 레이스 유닛3
wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True  # 클래스 외부에서 객체 추가

if wraith1.clocking == True:
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))


