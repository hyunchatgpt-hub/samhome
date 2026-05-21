#Q과제 파일의 한줄데이터를 저장하는 클래스를 설계 (변수, 생성자, 출력기능) 해보기
file = open("Question/Q4_Seoul_weather/seoul_weather_2026.csv", "r", encoding="utf-8")
data = file.readlines()



class Weather:
    def __init__ (self, month, aver, high, low, rain, humidity):
        self.month = month
        self.aver = aver
        self.high = high
        self.low = low
        self.rain = rain
        self.humidity = humidity

    def show_me(self):
        print(self.month, self.aver, self.high, self.low, self.rain, self.humidity)

for line in data:
    aft_strip = line.strip()
    aft_split = aft_strip.split(",")
        
    weather_result = Weather(*aft_split)
    weather_result.show_me()   
