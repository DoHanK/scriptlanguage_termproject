from tkinter import*
from io import BytesIO
import urllib.request
from PIL import Image, ImageTk
from search_name import*



class LOLGUI:

    def __init__(self):
        self.name = input("사용자이름을 입력하세요")
        self.person = user(self.name)


        image_url = self.person.getprofileurl()
        self.window = Tk()
        self.window.title("LOL_Dictionary")
        self.frame = Frame()
        self.frame.pack(side=LEFT)
        with urllib.request.urlopen(image_url) as u:
            raw_data = u.read()
        im = Image.open(BytesIO(raw_data))
        image = ImageTk.PhotoImage(im)

        Label(self.frame, image=image, height=400, width=400).pack()


        self.window.mainloop()



LOLGUI()
