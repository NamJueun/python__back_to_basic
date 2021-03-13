# 가변인자: 서로 다른 개수 값을 넣어줄 떄 가변인자 (*) 
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름: {0}\t나이: {1}\t".format(name, age), end=" ") # 문장 끝날 때 다음 문장 줄바꿈 없이 이어서 입력됨
#     print(lang1,lang2,lang3,lang4,lang5)

def profile(name, age, *language):
    print("이름: {0}\t나이: {1}\t".format(name, age), end=" ") # 문장 끝날 때 다음 문장 줄바꿈 없이 이어서 입력됨
    for lang in language:
        print(lang, end=" ")
    print()

profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "JS")
profile("김태호", 25, "Kotlin", "Swift")