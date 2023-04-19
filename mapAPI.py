import requests, json
from pprint import pprint
import googlemaps #pip install google maps
API_KEY = 'AIzaSyA75aaOrg2gdJycVtzQH8r_I_mfsXMcdXw'

map_client = googlemaps.Client(API_KEY)

address = '1155 Union Cir, Denton, TX 76203'
response = map_client.geocode(address)
#pprint(response)
#print(response[0]['geometry'])
#print(response)

################################## 

address1 = '1155 Union Cir, Denton, TX 76203'
address1Components = map_client.geocode(address1)
#address1Lat = address1Components.get("address_components")#.get("geometry").get("bounds").get("location").get("lat")
address1Lat = address1Components[0]["geometry"]["location"]["lat"]
address1Lng = address1Components[0]["geometry"]["location"]["lng"]
address2 = '12995 Preston Rd, Frisco, TX 75033'
address2Components = response = map_client.geocode(address2)
address2Lat = address2Components[0]["geometry"]["location"]["lat"]
address2Lng = address2Components[0]["geometry"]["location"]["lng"]

# Requires cities name
my_dist = map_client.distance_matrix(address1, address2)['rows'][0]['elements'][0]

# the result is a Python dictionary:
dist = my_dist.get("distance").get("text")
dur = my_dist.get("duration").get("text")

print(address1)
print(address1Lat)
print(address1Lng)
print(address2)
print(address2Lat)
print(address2Lng)

print(dist)
print(dur)

midpointLat = (address1Lat+address2Lat)/2
midpointLng = (address1Lng+address2Lng)/2

print(midpointLat)
print(midpointLng)

#pprint(my_dist["distance"])
#pprint(my_dist["duration"])

#########################################################

from gmplot import gmplot

# Initialize the map at a given point
gmap = gmplot.GoogleMapPlotter(midpointLat, midpointLng, 13) #API KEY ISSUES

# Add a marker
gmap.marker(address1Lat, address1Lng, 'cornflowerblue')
gmap.marker(midpointLat, midpointLng, 'cornflowerblue')
gmap.marker(address2Lat, address2Lng, 'cornflowerblue')

# Draw map into HTML file
gmap.draw("my_map.html")

#########################################################
"""""
# creating and viewing the html files in python
 
import webbrowser
import os
 
# 1st method how to open html files in chrome using
filename = 'file:///'+os.getcwd()+'/' + 'my_map.html'
webbrowser.open_new_tab(filename)
"""""
#########################################################

from datetime import datetime, timedelta

directions_result = map_client.directions(address1,
                                     address2)#,
                                     #arrival_time=datetime.now() + timedelta(minutes=0.5))



#########################################################

""""
waypoints = ["Chinatown Buddha Tooth Relic Temple", 
"Sentosa Island, Singapore", 
"National Gallery Singapore", 
"Botanic Garden, Singapore",
"Boat Quay @ Bonham Street, Singapore 049782"]
"""
waypoints = []

results = map_client.directions(origin = address1,
                                         destination = address2,                                     
                                         waypoints = waypoints,
                                         optimize_waypoints = True,
                                         departure_time=datetime.now() + timedelta(hours=1)) ######################

for i, leg in enumerate(results[0]["legs"]):
    print("Stop:" + str(i),
        leg["start_address"], 
        "==> ",
        leg["end_address"], 
        "distance: ",  
        leg["distance"]["value"], 
        "traveling Time: ",
        leg["duration"]["value"]
    )


locations = []

markers = ["color:blue|size:mid|label:" + chr(65+i) + "|" 
                   + r for i, r in enumerate(locations)]

"""
result_map = map_client.static_map(
                 center=locations[0],
                 scale=2, 
                 zoom=12,
                 size=[640, 640], 
                 format="jpg", 
                 maptype="roadmap",
                 markers=markers,
                 path="color:0x0000ff|weight:2|" + "|".join(locations)) ######################

with open("driving_route_map.jpg", "wb") as img:
    for chunk in result_map:
        img.write(chunk)
"""
###############################################################################

marker_points = []
waypoints = []

#extract the location points from the previous directions function

for leg in results[0]["legs"]:
    leg_start_loc = leg["start_location"]
    marker_points.append(f'{leg_start_loc["lat"]},{leg_start_loc["lng"]}')
    for step in leg["steps"]:
        end_loc = step["end_location"]
        waypoints.append(f'{end_loc["lat"]},{end_loc["lng"]}')
last_stop = results[0]["legs"][-1]["end_location"]
marker_points.append(f'{last_stop["lat"]},{last_stop["lng"]}')
        
markers = [ "color:blue|size:mid|label:" + chr(65+i) + "|" 
           + r for i, r in enumerate(marker_points)]
result_map = map_client.static_map(
                 center = (midpointLat, midpointLng), #Needs to be new calculated midpoint
                 scale=2, 
                 zoom=10,############################needs to be based on distance
                 size=[640, 640], 
                 format="jpg", 
                 maptype="roadmap",
                 markers=markers,
                 path="color:0x0000ff|weight:2|" + "|".join(waypoints)) ################################

with open("driving_route_map.jpg", "wb") as img:
    for chunk in result_map:
        img.write(chunk)

#distance is meters time is seconds