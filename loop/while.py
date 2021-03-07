# while
# customer = "토르"
# index = 5

# #while (조건) 조건 만족할 때 까지 반복


# while index >= 1:
#     print("{0}, 커피가 준비 되었습니다. {1}번 남았어요".format(customer,index))
#     index -= 1
#     if index == 0:
#         print("커피는 폐기처분되었습니다.")


# # 무한루프 ctrl + c  중지
# customer1 = "아이언맨"
# index1 = 1
# while True:
#     print("{0}, 커피가 준비 되었습니다. 호출 {1} 회".format(customer1,index1))
#     index1 += 1

customer2 = "토르"
person = "Unknown"

while person != customer2: # person이 내가 원하는 customer2가 아닐 떄
    print("{0}, 커피가 준비 되었습니다.".format(customer2))
    person = input("이름이 어떻게 되세요?")
    
    