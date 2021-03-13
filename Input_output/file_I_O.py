# 파일 입출력

# file 쓰기
# 덮어쓰기
score_file = open("score.txt", "w", encoding="utf8") # w -> write(덮어쓰기)  ------- 파일 열기
print("수학: 0" , file = score_file)
print("영어: 50", file = score_file)
score_file.close()                                                #--------파일 닫기 (필수) 

# 이어쓰기
score_file = open("score.txt","a",encoding="utf-8") # a -> append(이어쓰기)
score_file.write("과학: 80")
score_file.write("\n코딩: 100")
score_file.close()

# file 읽기

    # 전부 가져오기
score_file=open("score.txt", "r", encoding= "utf-8") # r -> read
print(score_file.read()) 
score_file.close()

    # 한줄씩 가져오기
score_file=open("score.txt", "r", encoding= "utf-8") # r -> read
print(score_file.readline())  # 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline())  
print(score_file.readline())  
print(score_file.readline(), end="") # 줄바꿈 안함
score_file.close()

    # 몇 줄인지 모를 때
score_file = open("score.txt","r",encoding="utf-8")
while True:
    line = score_file.readline()
    if not line: # 읽어온 라인 없을 때
        break
    print(line, end = "")
score_file.close()

    # list로 가져오기
score_file = open("score.txt", "r", encoding="utf-8")
lines = score_file.readlines() # list 형태로 저장
for line in lines:
    print(line, end="")
score_file.close()