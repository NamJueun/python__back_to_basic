# dict

cabinet = {3:"유재석",100:"김태호"}
print(cabinet[3])
print(cabinet.get(3))

print(cabinet[5]) # 에러
print(cabinet.get(5)) # none
print(cabinet.get(5), "사용가능") # none이면 "사용가능"을 입력

print(3 in cabinet) # cabinet에 3이라는 키가 있나 # True
print(5 in cabinet) # False


# list로 사전 가져오기
cabinet ={
    "A-3":"유재석",
    "B-100":"김태호"
    }

print(cabinet["A-3"]) # 유재석
print(cabinet["B-100"]) # 김태호

#새손님
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

# 간 손님
del cabinet["A-3"]
print(cabinet)

# key만 출력
print(cabinet.keys())

# value만 출력
print(cabinet.values())

# key, value 출력
print(cabinet.items())

# 모두 지움
cabinet.clear()
print(cabinet)