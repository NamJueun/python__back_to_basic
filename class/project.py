from random import *
###### 지상유닛######

# 일반 유닛
class Unit:  # 부모 클래스
    def __init__(self, name, hp, speed):  # __init__ ->기본
        self.name = name  # 겹치는 부분1
        self.hp = hp     # 겹치는 부분2
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(name))
        # self.name -> 매개변수
        # name -> 파라매터

    def move(self, location):
        #print("[지상 유닛 이름]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(
            self.name, location, self.speed))

    def damaged(self, damage):
        print("{0}:{1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        # self.hp = self.hp - damage
        print("{0}: 현재체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0}: 파괴되었습니다.".format(self.name))

# 공격 유닛


class AttackUnit(Unit):  # 자식 클래스
    # 일반 유닛을 상속받음 -> 겹치는 부분 지워도 되는 거임
    def __init__(self, name, hp, speed, damage):  # self는 __init__ 그 자체
        #self.name = name # 겹치는 부분1
        #self.hp = hp     # 겹치는 부분2

        # 유닛에서 만들어진 생성자 불러서 이름과 hp 생성가능
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    # method 1
    def attack(self, location):
        print("{0}:{1}방향으로 적군을 공격합니다. [공격력 {2}]"
              .format(self.name, location, self.damage))
    # method 2

    def damaged(self, damage):
        print("{0}:{1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        # self.hp = self.hp - damage
        print("{0}: 현재체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0}: 파괴되었습니다.".format(self.name))


class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)  # self/name/hp/speed/damage

    # 스팀팩: 일정 시간 동안 체력 10 써서 이동 및 공격 속도 up
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. [HP 10 감소]".format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))


class Tank(AttackUnit):
    # 시즈모드 : 탱크를 지상에 고정시켜, 더 강한 파워로 공격가능. 이동불가
    seize_developed = False  # 시즈모드 개발여부

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return

        # 현재 시즈모드 아닐 떄 -> 시즈모드
        if Tank.seize_mode == False:
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.seize_mode = True
        # 현재 시즈모드 일때  -> 모드 해제
        else:
            print("{0} : 시즈모드로 해제합니다..".format(self.name))
            self.damage /= 2
            self.seize_mode = False


###### 공중 유닛 ######

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0}:{1}방향으로 날아갑니다. [속도 {2}]".format(
            name, location, self.flying_speed))


# 공중 공격 클래스
class FlyableAttackUnit(AttackUnit, Flyable):  # 두개 클래스를 상속받아서 초기화함
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)  # 지상 speed 0
        Flyable.__init__(self, flying_speed)

    ## 지상유닛 move 메소드, 공중유닛 fly 메소드 매번 다르게 쓰기 귀찮으니까, 새로 정의함
    def move(self, location):
       # print("[공중 유닛 이동]")
        self.fly(self.name, location)

# 레이스


class Wraith(FlyableAttackUnit):
    def __init__(self):
        # self,name, hp, damage, flying_speed
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False  # 클로킹 모드 (해제 상태)

    def clocking(self):
        if self.clocked == True:  # 클로킹 모드 -> 모드 해제
            print("{0} : 클로킹 모드 해제합니다.".format(self.name))
            self.clocked == False
        else:
            print("{0} : 클로킹 모드 설정합니다.".format(self.name))
            self.clocked == True


def game_start():
    print("[알림] 새로운 게임을 시작합니다.")
    
def game_over():
    print("Player : gg ") 
    print("[Player] 님이 게임에서 퇴장했습니다.")    


# 게임 실행
game_start()

    ## 지상 유닛
# 마린 3기 생성
m1 = Marine()
m2 = Marine()
m3 = Marine()

# 탱크 2기 생성
t1 = Tank()
t2 = Tank()

    ## 공중 유닛
# 레이스 1기 생성
w1 = Wraith()


# 유닛 일괄 관리 (생성된 모든 유닛 append)
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

# 전군 이동
for unit in attack_units:
    unit.move("1시")

# 탱크 시즈 모드 개발
Tank.seize_developed == True
print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

# 공격 모드 준비(마린 : 스팀팩, 탱크: 시즈모드, 레이스: 클로킹 모드)
for unit in attack_units:
    if isinstance(unit, Marine):  # isinstance : 객체가 어떤 클래스의 인스턴스인지 체크
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit,Wraith):
        unit.clocking()
    
# 전군 공격
for unit in attack_units:
    unit.attack("1시")

# 전군 피해
for unit in attack_units:
    unit.damaged(randint(5,20)) # 5~20 사이의 랜덤 공격 받음

# 게임 종료
game_over()
