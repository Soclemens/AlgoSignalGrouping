import numpy
import talib
from numpy import genfromtxt
import math

close = genfromtxt('GOOG.csv', delimiter=',')
output = talib.BBANDS(close, timeperiod=5, nbdevup=2, nbdevdn=2, matype=0)

print(output[0][0])

buy = 0
totalP = 0
for i in range(len(output[0])):
    #print(output[0][i])
    if(not math.isnan(output[0][i]) and not math.isnan(output[1][i]) and not math.isnan(output[2][i])):
        if(close[i] + 1 > output[0][i]): #lower band
            buy = close[i]
        elif(close[i] - 1 < output[2][i]): #upper band
            if(buy != 0):
                print("profit: ", close[i] - buy)
                totalP += close[i] - buy
                buy = 0


print(totalP)
        # else:
        #     print(-1)
