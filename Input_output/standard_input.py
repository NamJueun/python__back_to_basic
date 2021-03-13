import sys
# print("Python", "Java", sep = ",", end = "?")
# print("무엇이 더 재미있을까요?")

# print("Python", "Java", file=sys.stdout) # 표준 출력
# print("Python", "Java", file=sys.stderr) # 표준 err

# 출력 포맷
# scores = {"수학":0, "영어":50, "코딩":100} # dict
# for subject, score in scores.items(): # items() -> key, value가 fair(튜플)로 나옴  
#     #print(subject,score)
#      print(subject.ljust(8),str(score).rjust(4), sep=":") # l/r just(n) n만큼 자리 확보해서 왼/오 쪽 정렬

# 은행 대기순번표
#001, 002 .... 
# for num in range(1, 21): #1부터 21 전까지 (20개)
#     print("대기번호 : " + str(num).zfill(3)) # zfill(n) #n개의 공간 확보 후 0 넣음

answer = input("아무 값이나 입력하세요: ")
print(type(answer))
#print("입력하신 값은 " + answer + "입니다.")