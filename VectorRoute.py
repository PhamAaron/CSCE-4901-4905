# Code to get he vectors from point a to b
# After getting the vectors, inputs into a map for the user to view for the mapApi.py program

locations = [address1,address2]

markers = ["color:blue|size:mid|label:" + chr(65+i) + "|" 
                   + r for i, r in enumerate(locations)]
                   
result_map = gmaps.static_map(
                 center=locations[0],
                 scale=2, 
                 zoom=12,
                 size=[640, 640], 
                 format="jpg", 
                 maptype="roadmap",
                 markers=markers,
                 path="color:0x0000ff|weight:2|" + "|".join(locations))

with open(“driving_route_map.jpg”, “wb”) as img:
    for chunk in result_map:
        img.write(chunk)

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
result_map = gmaps.static_map(
                 center = waypoints[0],
                 scale=2, 
                 zoom=13,
                 size=[640, 640], 
                 format="jpg", 
                 maptype="roadmap",
                 markers=markers,
                 path="color:0x0000ff|weight:2|" + "|".join(waypoints))
