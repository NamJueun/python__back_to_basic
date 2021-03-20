# package 설치하기

from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())


# pip list : 다운로드 되어 있는 패키지 리스트 
# pip show beautifulsoup4 : 해당 패키지 정보 알려줌
# pip install --upgrade beautifulsoup4 : 최신 버전로 업그레이드 
# pip uninstall 패키지명 : 패키지 삭제