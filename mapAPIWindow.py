import requests, json
from pprint import pprint
from gmplot import gmplot
import webbrowser
import os
import googlemaps #pip install google maps
API_KEY = 'AIzaSyA75aaOrg2gdJycVtzQH8r_I_mfsXMcdXw'


map_client = googlemaps.Client(API_KEY)

#address = '1155 Union Cir, Denton, TX 76203'
#response = map_client.geocode(address)
#pprint(response)
#print(response[0]['geometry'])
#print(response)

################################## 
"""

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
"""

#########################################################UI
import tkinter as tk
# Define a function to get the user inputs
input1 = '1155 Union Cir, Denton, TX 76203'
input2 = '12995 Preston Rd, Frisco, TX 75033'

def get_inputs():
    input1 = entry1.get()
    input2 = entry2.get()
    print("input1:", input1)
    print("input2:", input2)
    calculate(input1, input2)

def calculate(input1, input2):
    input1Components = map_client.geocode(input1)
    input1Lat = input1Components[0]["geometry"]["location"]["lat"]
    input1Lng = input1Components[0]["geometry"]["location"]["lng"]
    input2Components = map_client.geocode(input2)
    input2Lat = input2Components[0]["geometry"]["location"]["lat"]
    input2Lng = input2Components[0]["geometry"]["location"]["lng"]
    midpointLat = (input1Lat+input2Lat)/2
    midpointLng = (input1Lng+input2Lng)/2   

    # Requires cities name
    my_dist = map_client.distance_matrix(input1, input2)['rows'][0]['elements'][0]

    # the result is a Python dictionary:
    dist = my_dist.get("distance").get("text")
    dur = my_dist.get("duration").get("text")

    ############Draw
    label1.config(text="Lat:" + str(midpointLat))
    label2.config(text="Lng:" + str(midpointLng))
    label3.config(text="Dist:" + str(dist))
    label4.config(text="Time:" + str(dur))

    # Initialize the map at a given point
    gmap = gmplot.GoogleMapPlotter(midpointLat, midpointLng, 13)

    # Add a marker
    gmap.marker(input1Lat, input1Lng, 'cornflowerblue')
    gmap.marker(midpointLat, midpointLng, 'cornflowerblue')
    gmap.marker(input2Lat, input2Lng, 'cornflowerblue')

    # Draw map into HTML file
    gmap.draw("my_map.html")

def show():
    # 1st method how to open html files in chrome using
    filename = 'file:///'+os.getcwd()+'/' + 'my_map.html'
    webbrowser.open_new_tab(filename)

#################################################################################

# Create a tkinter window
window = tk.Tk()

# Set the window size to the size of the screen
#window.geometry("{}x{}+0+0".format(screen_width, screen_height))
  
# creating fixed geometry of the
# tkinter window with dimensions 150x200
window.geometry('1920x1080+100+100')

# Get the size of the screen
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Remove the window borders
#window.overrideredirect(True)

# Create two input fields with larger width and height
entry1 = tk.Entry(window, width=20, font=("Arial", 20))
entry2 = tk.Entry(window, width=20, font=("Arial", 20))

# Create a button to submit the inputs
button1 = tk.Button(window, text="Calculate", command=get_inputs)
button2 = tk.Button(window, text="Show Map", command=show)

# Place the input fields on the left side of the screen
entry1.place(x=50, y=screen_height/2-80)
entry2.place(x=50, y=screen_height/2+80)

# Place the button on the left
button1.place(x=50, y=screen_height/2+280)
button2.place(x=50, y=screen_height/2+320)

# Create a label to show the inputs
#label = tk.Label(window, font=("Arial", 20))
label1 = tk.Label(window, font=("Arial", 10), text="Lat:")
label2 = tk.Label(window, font=("Arial", 10), text="Lng:")
label3 = tk.Label(window, font=("Arial", 10), text="Dist:")
label4 = tk.Label(window, font=("Arial", 10), text="Time:")

# Place the label below the input fields
label1.place(x=screen_width-500, y=screen_height/2-60)
label2.place(x=screen_width-500, y=screen_height/2-20)
label3.place(x=screen_width-500, y=screen_height/2+20)
label4.place(x=screen_width-500, y=screen_height/2+60)

# Start the tkinter event loop ######################
window.mainloop()

######################################################