from bokeh.plotting import figure, output_file, show
import pandas

df = pandas.read_csv("https://www.google.com/finance/historical?q=NASDAQ:ADBE&startdate=Jan+01%2C+2009&enddate=Aug+2%2C+2012&output=csv",parse_dates=["Date"])

p = figure(width=500, height=250,x_axis_type="datetime", responsive=True)
p.title = 'Candlestick Chart'

p.line(df["Date"],df["Close"],color="Orange",alpha = 0.5)
#p.circle(df["Date"],df["Close"],color="Orange",alpha = 0.5)
#p.circle(df["Date"],df["Close"],size=[i * 2 for i in [1,5,9,25,50]],color="olive",alpha = 0.5)

output_file("Timeseries.html")
show(p)
#https://www.google.com/finance/historical?q=NASDAQ:ADBE&startdate=Jan+01%2C0
#https://www.google.com/finance/historical?q=NASDAQ:ADBE&startdate=Jan+01%2C+2009&enddate=Aug+2%2C+2012&output=csv
#bokeh.pydata.org/en/latest/docs/use_guide/plottig.html
#bokeh.pydata.org/en/0.10.0/docs/gallery.html
#jupyter notebook