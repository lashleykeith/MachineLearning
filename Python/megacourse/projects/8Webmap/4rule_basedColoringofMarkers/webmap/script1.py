import folium
import pandas

df=pandas.read_csv("Volcanoes_USA.txt")


map=folium.Map(location=[45.372,-121.697],zoom_start=12,tiles='Stamen Terrain')

for lat,lon,name,elev in zip(df['LAT'],df['LON'],df['NAME'],df['ELEV']):

	map.add_child(folium.Marker(location=[lat,lon],popup='name',icon=folium.Icon(color='green' if elev in range(0,1000)else'orange' if elev in range(1000,3000)else 'red')))



map.save('try.html')
