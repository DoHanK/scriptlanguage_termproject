
import requests
from bs4 import BeautifulSoup

def pushbackscr(s):#프로필 짤라주는 함수
    return s[30:len(s)-3]

def pushbacklevel(s):
    return  s[len('<span class="level">'):len(s)-len('</span>')]


num = '3424'
class Items:
    def __init__(self ,name):


        url = "https://www.op.gg/champions/"+name+"/top/build"
        hdr = {'Accept-Language': 'ko_KR,en;q=0.8', 'User-Agent': (
            'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Mobile Safari/537.36')}
        req = requests.get(url, headers=hdr)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        info = str(soup.text)


        #파씽을 통해 사용자 프로필 받아오기
        self.itemsource= str(*soup.select('#__next > div.css-0.ey0mjkm0'))
        for x in range(4):
            self.itemsource =self.itemsource[self.itemsource.find("추천 빌드")+len("추천 빌드"):]
        scr = []
        for x in range(3):
            p = self.itemsource.find('width=')
            temp = self.itemsource[self.itemsource.find("src="):p]
            self.itemsource = self.itemsource[p+len('width='):]
            scr.append(temp)

        self.itemurl =[]

        for x in scr:
            x.replace("'",'"')
            self.itemurl.append(x[5:-2])

    def geturl(self):
        return self.itemurl

# user("garen")
#katarina