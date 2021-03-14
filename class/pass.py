
###### 지상유닛######

# 일반 유닛
class Unit:  # 부모 클래스
    def __init__(self, name, hp, speed):  # __init__ ->기본
        self.name = name  # 겹치는 부분1
        self.hp = hp     # 겹치는 부분2
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이름]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(
            self.name, location, self.speed))

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
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# ------------------------------------------------------------------------
## pass

# 건물
# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         pass

# # 서플라이 디폿: 건물, 1개 건물 = 8 유닛 생성가능
# supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")

# def game_over():
#     pass

# game_start()
# game_over()

#----------------------------------------------
# super

# 건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        # 방법 1 (super x)
        # Unit.__init__(self, name, hp, 0)  # 건물은 이동 못하니까 스피드 0   

        # 방법 2 (super o)
        super().__init__(name, hp, 0)  # self 필요없음
        
        self.location = location
