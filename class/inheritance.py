# 1. 상속 (클래스 하나만 상속받음)

# 일반 유닛
class Unit:  # 부모 클래스
    def __init__(self, name, hp):  # __init__ ->기본
        self.name = name  # 겹치는 부분1
        self.hp = hp     # 겹치는 부분2

# 공격 유닛


class AttackUnit(Unit):  # 자식 클래스
    # 일반 유닛을 상속받음 -> 겹치는 부분 지워도 되는 거임
    def __init__(self, name, hp, damage):  # self는 __init__ 그 자체
        #self.name = name # 겹치는 부분1
        #self.hp = hp     # 겹치는 부분2

        # 유닛에서 만들어진 생성자 불러서 이름과 hp 생성가능
        Unit.__init__(self, name, hp)
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

# 2. 다중상속 (클래스 여러개 상속받음)

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0}:{1}방향으로 날아갑니다. [속도 {2}]".format(
            name, location, self.flying_speed))

# 공중 공격 클래스
class FlyableAttackUnit(AttackUnit, Flyable): # 두개 클래스를 상속받아서 초기화함
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)

# 발키리 유닛: 공중 공격 유닛
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly("발키리", "3시")

