file = open("Question/Q4_Seoul_weather/seoul_weather_2026.csv", "r", encoding="utf-8")
data = file.readlines()



class Weather:
    def __init__(self, month, aver, high, low, rain, humidity):
        self.month = month
        self.aver = aver
        self.high = high
        self.low = low
        self.rain = rain
        self.humidity = humidity

    def show_me(self):
        print(self.month, self.aver, self.high, self.low, self.rain, self.humidity, sep="\t")
#--------------------------

weather1 = Weather()

for line in data:

    line = line.strip()
    line = line.split(",")

    weather_cast = Weather(*line)
    weather_cast.show_me()
