class Player: #클래스 Player (플레이어와 딜러 객체 만들때 사용)

    def __init__(self,name):
        self.name = name
        self.cards = []     #Card 클래스 객체를 갖는 리스트
        self.number = []
        self.N = 0  #현재 갖고 있는 카드 개수

    def inHand(self):#손에 쥐고 있는 카드 개수
        return self.N

    def addCard(self,c): #인자 c: Card 클래스 객체
        self.cards.append(c)
        self.N += 1
    def addNumber(self,c):
        self.number.append(c)

    def reset(self):
        self.N = 0
        self.cards.clear() #점수 초기화
        self.number.clear()

    def value(self): # 점수를 계산해서 반환
        sum = 0
        onepair = []
        for x in self.cards:
            if x.value != 1:
                if x.value > 9:
                    sum += 10
                else:
                    sum += x.value
            else:
                onepair.append(x.value)
        if onepair is not None:
            for x in onepair:
                if sum + 11 > 21:
                    sum += 1
                else:
                    sum += 11
        return sum
    #우선 ace =11로 계산 2~10숫나는 그대로 합산, jqk는 10으로 계싼
    # 카드들의 점수를 합산하면서 ACE 카드 개수를 샌다
    #합산 결과가 21이 넘어가면 ACE 하나씩 1로 변경해서 21이 안넘을때까지

