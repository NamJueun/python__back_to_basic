# 모듈: 함수집합


## 1. 
# import theater_module
# theater_module.price(3) # 3명이서 영화보러 같을 때 가격
# theater_module.price_morning(3) # 3명이서 조조 할인 영화보러 같을 때 가격
# theater_module.price_soldier(3) # 3명이서 군인 할인 영화보러 같을 때 가격

## 2. 단축명 줄여서 사용
# import theater_module as mv
# mv.price(3)
# mv.price_morning(3)
# mv.price_soldier(3)

## 3. theater_module 모듈을 모든 함수 사용할 수 있게함. 모듈명 필요없음
# from theater_module import *  
# price(3)
# price_morning(3)
# price_soldier(3)
  
## 4. 필요한 함수만 호출 
# from theater_module import price, price_morning, price_soldier
# price(3)
# price_morning(3)
# price_soldier(3) # 에러남

## 5. 함수에 별명 붙임
from theater_module import price_soldier as price 
price(3) # theater_price_soldier 호출