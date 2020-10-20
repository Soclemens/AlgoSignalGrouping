class MAVP():
    def __init__(self, closeArr, periods, minperiod=2, maxperiod=30, matype=0):
        self.closeArr = closeArr
        self.periods = periods
        self.minPeriod = minperiod
        self.maxPeriod = maxperiod
        self.maType = matype
