# Quiz) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨: 3명은 커피 쿠폰을 받게 됩니다.
# 추첨 프로그램을 작성하시오.

# 조건1: 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
# 조건2: 댓글 내용과 상관없이 무작위로 추첨하되 중복 불가
# 조건3: random 모듈의 shuffle과 sample을 활용 

# (출력 예제)
# -- 당첨자 발표 -- 
# 치킨 담당자: 1
# 커피 담당자: [2:3:4]
# -- 축하합니다. --

# (활용 예제)
from random import * 
import random
# lst = [1,2,3,4,5]
# print(lst)
# shuffle(lst) # 섞음
# print(lst)
# print(sample(lst: 1)) #list에서 n개를 무작위로 뽑음 

########################################## 내꺼 ##########################

# comment = {
#     1:"comment1",
#     2:"comment2",
#     3:"comment3",
#     4:"comment4",
#     5:"comment5",
#     6:"comment6",
#     7:"comment7",
#     8:"comment8",
#     9:"comment9",
#     10:"comment10", 
#     11:"comment11",
#     12:"comment12",
#     13:"comment13",
#     14:"comment14",
#     15:"comment15",
#     16:"comment16", 
#     17:"comment17", 
#     18:"comment18", 
#     19:"comment19", 
#     20:"comment20"      
# }

# #print(comment[1])
# keys = list(comment.keys())
# random.shuffle(keys)
# #print(keys)


# # (출력 예제)
# print("-- 당첨자 발표 --")

# #치킨
# for key1 in keys:
#  print(f"치킨 담당자: {key1}")
#  break

# random.shuffle(keys) 

# #커피
# for key2 in range(3):
#     print(keys[key2])
# print(" -- 축하합니다. -- ")

  


####################### 유튜브 #######

from random import *
users = range(1,21) # 1부터 20까지 숫자를 생성
#print(type(users)) # range
users = list(users) # range to list
#print(type(users)) # list

#print(users)
shuffle(users)
#print(users)

winners = sample(users,4) # 4명 중에서 1명은 치킨, 3명은 커피

print("-- 당첨자 발표 --")
print("치킨 담당자: {0}".format(winners[0]))
print("커피 담당자: {0}".format(winners[1:])) # 1,2,3 가져옴
print(" -- 축하합니다. --")
