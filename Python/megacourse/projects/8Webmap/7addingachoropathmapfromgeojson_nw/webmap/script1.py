import folium
import pandas

df=pandas.read_csv("Volcanoes_USA.txt")


map=folium.Map(location=[df['LAT'].mean(),df['LON'].mean()],zoom_start=6,tiles='Stamen Terrain')
#---------you can replace Stamen Terrian with other options. http://deparkes.co.uk/2016/06/10/folium-map-tiles/.

def color(elev):
	minimum=int(min(df['ELEV']))
	step=int((max(df['ELEV'])-min(df['ELEV']))/3)
	if elev in range(minimum,minimum+step):
		col='green'
	elif elev in range(minimum+step,minimum+step*2):
		col='orange'
	else:
		col='red'
	return col

for lat,lon,name,elev in zip(df['LAT'],df['LON'],df['NAME'],df['ELEV']):
	map.add_child(folium.Marker(location=[lat,lon],popup=name,icon=folium.Icon(color=color(elev),icon_color='blue')))

map.add_child(folium.GeoJson(data=open('world_population.json'),
	name='world Population',
	style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005']<=10000000 else 'orange' if 10000000<x['properties']['POP2005']<20000000 else 'red'}))

map.save('vtv.html')
