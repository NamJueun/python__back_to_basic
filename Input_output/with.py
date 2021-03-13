# close 필요없음

## pickle 이용
# import pickle 

# with open("proflie.pickle", "rb") as profile_files: # 피클파일의 정보를 profile_files 변수로 가져옴
#     print(pickle.load(profile_files)) 

## pickle 이용하지 않음 -> close 필요없음

    # 쓰기
# with open("study.txt", "w", encoding="utf-8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")

    # 읽기
with open("study.txt", "r", encoding ="utf-8") as study_file:
    print(study_file.read())
