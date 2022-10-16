from pandas_datareader import data
#data.DataReader? this allows you to find what websites support this module.
#http://pandas-datareader.readthedocs.io/en/latest/remote_data.html#world-bank

import datetime
start = datetime.datetime(2015,3,4)
end = datetime.datetime(2016,3,4)
df = data.DataReader(name = "AAPL", data_source="google",start=start,end=end)
print(df)
