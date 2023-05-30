from tkinter import*
import tkinter.ttk as ttk
from io import BytesIO
import urllib.request
from PIL import Image, ImageTk ,ImageFont,ImageDraw
from search_name import*
from tkinter import font
import tkinter.messagebox
from random import*
import imageio
import cv2
import sys
import tkinterweb as web
from search_item import*
from pcsearch import*
import jongdoAI


HEIGHT = 400
WIDTH = 800






def CreateUrltoPhoto(url):
    image_url = url
    with urllib.request.urlopen(image_url) as u:
        raw_data = u.read()
    im = Image.open(BytesIO(raw_data))
    image = ImageTk.PhotoImage(im)
    return image


def translate_champion_name(korean_name):
    # Riot Games API에서 한글 이름을 영어로 변환하기 위한 URL
    url = f"http://ddragon.leagueoflegends.com/cdn/11.19.1/data/ko_KR/champion.json"

    try:
        response = requests.get(url)
        data = response.json()

        # 챔피언 데이터에서 한글 이름과 영어 이름을 매칭
        for champion in data['data'].values():
            if champion['name'] == korean_name:
                return champion['id']

        # 일치하는 챔피언이 없는 경우 None 반환
        return None

    except requests.exceptions.RequestException as e:
        print("요청 오류:", e)


# 비디오 파일 경로 설정
videolist=["아리.mp4","나미.mp4","로봇.mp4","애니.mp4"]
video_path = videolist[randint(0,len(videolist)-1)]

#색상 랜덤으로 배정
def CreateRandomColor():
    Colors = "#"
    for x in range(6):
        temp = randint(0, 15)
        if temp >= 10:
            Colors += chr(ord('A') + temp - 10)
        else:
            Colors += str(temp)
    return Colors


class LOLGUI:
    def on_subwindow_close(self):
        self.subwindow.destroy()
        self.subwindow = None

##전적 검색
    def user_search(self):
       subbg='black'
       subfg='white'
       if self.subwindow == None:
           self.subwindow  = Toplevel(self.window)
           self.subwindow .title("전적검색")
           self.subwindow .geometry("750x300+800+250")
           self.subwindow.protocol("WM_DELETE_WINDOW",self.on_subwindow_close)
           self.subwindow['bg']=subbg
       else:
           if self.profil_img != None:
               self.profil_img.place_forget()
           if self.profil_name != None:
               self.profil_name.place_forget()
           if self.profil_level != None:
               self.profil_level.place_forget()
           if self.profil_sololank != None:
               self.profil_sololank.place_forget()
           if self.profil_freelank != None:
               self.profil_freelank.place_forget()

       self.name = self.SEntry.get()
       if self.name != "":
        self.person = user(self.name)
        image_url = self.person.getprofileurl()
        with urllib.request.urlopen(image_url) as u:
            raw_data = u.read()
        im = Image.open(BytesIO(raw_data))
        self.image = ImageTk.PhotoImage(im)



        self.profil_img = Label(self.subwindow , image = self.image, height=300, width=300)
        self.profil_img.place(x=0, y=0)
        self.profil_name = Label(self.subwindow , text="닉네임: "+self.name+" ",bg=subbg,fg=subfg, font= self.TempFont)
        self.profil_name.place(x=310, y=30)
        self.profil_level = Label(self.subwindow , text= "LV."+self.person.getlevel(),bg=subbg, fg=subfg, font=self.TempFont)
        self.profil_level.place(x=310, y=60)
        self.profil_freelank = Label(self.subwindow , text=self.person.getfreelank(),bg=subbg, fg=subfg, font=self.TempFont)
        self.profil_freelank.place(x=310, y=90)
        self.profil_sololank = Label(self.subwindow , text=self.person.getsololank(),bg=subbg,fg=subfg, font=self.TempFont)
        self.profil_sololank.place(x=310, y=120)
        self.subwindow.mainloop()

## 전적 그래프에서 띄우기
    def changeprofil(self,user):
        subbg = 'black'
        subfg = 'white'
        if self.subwindow == None:
            self.subwindow = Toplevel(self.window)
            self.subwindow.title("전적검색")
            self.subwindow.geometry("750x300+800+250")
            self.subwindow.protocol("WM_DELETE_WINDOW", self.on_subwindow_close)
            self.subwindow['bg'] = subbg
        else:
            if self.profil_img != None:
                self.profil_img.place_forget()
            if self.profil_name != None:
                self.profil_name.place_forget()
            if self.profil_level != None:
                self.profil_level.place_forget()
            if self.profil_sololank != None:
                self.profil_sololank.place_forget()
            if self.profil_freelank != None:
                self.profil_freelank.place_forget()

        self.person = user
        image_url = self.person.getprofileurl()
        with urllib.request.urlopen(image_url) as u:
            raw_data = u.read()
        im = Image.open(BytesIO(raw_data))
        self.image = ImageTk.PhotoImage(im)


        self.profil_img = Label(self.subwindow, image=self.image, height=300, width=300)
        self.profil_img.place(x=0, y=0)
        self.profil_name = Label(self.subwindow, text="닉네임: " + self.person.name + " ", bg=subbg, fg=subfg,
                                 font=self.TempFont)
        self.profil_name.place(x=310, y=30)
        self.profil_level = Label(self.subwindow, text="LV." + self.person.getlevel(), bg=subbg, fg=subfg,
                                  font=self.TempFont)
        self.profil_level.place(x=310, y=60)
        self.profil_freelank = Label(self.subwindow, text=self.person.getfreelank(), bg=subbg, fg=subfg,
                                     font=self.TempFont)
        self.profil_freelank.place(x=310, y=90)
        self.profil_sololank = Label(self.subwindow, text=self.person.getsololank(), bg=subbg, fg=subfg,
                                     font=self.TempFont)
        self.profil_sololank.place(x=310, y=120)

#유저 그래프 추가
    def user_append(self):
        if  self.person !=None and self.person not in self.userlist:
            self.userlist.append(self.person)
            self.UserLabelCreate()

#유저 그래프 그리기
    def UserLabelCreate(self):
        for userLabel in self.Luserlist:
            #라벨 지우고 다시 추가
            if userLabel!= None:
                userLabel.destroy()
        for textlabel in self.textLabel:
            if textlabel != None:
                textlabel.destroy()

        self.LuserLabel = []
        self.textLabel = []
        count = 0
        self.frame2.delete('histogram')
        for x in self.userlist:
            fsize = 8
            text = Button(self.frame2,text=x.name,width=3,height=2,fg='red',bg="#010A13", command=lambda label_name=x: self.changeprofil(label_name),font=font.Font(size = fsize , weight='bold', family='Consolas'))
            text.place(x=26*count,y=20)
            self.textLabel.append(text)
            self.frame2.create_rectangle(25 * (count)+10, 100+(100 -(int)(x.GetOnlySoloLankOdds())),25 * (count + 1), 200, outline='#3F9DE0', fill='#3F9DE0',tags='histogram')
            # EC2040
            count+=1

#유저 그래프 비우기
    def cleargraph(self):
        for userLabel in self.Luserlist:
            # 라벨 지우고 다시 추가
            if userLabel != None:
                userLabel.destroy()
        for textlabel in self.textLabel:
            if textlabel != None:
                textlabel.destroy()

        self.LuserLabel = []
        self.textLabel = []
        self.userlist = []
        self.frame2.delete('histogram')

#챔피언 얼굴 띄우기
    def Searchcham(self):

        kcham = self.charEntry.get()
        self.chamnamelabel.place_forget()
        if(kcham.encode().isalpha() == False):
            echam = translate_champion_name(kcham)
            self.chamnamelabel = Label(self.frame3, text=kcham + "(" + echam + ")", bg="#010A13", fg="red",
                                       font=(font.Font(size=30, weight='bold', family='Consolas')))
            self.chamnamelabel.place(x=200, y=150)

        else:
            print("영오입니다.")
            echam = kcham
            self.chamnamelabel = Label(self.frame3, text=kcham , bg="#010A13", fg="red",font=(font.Font(size=30, weight='bold', family='Consolas')))
            self.chamnamelabel.place(x=200, y=150)

        self.chamfaceurl="https://opgg-static.akamaized.net/meta/images/lol/champion/"+echam+".png?image=c_crop,h_103,w_103,x_9,y_9/q_auto,f_webp,w_160&v=1685352893390"
        #url 이미지 링크를 이미지로 바꾸기
        self.chamface = CreateUrltoPhoto(self.chamfaceurl)

        #얼굴 라벨
        self.chamimageLabel =Label(self.frame3, image=self.chamface).place(x=20, y=55)
        if self.ItemListLabel !=None:
            for x in self.ItemListLabel:
                x.place_forget()
            self.ItemIagines = []
            self.ItemListLabel = []


        #추천 빌드 아이템
        self.item = Items(echam)
        for x in self.item.geturl():
            self.ItemIagines.append(CreateUrltoPhoto(x))

        for x in self.ItemIagines:
            self.ItemListLabel.append(Label(self.frame3, image=x))

        for x in range(3):
            self.ItemListLabel[x].place(x=200+100*x, y = 250)




    def __init__(self):
        self.window = Tk()
        self.subwindow = None
        #노트북 설정 하기
        self.window.geometry("800x400+0+60")
        self.window.title("LOL_Dictionary")
        self.TempFont= font.Font(size = 16 , weight='bold', family='Consolas')
        style = ttk.Style()
        style.theme_create("custom_theme", parent="alt", settings={
            "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0],"background":"#010A13"}},
            "TNotebook.Tab": {
                "configure": {"padding": [10, 5], "background": "#0F09A0","foreground": "#FFFFFF"},
                "map": {"background": [("selected", "black")],"foreground": [("selected", "red")]},
            }
        })
        style.theme_use("custom_theme")
        #노트북을 만들기
        self.notebook = tkinter.ttk.Notebook(self.window,width=800,height=600, style="TNotebook")
        self.notebook.pack()
        #프레임 1 사용자검색기능
        self.frame1 = Frame(self.notebook,bg="#010A13")
        self.notebook.add(self.frame1, text="전적검색기능")
        self.SEntry = Entry(self.frame1,font=self.TempFont)
        self.SEntry.place(x=0,y=0)
        #검색 버튼 프레임 1에대한
        self.SButton=Button(self.frame1,bg="#330303",fg="#FFFFFF",text='전적검색',command=self.user_search)
        self.SButton.place(x=250,y=0)
        self.GButton = Button(self.frame1,bg="#330303",fg="#FFFFFF",text='그래프에추가하기', command=self.user_append)
        self.GButton.place(x=310, y=0)


        #프레임2 사용자 승률 비교프레임
        self.frame2 = Canvas(self.notebook,bg="#010A13")
        self.notebook.add(self.frame2, text="승률비교그래프")
        bg_image = PhotoImage(file="background.png")


        #프레임 2 변수들
        self.Luserlist = []
        self.userlist = []
        self.textLabel = []
        self.ClearButton =Button(self.frame2,bg="#330303",width=11,height=3,fg="#FFFFFF",text='그래프 비우기',command=self.cleargraph)
        self.ClearButton.place(x=10,y=300)
        #프레임3
        self.frame3 = Frame(self.notebook)
        Label(self.frame3,image = bg_image).place(x=0,y=0)
        self.notebook.add(self.frame3 , text="챔피언아이템 빌드")
        self.charEntry= Entry(self.frame3,font=self.TempFont)
        self.charEntry.place(x=20, y=25)
        self.chamfaceurl =None
        self.chamface = None
        self.ItemListLabel=[]
        self.ItemIagines = []
        self.chamnamelabel = None
        self.item =None
        Label(self.frame3, text="챔피언이름  " , bg="#010A13", fg="red",font=(font.Font(size=30, weight='bold', family='Consolas'))).place(x=200, y=90)
        self.chamnamelabel = Label(self.frame3, text="", bg="#010A13", fg="red", font=(font.Font(size=30, weight='bold', family='Consolas')))
        #검색 버튼 프레임 3에대한
        self.charButton=Button(self.frame3,bg="#330303",fg="#FFFFFF",text='챔피언검색',command=self.Searchcham)
        self.charButton.place(x=270,y=25)
        self.chamimageLabel = None
        Label(self.frame3,text="추천빌드",bg="#010A13",fg="white",font=(font.Font(size = 30 , weight='bold', family='Consolas'))).place(x=20,y=250)

        #프레임 4 주변 피시방 관련
        self.frame4 = Frame(self.notebook)
        Label(self.frame4, image=bg_image).place(x=0, y=0)
        self.notebook.add(self.frame4, text="주변 피시방 검색")
        GoogleMap(self.frame4,self.window)




        #프레임 1에 대한 변수들
        self.name = None
        self.person = None
        self.image = None

        #프로필 버튼들변수들
        self.profil_img = None
        self.profil_level = None
        self.profil_sololank = None
        self.profil_freelank = None
        self.profil_name = None




        # 비디오 이미지
        self.InitVideo()
        self.window.mainloop()



    def InitVideo(self):
        # 비디오 파일 열기
        self.video = cv2.VideoCapture(video_path)

        # 비디오 크기 가져오기
        width = int(self.video.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(self.video.get(cv2.CAP_PROP_FRAME_HEIGHT))

        # 비디오 프레임 표시할 레이블 생성
        self.vlabel = Label(self.frame1,width=800,height=400)
        self.vlabel.place(x=0,y=30)

        # 비디오 플레이어 시작
        self.show_frame()
    def show_frame(self):
        # 비디오 프레임 읽기
        ret, frame = self.video.read()

        if ret:
            # 프레임을 PIL 이미지로 변환
            image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            photo = ImageTk.PhotoImage(image)

            # 레이블에 이미지 표시
            self.vlabel.config(image=photo)
            self.vlabel.image = photo


        else:
            self.video.set(cv2.CAP_PROP_POS_FRAMES, 0)  # 비디오 위치를 처음으로 되돌림
         # 다음 프레임을 표시하기 위해 함수 재호출
        self.window.after(30, self.show_frame)











LOLGUI()

#캐릭터이름 넣으면 됨
#https://opgg-static.akamaized.net/meta/images/lol/champion/katarina.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto,f_webp,w_160&v=1685352893390
