output = ""

# for i in range(1,10):
#     for j in range(0,i):
#         output += "*"
#     output += "\n"

# print(output)



# for i in range(1,10):
#     i = i += 1
#     print(i)


# for i in range(1,6):
# for i in range(1, 6):
#     for j in range(i + 1):
#         print(i, end='')
#     print()

# for i in range(1,6):
#     for j in range(i+1):
#         print("A", end='')
# #     print()

# for i in range(1,6):
#     for j in range(i + 1):
#         print(i, end = '')
#     print()

# for i in range(1,6):
#     for j in range(i + 1):
#         print(i, end='')
#     print()


# a = ' '
# for i in range(0,6):
#     for j in range(0, i):
#         print("*", end='')
#     print()

# i = 0
# while 1 <10:
#     print("{}번쨰 반복입니다".format(i))
#     i += 1

# list_test = [1,2,1,2]
# value = 2

# while value in list_test:
#     list_test.remove(value)

# print(list_test)

# i = 0
# while True:
#     print("{}번째 반복문입니다.".format(i))
#     i = i +1
#     input("종료하시겠습니까?")
#     if input in ['y', 'Y']:
#         print ("반복을 종료합니다")
#         break

# numbers = [5,15, 6, 20, 7, 25]
# for number in numbers:
#     if number < 10:
#         continue
#     print(number)

# 4,5
# # 7654321
# # 3,10,3

# # -----------

# character = {"name":"기사", "hp":200, "mp":30}
# # print(character)

# list = ["요소A", "요소B", "요소C"]
# i = 0
# for item in list:
#     print("{}번째 요소는 {}입니다.".format(i, item))
#     i += 1

# eg_list = ["요소A", "요소B", "요소C"]
# print("#단순 출력")
# print (eg_list)

# print ("enumerate 적용후 출력")
# print (enumerate(eg_list))

# print("list함수로 변환해서 출력")
# print(list(enumerate(eg_list)))
# print()

# eg_dict = {"키A": "값A",
#  "키A1": "값A1",
#  "키A2": "값A2"}

# print("#딕셔너리의 items() 함수")
# print("items():", eg_dict.items())

# print("딕셔너리의 아이템즈() 함수와 반복문 조합하기")
# for key, element in eg_dict.items():
#     print("dictionary [{}]={}".format(key, element))

# array = []
# for i in range (0,20,2):
#     array.append()
# print(array)
# # 0


# def a(a1, a2):
#     for i in range(a2):
#         print(a1)

# a("안녕하세요", 5)

# def print_n_times(n, *values):
#     for i in range(n):
#         for value in values:
#             print(value)
#         print()

# print_n_times(3, "안녕하세요", "즐거운 파이썬")

# def print_n_times(n=2, *values):
#     for i in range (n):
#         print(value)

# print_n_times("hihi", "파이썬")

# def print_n_times (*values, n=2):
#     for i in range(n):
#         for value in values:
#             print(value)
#         print()
# print_n_times("안녕하세요", "즐거운 파이썬", 3)

# def print_n_times(*values, n=2):
#     for i in range (n):
#         for value in values:
#             print(value)
#         print()

# print_n_times("안녕하세요", "즐거운", "py", n)

# def test(a, b=10, c=100):
#     print(a + b + c)

# test(10)

# def return_test():
#     print("A위치입니다")
#     return "hi"
# return_test()

# def sum_att(start, end):
#     output=0

#     for i in range(start, end+1):
#         output += 1

#     return output

# print("0 to 100:", sum_att(1, 10))

# def sum_all(start=0, end=100, step=1):
#     output=0
#     for i in range(start, end +1, step):
#         output += i
#     return output

# print("A", sum_all(0, 100,10))


# from urllib import request

# url= request.urlopen('https://www.naver.com')
# data= url.read()
# print(data)

# from urllib import request

# target = request.urlopen("https://www.britmates.com/")
# output = target.read()

# print(output)

from urllib import request
from bs4 import BeautifulSoup
import requests

# response = requests.get("https://www.britmates.com/adult/brit-talk-beginner.php")
# text = response.text

# soup = BeautifulSoup(text, "html.parser")
# print(soup.find("h2"))

#-------------네이버에서 환율 정보 가지고 오기------------------
url = "https://finance.naver.com/marketindex/"
response1 = requests.get(url)
# print("달러" in response.text)
soup1 = BeautifulSoup(response1.text, "html.parser")

ur2 = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&ssc=tab.nx.all&query=%EC%84%9C%EC%9A%B8%EC%98%A8%EB%8F%84+%EC%8B%A4%EC%8B%9C%EA%B0%84+%EC%98%A8%EB%8F%84&oquery=%EC%84%9C%EC%9A%B8%EC%98%A8%EB%8F%84+%EC%8B%A4%EC%8B%9C%EA%B0%84+rss&tqi=jlDAVsqXKZGssmZziMw-010092&ackey=gze7h0c8"
response2 = requests.get(ur2) # 홈페이지에서 ur2가지고 오고
soup2 = BeautifulSoup(response2.text, "html.parser") #수프로 텍스트 편집가능한 상태로 정리하고

rate = soup1.select_one("span.value").text
print(rate)

rate2 = soup2.select_one("div.temperature_text").text
print(rate2)

# index = response1.text.find("달러")
# # print(index)

# print(response1.text[index-6195:index+6195])


header = """<br><br> <h2 class="title"> 
환율정보와 시간을 실시간으로 보여주는 페이지 입니다</h2>"""

body = f"""
<style>
.title{{text-align:center; font-size:35px;}}
.currency{{text-align:center; color:blue;}}
.exchange{{text-align:center; color:orange}}
.exchange_p{{font-size:20px;font-weight:bold;background-color:yellow;}}
.currency_p{{font-size:20px;font-weight:bold;background-color:yellow;}}
p{{text-align:center;}}</style>
<br><br><br>

<h1 class="currency">실시간 환율정보</h1>
<p> 현재의 환율은 1USD = <span class="exchange_p">{rate}</span>원 입니다</p>
<br>

<h1 class="exchange">실시간 서울온도</h1>
<p> 현재의 서울 온도는 <span class="currency_p">{rate2}</span>도 입니다"""


html_complete = (header + body)
print(html_complete)

#------------html파일로 저장하기-------------------------
file = open("Projects/sam_prac.py/exchange_html_file.html", "w", encoding="utf-8")
file.write(html_complete)
file.close()
#-----------페이지 꾸미기--------------------------------


print(response2.text.find("temperature_text"))
print(rate2)

