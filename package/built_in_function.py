## 1. 내장함수 

# input : 사용자 입력을 받는 함수
#language = input("좋아하는 언어: ")

# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
# print(dir())
#import random # 외장함수
# print(dir())
# import pickle
# print(dir())

# print(dir(random))
# "random." 찍었을 때랑 같음

# lst = [1,2,3]
# print(dir(lst))

# name = "Jim"
# print(dir(name))


## 2. 외장함수 

# glob : 경로 내의 폴더, 파일을 목록 조회 (윈도우 dir)
# import glob
# print(glob.glob("*.py")) # 확장자가 py인 모든 파일

# os : 운영체제에서 제공하는 기본 기능 ex) 폴더 생성, 삭제
#import os
# print(os.getcwd()) # 현재 디렉토리

# folder = "sample.dir"

# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder)
#     print("폴더 삭제")
# else:
#     os.makedirs(folder) # 폴더 생성
#     print(folder,"폴더 생성")

#print(os.listdir())

# time : 시간 관련 함수
# import time
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:$M:$S"))

# datetime
import datetime
print(datetime.date.today())

# timedelta : 두 날짜 사이의 간격
today = datetime.date.today() # 오늘 날짜 지정
td = datetime.timedelta(days = 100 ) # 오늘로 부터 100일 뒤

print("오늘부터 100일 후는: " today + td)