from tkinter import*
from io import BytesIO
import urllib.request
from PIL import Image, ImageTk
from search_name import*
from tkinter import font
import tkinter.messagebox


class LOLGUI:
    def search(self):

        self.name = self.SEntry.get()
        self.person = user(self.name)
        image_url = self.person.getprofileurl()
        with urllib.request.urlopen(image_url) as u:
            raw_data = u.read()
        im = Image.open(BytesIO(raw_data))
        self.image = ImageTk.PhotoImage(im)

        if self.profil_img != None:
            self.profil_img.pack_forget()
        if self.profil_level != None:
            self.profil_level.pack_forget()
        if self.profil_sololank != None:
            self.profil_sololank.pack_forget()
        if self.profil_freelank != None:
            self.profil_freelank.pack_forget()
        self.profil_img = Label(self.window, image = self.image, height=300, width=300).place(x=0, y=30)
        self.profil_level = Label(self.window, text="LV."+self.person.getlevel(), font=self.TempFont).place(x=310, y=30)
        self.profil_sololank = Label(self.window, text=self.person.getsololank(), font=self.TempFont).place(x=310, y=60)
        self.profil_freelank = Label(self.window, text=self.person.getfreelank(), font=self.TempFont).place(x=310, y=90)

    def __init__(self):
        self.window = Tk()
        self.window.geometry("800x800")
        self.window.title("LOL_Dictionary")
        self.TempFont= font.Font(size = 16 , weight='bold', family='Consolas')
        self.SEntry = Entry(self.window,font= self.TempFont)
        self.SEntry.place(x=0,y=0)
        self.name = None
        self.person = None
        self.image = None
        #프로필 버튼들변수들
        self.profil_img = None
        self.profil_level = None
        self.profil_sololank = None
        self.profil_freelank = None
        #검색 버튼
        self.SButton=Button(self.window,text='검색',command=self.search)
        self.SButton.place(x=250,y=0)


        self.window.mainloop()



LOLGUI()
