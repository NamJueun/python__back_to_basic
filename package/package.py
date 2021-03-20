# 1. 패키지: 하나의 디렉토리 안의 모듈 집합

## 방법 1
    # import travel.thailand # module, package만 가능 
    #                         # class, 함수는 import 직접 할 수 없음
    #                         # import travel.thailand.ThailandPackage() -> 불가능
    # trip_to = travel.thailand.ThailandPackage()
    # trip_to.detail()

## 방법 2
    # from travel.thailand import ThailandPackage
    # trip_to = ThailandPackage()
    # trip_to.detail()

# from travel import vietnam # travel package에서 모듈 vietnam를 import 
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()


# 2. __all__
from travel import *  # travel 패키지 안에 있는 모든 걸 가져오지만, 공개 범위에 따라 다름 -> __init__ 으로 공개범위 설정
# #trip_to = vietnam.VietnamPackage()
trip_to = thailand.ThailandPackage()
trip_to.detail()

## 3. 모듈, 패키지의 위치 확인
import inspect 
import random
from travel import thailand 
print(inspect.getfile(random))
print(inspect.getfile(thailand))
