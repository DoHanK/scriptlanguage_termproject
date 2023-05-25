import tkinter as tk
from tkinter import ttk
import webbrowser

# Google Maps API key
API_KEY = 'AIzaSyAAe90xo8B26j_5bne0HAU0cS1IQDQUP5s'

# 시/도와 도시 정보
provinces = {'Seoul': ['Gangnam-gu', 'Seocho-gu'], 'Busan': ['Haeundae-gu', 'Busanjin-gu']}


def open_map(*args):
    province = province_var.get()
    city = city_var.get()

    # Open the Google Maps URL with the selected city in the web browser
    url = f"https://www.google.com/maps/search/PC방+in+{province}+{city}?key={API_KEY}"
    webbrowser.open(url)


# Set up the Tkinter window
root = tk.Tk()

province_var = tk.StringVar()
city_var = tk.StringVar()

# Create the province dropdown menu
province_dropdown = ttk.Combobox(root, textvariable=province_var)
province_dropdown['values'] = list(provinces.keys())
province_dropdown.grid(column=0, row=0)

# Create the city dropdown menu
city_dropdown = ttk.Combobox(root, textvariable=city_var)
city_dropdown.grid(column=1, row=0)


# Update the city dropdown menu when a province is selected
def update_cities(*args):
    cities = provinces[province_var.get()]
    city_dropdown['values'] = cities


province_var.trace('w', update_cities)

# When a city is selected, open the map
city_var.trace('w', open_map)

root.mainloop()