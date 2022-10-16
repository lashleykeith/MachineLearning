from bokeh.charts import Scatter, output_file, show
import pandas

df=pandas.DataFrame(columns=["X","Y"])
df["X"]= [1,2,3,4,5]
df["Y"]= [5,6,4,5,3]

p=Scatter(df, x="X", y="Y", title="Temperature Observations",xlabel="Day of observation", ylabel="Temperature")

output_file("Scatter_charts.html")

show(p)

from bokeh.plotting import figure, output_file, show

p=figure(plot_width=500,plot_height=400,title="Earthquakes")

# the x than y than the size of the plots
p.circle([1,2,3,4,5],[5,6,5,5,3], size=[i * 2 for i in [8,12,14,15,20]], color="red",alpha=0.5)

output_file("Scatter_plotting.html")
show(p)