import requests as r
import re
from getsp500 import get_sp500_syms
from datetime import datetime
import time

def get_data(symbols, csv = False):
    data = []
    url = 'http://finance.yahoo.com/d/quotes.csv?s='
    for s in symbols:
        if "." in s:
            s = s.replace(".", "-")
        url += s+"+"
    url = url[0:-1]
    url += "&f=sb3b2l1p"
    f = r.get(url).content
    rows = f.splitlines()
    for row in rows:
        try:
            values = [x for x in row.split(',')]
            symbol = values[0][1:-1]
            bid = values[1]
            ask = values[2]
            latest = values[3]
            previous = values[4]
            time = datetime.now()
            if csv:
                # Hour, Minute, Second, Month, Day, Year, Bid, Ask, Latest
                f = open("data/%s.csv" % symbol, "a")
                f.write("%s,%s,%s,%s,%s,%s,%s,%s,%s\r\n" % \
                    (time.hour, time.minute, time.second, time.month, \
                     time.day, time.year, bid, ask, latest))
                f.close()
            else:
                data.append({"time": str(time),
                             "symbol":symbol, \
                             "bid":float(bid), \
                             "ask":float(ask), \
                             "latest":float(latest),\
                             "previous":float(previous)})
        except Exception as e:
            print "Error on '%s': %s" % (symbol, e.__str__())
    return data

def get_all_data(csv = False):
    symbols = get_sp500_syms()
    res = get_data(symbols[0:100], csv=csv)
    res += get_data(symbols[100:200], csv=csv)
    res += get_data(symbols[200:300], csv=csv)
    res += get_data(symbols[300:400], csv=csv)
    res += get_data(symbols[400:500], csv=csv)
    return res

def get_gaps(data):
    ''' 
    Returns a list of the percentage change (gap) between current price and 
    previous day's close.
    '''
    gaps = []
    for d in data:
        dif = d["latest"] - d["previous"]
        percent = (dif / d["previous"]) * 100
        gaps.append((d,percent))
        if abs(percent) >= 5:
            print "%s's percent change = %f" % (d["symbol"], percent)
    return gaps

# this will run in a loop from the opening of the market until the
# close, grabbing the data every 5 seconds.
start_time = datetime.strptime('08:30:00 09/16/2013', '%H:%M:%S %m/%d/%Y')
stop_time = datetime.strptime('16:00:00 09/16/2013', '%H:%M:%S %m/%d/%Y')

while 0 <= datetime.now().weekday() <= 4 and start_time <= datetime.now() <= stop_time:
    get_all_data(csv=True)
    time.sleep(2)