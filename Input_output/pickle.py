# 프로그램 상에서 사용하고 있는 데이터를 파일형태로 저장

import pickle

# file 쓰기

# profile_file = open("profile.pickle", "wb") # w"b" -> 피클 쓰려면 binary 정의 해야
# profile = {"이름" : "박명수", "나이" : 30, "취미": ["축구", "야구","코딩"]}
# print(profile)
# # 제일 중요. 피클로 파일에 씀
# pickle.dump(profile, profile_file) # profile에 있는 정보를 profile_file에 저장
# profile_file.close()

# file 읽기 

profile_file = open("profile.pickle","rb") 
profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close() 