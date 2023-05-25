import requests
from bs4 import BeautifulSoup
import tkinter as tk
from PIL import Image, ImageTk
from io import BytesIO

def get_pcbang_info(location):
    search_url = "https://map.naver.com/v5/search/%EC%A0%95%EC%99%95%EB%8F%99%20pc%EB%B0%A9?c=12,0,0,0,dh"
    res = requests.get(search_url)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, 'html.parser')
    print(res.text,"utp-8")

    pcbang_list = soup.find_all('li', attrs={'class': 'item ng-tns-c27-1'})

    for pcbang in pcbang_list:
        name = pcbang.find('a', attrs={'class': 'title'}).get_text()
        address = pcbang.find('div', attrs={'class': 'item_address ng-star-inserted'}).get_text()
        display_map(address, name)


def display_map(location, name):
    # Replace this with your actual Google Static Maps API key
    API_KEY = "MY_Keys"

    URL = f"https://maps.googleapis.com/maps/api/staticmap?center={location}&zoom=13&size=600x300&maptype=roadmap&key={API_KEY}"

    response = requests.get(URL)
    img_data = response.content
    img = Image.open(BytesIO(img_data))

    window = tk.Tk()
    window.title(name)
    tk_img = ImageTk.PhotoImage(img)
    label = tk.Label(window, image=tk_img)
    label.pack()
    window.mainloop()


get_pcbang_info('정왕동')
