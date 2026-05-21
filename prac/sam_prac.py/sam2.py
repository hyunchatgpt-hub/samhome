from bs4 import BeautifulSoup
import requests


url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&ssc=tab.nx.all&query=%EC%84%9C%EC%9A%B8%EC%98%A8%EB%8F%84+%EC%8B%A4%EC%8B%9C%EA%B0%84+%EC%98%A8%EB%8F%84&oquery=%EC%84%9C%EC%9A%B8%EC%98%A8%EB%8F%84+%EC%8B%A4%EC%8B%9C%EA%B0%84+rss&tqi=jlDAVsqXKZGssmZziMw-010092&ackey=gze7h0c8"
response = requests.get(url) # 홈페이지에서 url가지고 오고
soup = BeautifulSoup(response.text, "html.parser") #수프로 텍스트 편집가능한 상태로 정리하고
# print("23" in response.text)
# index = response.text.find("28.8")
# print (index)

# print(response.text[index-70321:index+70321])

# index = response.text.find("달러")
# # print(index)

# print(response.text[index-6195:index+6195])

# soup = BeautifulSoup(response.text, "html.parser")
rate = soup.select_one("div.temperature_text").text
print(rate)


# print("달러" in response.text)