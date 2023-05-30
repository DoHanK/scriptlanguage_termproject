from tkinter import *
from tkinter import messagebox
import webbrowser
from PIL import Image, ImageTk
import requests
import io
from tkinter import font


class GoogleMap():
    def __init__(self,frame,window):
        # Tkinter 윈도우 생성
        self.TempFont = font.Font(size=13, weight='bold', family='Consolas')
        self.frame = frame
        # 레이블 및 입력 상자 추가
        self.label_location = Label(self.frame, fg="white",width=24 ,height=1,bg="#330303", text="지역 입력",font=self.TempFont)
        self.label_location.place(x=20,y=30)
        self.entry_location = Entry(self.frame ,fg="white",bg="#330303",font=font.Font(size=15, weight='bold', family='Consolas'))
        self.entry_location.place(x= 20,y=60)

        # 검색 버튼 추가
        self.button_search = Button(self.frame, text="검색",width=5 ,height=3, fg="white",bg="#330303",font=font.Font(size=11, weight='bold', family='Consolas'),command=self.search_pc_bang)
        self.button_search.place(x=250, y= 25)
        self.selected_index = 0
        # PC방 리스트 박스 추가
        Label(self.frame, fg="white", bg="#330303",width=30 ,height=1, text="피시방리스트",font=font.Font(size=13, weight='bold', family='Consolas')).place(x=400,y=35)
        self.listbox_pc_bangs = Listbox(self.frame,width=65 ,height=14, fg="white",bg="#330303", selectbackground="#010A13")
        self.listbox_pc_bangs.place(x=310,y=75)

        # PC방 선택 이벤트 바인딩
        self.listbox_pc_bangs.bind("<<ListboxSelect>>", self.select_pc_bang)

        # 위치 정보 레이블 추가
        self.label_location_info = Label(self.frame, fg="white",bg="#010A13", text="")
        self.label_location_info.place(x=310,y=315)

        # 위치보기 버튼 추가
        self.button_show_location = Button(self.frame,width= 30 ,height=15, fg="white",bg="#330303", text="위치보기", command=self.show_location)
        self.button_show_location.place(x=20, y=100)

        self.pcsubwindow = None
        self.subframe = None
        self.window = window

        self.label_map = None

    def select_pc_bang(self,event):
        # 선택된 PC방의 인덱스 가져오기
        index = self.listbox_pc_bangs.curselection()
        # 선택된 PC방이 있는 경우
        if index:
            # 이전에 선택된 항목의 색상 초기화
            self.listbox_pc_bangs.itemconfig(self.selected_index,fg="white", bg="#330303")

            # 선택된 PC방의 인덱스 저장
            self.selected_index = index[0]

            # 선택된 PC방의 색상 변경
            self.listbox_pc_bangs.itemconfig(self.selected_index,fg="white", bg="black")

    def on_subwindow_close(self):
        self.pcsubwindow.destroy()
        self.label_map =None
        self.pcsubwindow = None
        self.subframe = None

    def show_google_map(self,latitude, longitude):
        global image_tk, zoom # image_tk를 전역 변수로 선언

        if self.pcsubwindow == None:
            self.pcsubwindow = Toplevel(self.window)
            self.pcsubwindow.title("PC방 위치")
            self.pcsubwindow.geometry("400x400+800+250")
            self.pcsubwindow.protocol("WM_DELETE_WINDOW", self.on_subwindow_close)


        # Google Maps Static API URL for the map image
        api_key = "AIzaSyAAe90xo8B26j_5bne0HAU0cS1IQDQUP5s"
        zoom = 15
        size = "400x400"
        markers = f"color:red%7C{latitude},{longitude}"
        map_url = f"https://maps.googleapis.com/maps/api/staticmap?center={latitude},{longitude}&zoom={zoom}&size={size}&key={api_key}&markers={markers}"

        # 지도 이미지 로드 및 표시
        image_data = requests.get(map_url).content
        image = Image.open(io.BytesIO(image_data))
        image_tk = ImageTk.PhotoImage(image)
        if self.label_map == None:
            self.label_map = Label(self.pcsubwindow, image=image_tk)
            self.label_map.place(x=0,y=0)
        else:
            self.label_map.configure(image=image_tk)

        self.pcsubwindow.mainloop()
        def zoom_in():
            global zoom
            zoom += 1
            update_map()

        def zoom_out():
            global zoom
            zoom -= 1
            update_map()

        def update_map():
            nonlocal map_url
            image_data = requests.get(map_url).content
            image = Image.open(io.BytesIO(image_data))
            image_tk = ImageTk.PhotoImage(image)
            self.label_map.configure(image=image_tk)
            self.label_map.image = image_tk

            # Create zoom buttons

        btn_zoom_in = Button(self.frame, text="Zoom In", command = zoom_in)
        btn_zoom_in.place(x=400,y=400)
        btn_zoom_out = Button(self.frame, text="Zoom Out", command=zoom_out)
        btn_zoom_out.place(x=400,y=500)

    def show_location(self):



        location = self.listbox_pc_bangs.get(self.selected_index)
        # PC방 검색 API 호출
        api_key = "AIzaSyAAe90xo8B26j_5bne0HAU0cS1IQDQUP5s"  # Google Maps Places API 키
        url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query=pc방+{location}&key={api_key}"

        try:
            response = requests.get(url)
            data = response.json()

            results = data["results"]
            if not results:
                messagebox.showinfo("알림", "PC방 위치를 찾을 수 없습니다.")
            else:
                lat = results[0]["geometry"]["location"]["lat"]
                lng = results[0]["geometry"]["location"]["lng"]
                location_info = f"위도: {lat}\n경도: {lng}"
                self.label_location_info.config(text=location_info)
                self.show_google_map(lat, lng)

        except requests.exceptions.RequestException:
            messagebox.showerror("오류", "PC방 위치 검색에 실패하였습니다.")


    def search_pc_bang(self):
        location = self.entry_location.get()

        if location == "":
            messagebox.showwarning("경고", "지역을 입력하세요.")
            return

        # PC방 검색 API 호출
        api_key = "AIzaSyAAe90xo8B26j_5bne0HAU0cS1IQDQUP5s"  # Google Maps Places API 키
        url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query=pc방+{location}&key={api_key}"

        try:
            response = requests.get(url)
            data = response.json()

            results = data["results"]
            if not results:
                messagebox.showinfo("알림", "해당 지역에서 PC방을 찾을 수 없습니다.")
            else:
                pc_bangs = [result["name"] for result in results]
                # messagebox.showinfo("PC방 목록", "\n".join(pc_bangs))

                # PC방 리스트를 Tkinter 창에 추가
                self.listbox_pc_bangs.delete(0, END)
                for pc_bang in pc_bangs:
                    self.listbox_pc_bangs.insert(END, pc_bang)

        except requests.exceptions.RequestException:
            messagebox.showerror("오류", "PC방 검색에 실패하였습니다.")



