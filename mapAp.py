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

address1 = '1155 Union Cir, Denton, TX 76203'
address1Components = map_client.geocode(address1)
#address1Lat = address1Components.get("address_components")#.get("geometry").get("bounds").get("location").get("lat")
address1Lat = address1Components[0]["geometry"]["location"]["lat"]
address1Lng = address1Components[0]["geometry"]["location"]["lng"]
address2 = '12995 Preston Rd, Frisco, TX 75033'
address2Components = response = map_client.geocode(address2)
address2Lat = address2Components[0]["geometry"]["location"]["lat"]
address2Lng = address2Components[0]["geometry"]["location"]["lng"]