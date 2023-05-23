
import requests
from bs4 import BeautifulSoup

def pushbackscr(s):#프로필 짤라주는 함수
    return s[30:len(s)-3]

def pushbacklevel(s):
    return  s[len('<span class="level">'):len(s)-len('</span>')]


num = '3424'
class user:
    def __init__(self ,name):


        url = 'https://www.op.gg/summoners/kr/'+name
        hdr = {'Accept-Language': 'ko_KR,en;q=0.8', 'User-Agent': (
            'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Mobile Safari/537.36')}
        req = requests.get(url, headers=hdr)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        info = str(soup.text)
        print(info)
        pmid = info.find("종합")
        psolo = info.find("솔로랭크")
        pfree = info.find("자유랭크")
        self.sololank = info[psolo:pfree]
        self.freelank = info[pfree:pmid]

        print(self.sololank)
        print(self.freelank)

        #파씽을 통해 사용자 프로필 받아오기
        self.profil_pic = pushbackscr(str(*soup.select('#__next > div.css-uclu8m.eioz'+num+' > div.summary > div > div.face > div > img')))
        #레벨 불러오기
        self.level =pushbacklevel(str(*soup.select('#__next > div.css-uclu8m.eioz'+num+' > div.summary > div > div.face > div > div > span')))
        self.name = name


    def getsololank(self):
        return self.sololank

    def getfreelank(self):
        return self.freelank

    def getprofileurl(self):
        return self.profil_pic

    def getlevel(self):
        return self.level

