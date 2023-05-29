from tkinter import*
import tkinter.ttk
from io import BytesIO
import urllib.request
from PIL import Image, ImageTk
from search_name import*
from tkinter import font
import tkinter.messagebox


#frame1은 전적검색 기능

class LOLGUI:
    def user_search(self):

       self.name = self.SEntry.get()
       if self.name != "":
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

        self.profil_img = Label(self.frame1, image = self.image, height=300, width=300).place(x=0, y=30)
        self.profil_name = Label(self.frame1, text= "닉네임: "+self.person.name+"  ", font=self.TempFont).place(x=310, y=30)
        self.profil_level = Label(self.frame1, text= "LV."+self.person.getlevel(), font=self.TempFont).place(x=310, y=60)
        self.profil_sololank = Label(self.frame1, text=self.person.getsololank(), font=self.TempFont).place(x=310, y=90)
        self.profil_freelank = Label(self.frame1, text=self.person.getfreelank(), font=self.TempFont).place(x=310, y=120)
        self.SEntry.delete(0, 'end')

    def user_append(self):
        if  self.person !=None and self.person not in self.userlist:
            self.userlist.append(self.person)
        print(self.userlist)

    def __init__(self):
        self.window = Tk()

        #노트북을 만들기
        self.notebook = tkinter.ttk.Notebook(self.window, width=800, height=600)
        self.notebook.pack()
        self.notefont= font.Font(size = 20 , weight='bold', family='Consolas')
        #프레임 1 사용자검색기능
        self.frame1 = Frame(self.window)
        self.notebook.add(self.frame1, text="전적검색기능")
        #프레임2 사용자 승률 비교프레임
        self.frame2 = Frame(self.window)
        self.notebook.add(self.frame2, text="승률비교그래프")


        self.window.geometry("800x800")
        self.window.title("LOL_Dictionary")
        self.TempFont= font.Font(size = 16 , weight='bold', family='Consolas')
        self.SEntry = Entry(self.frame1,font= self.TempFont)
        self.SEntry.place(x=0,y=0)
        self.name = None
        self.person = None
        self.image = None

        #프로필 버튼들변수들
        self.profil_img = None
        self.profil_level = None
        self.profil_sololank = None
        self.profil_freelank = None
        self.profil_name = None

        #검색 버튼
        self.SButton=Button(self.frame1,text='전적검색',command=self.user_search)
        self.SButton.place(x=250,y=0)
        self.GButton = Button(self.frame1, text='그래프에추가하기', command=self.user_append)
        self.GButton.place(x=310, y=0)

        #사용자리스트들
        self.userlist = []
        self.Luserlist = []

        self.window.mainloop()



LOLGUI()
