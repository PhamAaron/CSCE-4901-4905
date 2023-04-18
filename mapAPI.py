import requests, json
from pprint import pprint
import googlemaps #pip install google maps
API_KEY = 'AIzaSyA75aaOrg2gdJycVtzQH8r_I_mfsXMcdXw'

map_client = googlemaps.Client(API_KEY)

address = '1155 Union Cir, Denton, TX 76203'
response = map_client.geocode(address)
pprint(response)
print(response[0]['geometry'])
#print(response)

################################## 

address1 = '1155 Union Cir, Denton, TX 76203'
address2 = '12995 Preston Rd, Frisco, TX 75033'

# Requires cities name
my_dist = map_client.distance_matrix(address1, address2)['rows'][0]['elements'][0]
  
# Printing the result
print(my_dist)