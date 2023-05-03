#How to obtain the distance between two locatiosn using the google maps distance matrix.
#Saved here for future reference in the program.

from datetime import datetime, timedelta

gmaps.distance_matrix(origins=geocode_result[0]['formatted_address'], 
                      destinations=reverse_geocode_result[0]["formatted_address"], 
                      departure_time=datetime.now() + timedelta(minutes=10))
