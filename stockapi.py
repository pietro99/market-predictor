import requests
import datetime
import matplotlib.pyplot as plt
from processData import processData
from model import model
import time
#alpha vantage api
#key:
#RUKC5976NKB5TO2E

#api query for 10 years max of daily stock prices:
#https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=OK&outputsize=full&apikey=RUKC5976NKB5TO2E
class stockapi():
    def __init__(self):
        self.DEBUG = False
        self.tickerList = ["GOOG", "MSFT", "AMZN", "V", "UNH"]
        self.key= 'RUKC5976NKB5TO2E'

    def __nextDay(self, date):
        year, month, day = date.split("-")
        d1 = datetime.date(int(year), int(month), int(day))
        d1 += datetime.timedelta(days=-1)
        return d1.strftime("%Y-%m-%d")


    def getTickerHistory(self, ticker):
        stockPrices_ = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol='+ticker+'&outputsize=full&apikey='+self.key)
        stockPrices = stockPrices_.json()
        try:
            last_refreshed = stockPrices['Meta Data']["3. Last Refreshed"]
            stockPerDay = stockPrices["Time Series (Daily)"]
        except Exception:
            print(tiker)
            return False
        date = last_refreshed
        daysCount = 0
        tenYears = 3650
        info = []
        print()
        info.append(stockPerDay[last_refreshed])
        while daysCount<=tenYears:
            daysCount +=1
            date = self.__nextDay(date)
            try:
                dayInfo = stockPerDay[date]
                info.append(dayInfo)
                if self.DEBUG:
                    print(dayInfo)
                    print(date)
                    print(daysCount)
                    print()
            except Exception:
                #info.append(dayInfo)
                if self.DEBUG:
                    print("date not available")
        return info

    def plot(self, th):
        prices = self.getClosingPrice(th)
        plt.plot(prices)
        plt.show()

    def getVolume(self, th):
        volumes = []
        for i in range(len(th)):
            volumes.append(float((th[len(th)-i-1]["6. volume"])))
        return volumes

    def getClosingPrice(self, th):
        prices = []
        for i in range(len(th)):
            prices.append(float((th[len(th)-i-1]["5. adjusted close"])))
        return prices

    def getChange(self, priceList):
        change = []
        change.append(0)
        for i in range(1, len(priceList)):
            change.append((priceList[i]-priceList[i-1])/priceList[i-1])
        return change

stocks = stockapi()
tickerList = stocks.tickerList
process = processData(39, 1)
trainingData_X = []
trainingData_Y = []
testingData_X = []
testingData_Y = []
for tiker in tickerList:
    time.sleep(1)
    th = stocks.getTickerHistory(tiker)
    if(th):      
        prices = stocks.getClosingPrice(th)
        change = stocks.getChange(prices)
        newData = process.cut(prices)
        trD, teD = process.splitValidation(newData)
        train_x, train_y = process.split(trD)
        test_x, test_y = process.split(teD)
        trainingData_X = (trainingData_X + train_x)
        trainingData_Y= (trainingData_Y + train_y)
        testingData_X= (testingData_X + test_x)
        testingData_Y= (testingData_Y + test_y)
    f = open("trainig.txt", "a+")
    for i in range(len(trainingData_Y)):
      f.write(str([trainingData_X[i]]+[trainingData_Y[i]])) 


# print(len(trainingData_X))
# print()
# print(len(trainingData_Y))
# print()
# print(len(testingData_X))
# print()
# print(len(testingData_Y))
# print()
# print(len(trainingData_X[0]))
# print()
# print(len(trainingData_Y[0]))
# print()
# print(len(testingData_X[0]))
# print()
# print(len(testingData_Y[0]))
# print()




# input: [224.5472, 227.2797, 223.2839, 219.6602, 219.151, 222.187, 211.8939, 210.0234, 217.5252, 212.8733, 217.5644, 216.6242, 211.561, 214.783, 216.0954, 218.1324, 210.6501, 215.2629, 211.8352, 207.859, 208.8971, 214.3423, 217.633, 203.1972, 197.4288, 199.5638, 205.6162, 204.9013, 200.9505, 190.8278, 188.9212, 183.5847, 188.1153]

# output: [190.1988, 182.6608, 173.9337, 173.7371, 169.3244, 171.6143, 171.2409]

# prediction: [[385.12437767 384.23208301 384.73227965 385.40576856 386.29168253
#   388.5366287  388.91571108]]