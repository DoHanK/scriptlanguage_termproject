from tkinter import *
from tkinter import font
from winsound import *
from Card import *
from Player import*
import random

class Dori:
    def checkWinner(self):
        pass
        # if self.player.value() > 21:
        #     self.Lstatus.configure(text="Player Busts")
        #     PlaySound('BlackJack Resource/sounds/wrong.wav', SND_FILENAME)
        # elif self.dealer.value() > 21:
        #     self.Lstatus.configure(text="Dealer Busts")
        #     self.playerMoney += self.betMoney * 2
        #     PlaySound('BlackJack Resource/sounds/win.wav', SND_FILENAME)
        # elif self.dealer.value() == self.player.value():
        #     self.Lstatus.configure(text="Push")
        #     self.playerMoney += self.betMoney
        # elif self.dealer.value() < self.player.value():
        #     self.Lstatus.configure(text="You won!!")
        #     self.playerMoney += self.betMoney * 2
        #     PlaySound('BlackJack Resource/sounds/win.wav', SND_FILENAME)
        # else:
        #      self.Lstatus.configure(text="Sorry you lost!")


    def hitPlayer1(self,n):
        newCard = Card(self.cardDeck[self.deckN])
        self.deckN += 1
        self.player1.addCard(newCard)
        p = PhotoImage(file='GodoriCards/'+newCard.filename())
        self.LcardPlayer1.append(Label(self.window, image=p))
        self.LcardPlayer1[self.player1.inHand()-1].image = p
        self.LcardPlayer1[self.player1.inHand()-1].place(x=150+n*30, y=650)
        self.Lplayer1Pts.configure(text=str(self.player1.value()))
        #PlaySound('sounds/cardFilp1.wav',SND_FILENAME)

    def hitPlayer2(self,n):
        newCard = Card(self.cardDeck[self.deckN])
        self.deckN += 1
        self.player2.addCard(newCard)
        p = PhotoImage(file='GodoriCards/'+newCard.filename())
        self.LcardPlayer2.append(Label(self.window, image=p))
        self.LcardPlayer2[self.player2.inHand()-1].image = p
        self.LcardPlayer2[self.player2.inHand()-1].place(x=550+n*30, y=650)
        self.Lplayer2Pts.configure(text=str(self.player2.value()))
        #PlaySound('sounds/cardFilp1.wav',SND_FILENAME)

    def hitPlayer3(self,n):
        newCard = Card(self.cardDeck[self.deckN])
        self.deckN += 1
        self.player3.addCard(newCard)
        p = PhotoImage(file='GodoriCards/'+newCard.filename())
        self.LcardPlayer3.append(Label(self.window, image=p))
        self.LcardPlayer3[self.player3.inHand()-1].image = p
        self.LcardPlayer3[self.player3.inHand()-1].place(x=950+n*30, y=650)
        self.Lplayer3Pts.configure(text=str(self.player3.value()))
       # PlaySound('sounds/cardFilp1.wav',SND_FILENAME)

    def hitDealer(self,n):
        newCard = Card(self.cardDeck[self.deckN])
        self.deckN += 1
        self.dealer.addCard(newCard)
        p = PhotoImage(file='GodoriCards/'+newCard.filename())
        self.LcardDealer.append(Label(self.window, image=p))
        self.LcardDealer[self.dealer.inHand() - 1].image = p
        self.LcardDealer[self.dealer.inHand() - 1].place(x=550 + n * 30, y=250)
        #PlaySound('sounds/cardFilp1.wav', SND_FILENAME)
    def deal(self):
        if self.cards == 0:
            random.shuffle(self.cardDeck)
            self.hitPlayer1(0)
            self.hitPlayer2(0)
            self.hitPlayer3(0)
            self.hitDealer(0)
            self.cards = 1
        elif self.cards == 1:
            self.hitPlayer1(1)
            self.hitPlayer1(2)
            self.hitPlayer1(3)
            self.hitPlayer2(1)
            self.hitPlayer2(2)
            self.hitPlayer2(3)
            self.hitPlayer3(1)
            self.hitPlayer3(2)
            self.hitPlayer3(3)
            self.hitDealer(1)
            self.hitDealer(2)
            self.hitDealer(3)
            self.cards = 4
        else:
            self.hitPlayer1(4)
            self.hitPlayer2(4)
            self.hitPlayer3(4)
            self.hitDealer(4)
            self.cards = 5
        if self.cards == 5:
            self.checkWinner()





    def pressedP1B5(self):
        self.Deal['state'] = 'active'
        self.Deal['bg'] = 'white'
        self.P1betMoney += 5
        if self.playerMoney >= 5:
            self.LP1betMoney.configure(text= str(self.P1betMoney)+"만")
            self.playerMoney -= 5
            self.LplayerMoney.configure(text=str(self.playerMoney)+"만")
            #PlaySound('BlackJack Resource/sounds/chip.wav', SND_FILENAME)
        else:
            self.betMoney -= 5
    def pressedP1B1(self):
        self.Deal['state'] = 'active'
        self.Deal['bg'] = 'white'
        self.P1betMoney += 1
        if self.playerMoney >= 1:
            self.LP1betMoney.configure(text=str(self.P1betMoney) + "만")
            self.playerMoney -= 1
            self.LplayerMoney.configure(text=str(self.playerMoney) + "만")
            # PlaySound('BlackJack Resource/sounds/chip.wav', SND_FILENAME)
        else:
            self.betMoney -= 1
    def pressedP2B5(self):
        self.Deal['state'] = 'active'
        self.Deal['bg'] = 'white'
        self.P2betMoney += 5
        if self.playerMoney >= 5:
            self.LP2betMoney.configure(text=str(self.P2betMoney) + "만")
            self.playerMoney -= 5
            self.LplayerMoney.configure(text=str(self.playerMoney) + "만")
            # PlaySound('BlackJack Resource/sounds/chip.wav', SND_FILENAME)
        else:
            self.betMoney -= 5
    def pressedP2B1(self):
        self.Deal['state'] = 'active'
        self.Deal['bg'] = 'white'
        self.P2betMoney += 1
        if self.playerMoney >= 1:
            self.LP2betMoney.configure(text=str(self.P2betMoney) + "만")
            self.playerMoney -= 1
            self.LplayerMoney.configure(text=str(self.playerMoney) + "만")
            # PlaySound('BlackJack Resource/sounds/chip.wav', SND_FILENAME)
        else:
            self.betMoney -= 1
    def pressedP3B5(self):
        self.Deal['state'] = 'active'
        self.Deal['bg'] = 'white'
        self.P3betMoney += 5
        if self.playerMoney >= 5:
            self.LP3betMoney.configure(text=str(self.P3betMoney) + "만")
            self.playerMoney -= 5
            self.LplayerMoney.configure(text=str(self.playerMoney) + "만")
            # PlaySound('BlackJack Resource/sounds/chip.wav', SND_FILENAME)
        else:
            self.betMoney -= 5
    def pressedP3B1(self):
        self.Deal['state'] = 'active'
        self.Deal['bg'] = 'white'
        self.P3betMoney += 1
        if self.playerMoney >= 1:
            self.LP3betMoney.configure(text=str(self.P3betMoney) + "만")
            self.playerMoney -= 1
            self.LplayerMoney.configure(text=str(self.playerMoney) + "만")
            # PlaySound('BlackJack Resource/sounds/chip.wav', SND_FILENAME)
        else:
            self.betMoney -= 1
    def pressedDeal(self):
        self.Deal['state'] = 'disable'
        self.Deal['bg'] = 'gray'
        if self.cards == 0:
            self.P1B5['state'] = 'active'
            self.P1B5['bg'] = 'white'
            self.P1B1['state'] = 'active'
            self.P1B1['bg'] = 'white'
            self.P2B5['state'] = 'active'
            self.P2B5['bg'] = 'white'
            self.P2B1['state'] = 'active'
            self.P2B1['bg'] = 'white'
            self.P3B5['state'] = 'active'
            self.P3B5['bg'] = 'white'
            self.P3B1['state'] = 'active'
            self.P3B1['bg'] = 'white'
            self.Deal['state'] = 'disabled'
            self.Deal['bg'] = 'gray'
        elif self.cards == 4:
            self.P1B5['state'] = 'disable'
            self.P1B5['bg'] = 'gray'
            self.P1B1['state'] = 'disable'
            self.P1B1['bg'] = 'gray'
            self.P2B5['state'] = 'disable'
            self.P2B5['bg'] = 'gray'
            self.P2B1['state'] = 'disable'
            self.P2B1['bg'] = 'gray'
            self.P3B5['state'] = 'disable'
            self.P3B5['bg'] = 'gray'
            self.P3B1['state'] = 'disable'
            self.P3B1['bg'] = 'gray'
            self.Deal['state'] = 'disabled'
            self.Deal['bg'] = 'gray'
            self.Again['state'] = 'active'
            self.Again['bg'] = 'white'

        self.deal()

    def pressedAgain(self):
        self.cards = 0
        self.P1B5['state'] = 'disabled'
        self.P1B5['bg'] = 'gray'
        self.P1B1['state'] = 'disabled'
        self.P1B1['bg'] = 'gray'
        self.P2B5['state'] = 'disabled'
        self.P2B5['bg'] = 'gray'
        self.P2B1['state'] = 'disabled'
        self.P2B1['bg'] = 'gray'
        self.P3B5['state'] = 'disabled'
        self.P3B5['bg'] = 'gray'
        self.P3B1['state'] = 'disabled'
        self.P3B1['bg'] = 'gray'
        self.Again['state'] = 'disabled'
        self.Again['bg'] = 'gray'
        self.Deal['state'] = 'active'
        self.Deal['bg'] = 'white'

        for x in self.LcardPlayer1:
            x.destroy()
        for x in self.LcardPlayer2:
            x.destroy()
        for x in self.LcardPlayer3:
            x.destroy()
        for x in self.LcardDealer:
            x.destroy()
        self.P1Lstatus.configure(text="")
        self.P2Lstatus.configure(text="")
        self.P3Lstatus.configure(text="")

        self.LcardPlayer1 = []
        self.LcardPlayer2 = []
        self.LcardPlayer3 = []
        self.LcardDealer = []
        self.nCardsPlayer1 = 0 #플레이어 카드 위치변수
        self.nCardsPlayer2 = 0 #플레이어 카드 위치변수
        self.nCardsPlayer3 = 0 #플레이어 카드 위치변수
        self.nCardsDealer = 0 #딜러 카드 위치 변수
        self.P1betMoney = 0
        self.P2betMoney = 0
        self.P3betMoney = 0
        self.LP1betMoney.configure(text = str(self.P1betMoney)+'만')
        self.LP2betMoney.configure(text= str(self.P2betMoney)+'만')
        self.LP3betMoney.configure(text=str(self.P3betMoney)+'만')
        self.LplayerMoney.configure(text=str(self.playerMoney)+'만')
        self.player1.reset()
        self.player2.reset()
        self.player3.reset()
        self.dealer.reset()
        self.deckN = 0

    def setupButton(self):
        self.P1B5 =Button(self.window,text='Bet 5만',width=10,height=2,font =self.fontstyle2,command=self.pressedP1B5)
        self.P1B5.place(x=100,y=950)
        self.P1B1 =Button(self.window,text='Bet 1만',width=10,height=2,font =self.fontstyle2,command=self.pressedP1B1)
        self.P1B1.place(x=250,y=950)
        self.P2B5 =Button(self.window,text='Bet 5만',width=10,height=2,font =self.fontstyle2,command=self.pressedP2B5)
        self.P2B5.place(x=500,y=950)
        self.P2B1 = Button(self.window, text='Bet 1만', width=10, height=2, font=self.fontstyle2, command=self.pressedP2B1)
        self.P2B1.place(x=650, y=950)
        self.P3B5 = Button(self.window, text='Bet 5만', width=10, height=2, font=self.fontstyle2, command=self.pressedP3B5)
        self.P3B5.place(x=900, y=950)
        self.P3B1 = Button(self.window, text='Bet 1만', width=10, height=2, font=self.fontstyle2, command=self.pressedP3B1)
        self.P3B1.place(x=1050, y=950)
        self.Deal =Button(self.window,text='Deal',width=10,height=2,font =self.fontstyle2,command=self.pressedDeal)
        self.Deal.place(x=1250,y=950)
        self.Again =Button(self.window,text='Again',width=10,height=2,font =self.fontstyle2,command=self.pressedAgain)
        self.Again.place(x=1400,y=950)
        self.P1B5['state'] = 'disabled'
        self.P1B5['bg'] = 'gray'
        self.P1B1['state'] = 'disabled'
        self.P1B1['bg'] = 'gray'
        self.P2B5['state'] = 'disabled'
        self.P2B5['bg'] = 'gray'
        self.P2B1['state'] = 'disabled'
        self.P2B1['bg'] = 'gray'
        self.P3B5['state'] = 'disabled'
        self.P3B5['bg'] = 'gray'
        self.P3B1['state'] = 'disabled'
        self.P3B1['bg'] = 'gray'
        self.Again['state'] = 'disabled'
        self.Again['bg'] = 'gray'

    def setupLabel(self):
        self.LP1betMoney = Label(text='0만',width=7,height=1,font=self.fontstyle,bg='#2B652E',fg='yellow')
        self.LP1betMoney.place(x=200,y=900)

        self.LP2betMoney = Label(text='0만', width=7, height=1, font=self.fontstyle, bg='#2B652E', fg='yellow')
        self.LP2betMoney.place(x=600, y=900)

        self.LP3betMoney = Label(text='0만', width=7, height=1, font=self.fontstyle, bg='#2B652E', fg='yellow')
        self.LP3betMoney.place(x=1000, y=900)

        self.LplayerMoney = Label(text='1000만', width=7, height=1, font=self.fontstyle, bg='#205928', fg='yellow')
        self.LplayerMoney.place(x=1400, y=900)

        self.P1card1 = Label(text='', width=1, height=1, font=self.fontstyle, bg='green', fg='white')
        self.P1card1.place(x=100, y=800)
        self.P1card2 = Label(text='', width=1, height=1, font=self.fontstyle, bg='green', fg='white')
        self.P1card2.place(x=500, y=300)
        self.P1card3 = Label(text='', width=1, height=1, font=self.fontstyle, bg='green', fg='white')
        self.P1card3.place(x=500, y=300)
        self.P1card4 = Label(text='', width=1, height=1, font=self.fontstyle, bg='green', fg='white')
        self.P1card4.place(x=500, y=300)
        self.P1card5 = Label(text='', width=1, height=1, font=self.fontstyle, bg='green', fg='white')
        self.P1card5.place(x=500, y=300)

        self.P2card1 = Label(text='', width=1, height=1, font=self.fontstyle, bg='green', fg='white')
        self.P2card1.place(x=500, y=300)
        self.P2card2 = Label(text='', width=1, height=1, font=self.fontstyle, bg='green', fg='white')
        self.P2card2.place(x=500, y=300)
        self.P2card3 = Label(text='', width=1, height=1, font=self.fontstyle, bg='green', fg='white')
        self.P2card3.place(x=500, y=300)
        self.P2card4 = Label(text='', width=1, height=1, font=self.fontstyle, bg='green', fg='white')
        self.P2card4.place(x=500, y=300)
        self.P2card5 = Label(text='', width=1, height=1, font=self.fontstyle, bg='green', fg='white')
        self.P2card5.place(x=500, y=300)

        self.P3card1 = Label(text='', width=1, height=1, font=self.fontstyle, bg='green', fg='white')
        self.P3card1.place(x=500, y=300)
        self.P3card2 = Label(text='', width=1, height=1, font=self.fontstyle, bg='green', fg='white')
        self.P3card2.place(x=500, y=300)
        self.P3card3 = Label(text='', width=1, height=1, font=self.fontstyle, bg='green', fg='white')
        self.P3card3.place(x=500, y=300)
        self.P3card4 = Label(text='', width=1, height=1, font=self.fontstyle, bg='green', fg='white')
        self.P3card4.place(x=500, y=300)
        self.P3card5 = Label(text='', width=1, height=1, font=self.fontstyle, bg='green', fg='white')
        self.P3card5.place(x=500, y=300)

        self.Dcard1 = Label(text='', width=1, height=1, font=self.fontstyle, bg='green', fg='white')
        self.Dcard1.place(x=500, y=300)
        self.Dcard2 = Label(text='', width=1, height=1, font=self.fontstyle, bg='green', fg='white')
        self.Dcard2.place(x=500, y=300)
        self.Dcard3 = Label(text='', width=1, height=1, font=self.fontstyle, bg='green', fg='white')
        self.Dcard3.place(x=500, y=300)
        self.Dcard4 = Label(text='', width=1, height=1, font=self.fontstyle, bg='green', fg='white')
        self.Dcard4.place(x=500, y=300)
        self.Dcard5 = Label(text='', width=1, height=1, font=self.fontstyle, bg='green', fg='white')
        self.Dcard5.place(x=500, y=300)

        self.Lplayer1Pts = Label(text='', width=6, height=1, font=self.fontstyle, bg='green', fg='white')
        self.Lplayer1Pts.place(x=300, y=300)

        self.Lplayer2Pts = Label(text='', width=6, height=1, font=self.fontstyle, bg='green', fg='white')
        self.Lplayer2Pts.place(x=300, y=300)

        self.Lplayer3Pts = Label(text='', width=6, height=1, font=self.fontstyle, bg='green', fg='white')
        self.Lplayer3Pts.place(x=300, y=300)

        self.LDealerPts = Label(text='', width=6, height=1, font=self.fontstyle, bg='green', fg='white')
        self.LDealerPts.place(x=300, y=300)

        self.P1Lstatus = Label(text='', width=15, height=1, font=self.fontstyle, bg='green', fg='white')
        self.P1Lstatus.place(x=500, y=300)

        self.P2Lstatus = Label(text='', width=15, height=1, font=self.fontstyle, bg='green', fg='white')
        self.P2Lstatus.place(x=500, y=300)

        self.P3Lstatus = Label(text='', width=15, height=1, font=self.fontstyle, bg='green', fg='white')
        self.P3Lstatus.place(x=500, y=300)


    def __init__(self):
        self.window = Tk()
        self.window.title('도리짓고 땡')
        self.window.geometry('1625x1081')
        p = PhotoImage(file='GodoriCards/table.gif')
        label = Label(self.window,image=p)
        label.place(x=-2,y=-2)
        self.fontstyle = font.Font(self.window, size=24, weight='bold',family='굴림체')
        self.fontstyle2 = font.Font(self.window, size=16, weight='bold',family='굴림체')
        self.setupButton()
        self.setupLabel()

        self.cards = 0
        self.player1 = Player('player1')
        self.player2 = Player('player2')
        self.player3 = Player('player3')
        self.dealer = Player('dealer')
        self.P1betMoney = 0 #배팅 머니 변수
        self.P2betMoney = 0 #배팅 머니 변수
        self.P3betMoney = 0 #배팅 머니 변수
        self.playerMoney = 1000 #플레이어가 갖고 있는 머니 변수
        self.nCardsPlayer1 = 0 #플레이어 카드 위치변수
        self.nCardsPlayer2 = 0 #플레이어 카드 위치변수
        self.nCardsPlayer3 = 0 #플레이어 카드 위치변수
        self.nCardsDealer = 0 #딜러 카드 위치 변수
        self.LcardPlayer1 = [] #플레이어 카드 이미지 라벨들을 갖는 리스트
        self.LcardPlayer2 = [] #플레이어 카드 이미지 라벨들을 갖는 리스트
        self.LcardPlayer3 = [] #플레이어 카드 이미지 라벨들을 갖는 리스트
        self.LcardDealer = []
        self.cardDeck =[i for i in range(40)]
        self.deckN = 0 #카드덱에서 몇번째 숫자를 선택하느냐 나타내는 변수
        self.window.mainloop()


Dori()