class Player: #클래스 Player (플레이어와 딜러 객체 만들때 사용)

    def __init__(self,name):
        self.name = name
        self.cards = []     #Card 클래스 객체를 갖는 리스트
        self.number = []
        self.cardtype = []
        self.N = 0  #현재 갖고 있는 카드 개수
        self.made = ''
        self.Lpedi = ''
        self.pedigree = -1
        self.made_card = [0,0,0,0,0]

    def inHand(self):#손에 쥐고 있는 카드 개수
        return self.N

    def addCard(self,c): #인자 c: Card 클래스 객체
        self.cards.append(c)
        self.N += 1
    def addNumber(self,c):
        self.number.append(c)
    def addCardtype(self,c):
        self.cardtype.append(c)
    def reset(self):
        self.N = 0
        self.cards.clear() #점수 초기화
        self.number.clear()
        self.cardtype.clear()
        self.made = ''
        self.Lpedi = ''
        self.pedigree = -1
        self.made_card = [0, 0, 0, 0, 0]


