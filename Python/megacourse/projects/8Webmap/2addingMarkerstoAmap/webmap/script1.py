import folium

map=folium.Map(location=[45.372,-121.697],zoom_start=12,tiles='Stamen Terrain')
map.add_child(folium.Marker(location=[45.3288,-121.6625],popup='Mt. Hood Meadows',icon=folium.Icon(color='red')))
map.add_child(folium.Marker(location=[45.3311,-121.7311],popup='Timberlake Lodge',icon=folium.Icon(color='green')))



map.save('try.html')
