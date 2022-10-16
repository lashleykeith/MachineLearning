import folium
import pandas
import json
data = pandas.read_csv("Volcanoes_USA.txt")
map = folium.Map(location = [38.58,-99.09], zoom_start = 6, tiles = "Mapbox Bright")
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])
def color_producer(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation < 3000:
        return "orange"
    else:
        return "red"
fg = folium.FeatureGroup(name = "My Map")
for lt, ln, el in zip(lat, lon, elev):
        
	fg.add_child(folium.CircleMarker(location = [lt, ln],radius= 5, color = "grey",popup= str(el) +  "m", fill_color = color_producer(el), fill_opacity = 0.7, fill = "True" ))
fg.add_child(folium.GeoJson(data= open("world_population.json", 'r',encoding='UTF-8-sig').read(),
style_function= lambda x: {'fillColor' : 'yellow'}))
map.add_child(fg)
map.save("mapp5.html")


'''
import folium
import pandas

df=pandas.read_csv("Volcanoes_USA.txt")


map=folium.Map(location=[df['LAT'].mean(),df['LON'].mean()],zoom_start=6,tiles='Mapbox bright')
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

fg=folium.FeatureGroup(name="Volcano Locations")

for lat,lon,name,elev in zip(df['LAT'],df['LON'],df['NAME'],df['ELEV']):
	fg.add_child(folium.Marker(location=[lat,lon],popup=name,icon=folium.Icon(color=color(elev),icon_color='blue')))

map.add_child(fg)

map.add_child(folium.GeoJson(data=open('world_population.json'),
name='world Population',
style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005']<=10000000 else 'orange' if 10000000<x['properties']['POP2005']<20000000 else 'red'}))

map.add_child(folium.LayerControl())


map.save(outfile='tt.html')
'''