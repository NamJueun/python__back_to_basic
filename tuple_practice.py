# 튜플: 
# * 리스트랑 다르게 내용 변경, 추가 불가
# * 속도가 리스트보다 빠르기 때문에 불면의 리스트 이용할 때 사용

menu = ("돈까스", "치즈가쓰")
print(menu[0])
print(menu[1])

#추가
#menu.add("생선가쓰") # error 추가, 변경불가

#-----------------------------
name = "김종국"
age = 20
hobby = "코딩"
print(name, age, hobby)

#   -> 
(name, age, hobby) = ("김종국, 20, 코딩")
print(name, age, hobby)