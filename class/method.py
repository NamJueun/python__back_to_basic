from typing import ClassVar

# 일반 유닛
class Unit:
    def __init__(self, name, hp, damage):  # __init__ ->기본
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0}유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# 공격 유닛
class AttackUnit:
    def __init__(self, name, hp, damage):  # self는 __init__ 그 자체
        self.name = name # 파이어벳
        self.hp = hp # 50
        self.damage = damage # 16

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


# 파이어벳 유닛
firebat1 = AttackUnit("파이어벳",50,16)
firebat1.attack("5시") # self는 보낼 필요없음

# 공격 2번 받는다고 가정
firebat1.damaged(25)
firebat1.damaged(25)

