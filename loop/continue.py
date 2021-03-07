# continue, break

absent = [2,5] # 출석번호 2와 5가 결석함
# 결석한 학생들 빼고 책을 읽음
no_book = [7] #책을 깜빡했음
for student in range(1,11): # 1부터 10번까지 학생 있음
    if student in absent: 
        continue
    elif student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
        break
    print("{0}, 책을 읽어봐".format(student))
