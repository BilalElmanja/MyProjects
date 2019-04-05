import folium
import pandas
import os

database = pandas.read_excel('worldcities.xlsx')


webmap = folium.Map(zoom_start=1)
Cities = folium.FeatureGroup(name='cities')
Population = folium.FeatureGroup(name='population')


Population.add_child(folium.GeoJson(data=open('115 world.json' , 'r' , encoding='utf-8-sig').read(),
 style_function=lambda x: {'fillColor':'orange' if x['properties']['POP2005']<10000000 
 else 'green' if 1000000 <= x['properties']['POP2005'] < 20000000 else 'red'} , tooltip='country'))


for i in range(database.shape[0]):
    list1 = [database['lat'][i] , database['lng'][i]]
    popup1 = "city : " + database['city'][i] + "\n" + " country : " + database['country'][i] + "\n" + " id : " + str(database['id'][i])
    Cities.add_child(folium.CircleMarker(location=list1 , radius=0.1 , popup=popup1 , fill_color='orange' , fill_opacity=0.4 , color='orange'))





webmap.add_child(Cities)
webmap.add_child(Population)
webmap.add_child(folium.LayerControl())

webmap.save('MapApplication.html')

