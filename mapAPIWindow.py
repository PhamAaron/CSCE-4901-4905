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
address2 = '12995 Preston Rd, Frisco, TX 75033'

# Requires cities name
my_dist = map_client.distance_matrix(address1, address2)['rows'][0]['elements'][0]
  
# Printing the result
#print(my_dist)


####################################################UI
import tkinter as tk
# Define a function to get the user inputs
input1 = '1155 Union Cir, Denton, TX 76203'
input2 = '12995 Preston Rd, Frisco, TX 75033'

def get_inputs():
    input1 = entry1.get()
    input2 = entry2.get()
    print("input1:", input1)
    print("input2:", input2)

# Create a tkinter window
window = tk.Tk()

# Get the size of the screen
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Set the window size to the size of the screen
window.geometry("{}x{}+0+0".format(screen_width, screen_height))

# Remove the window borders
window.overrideredirect(True)

# Create two input fields with larger width and height
entry1 = tk.Entry(window, width=10, font=("Arial", 50))
entry2 = tk.Entry(window, width=10, font=("Arial", 50))

# Create a button to submit the inputs
button = tk.Button(window, text="Submit", command=get_inputs)

# Place the input fields on the left side of the screen
entry1.place(x=50, y=screen_height/2-80)
entry2.place(x=50, y=screen_height/2+80)

# Place the button on the left
button.place(x=50, y=screen_height/2+280)

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
my_dist = map_client.distance_matrix(input1, input2)['rows'][0]['elements'][0]