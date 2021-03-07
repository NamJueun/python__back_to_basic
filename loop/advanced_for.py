# 한줄 for문

# 1. 출석번호가 1,2,3,4 앞에 100을 붙이기로 함 -> 101, 102, 103, 104
# students = [1,2,3,4,5]
# print(students)
# students = [i+100 for i in students] # students에 있는 값들을 가져와서 100을 더함
# print(students)

# 2. 학생 이름을 길이로 변환
# students = ["Iron man","Thor","I am groot"]
# students = [len(i) for i in students] # students에 있는 값을들 가져와서 len()에 넣음
# print(students)

# 3. 학생 이름을 대문자로 변환
students = ["Iron man","Thor","I am groot"]
students = [i.upper() for i in students]
print(students)