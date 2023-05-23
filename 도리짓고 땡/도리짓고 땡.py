from tkinter import *
from tkinter import font
from winsound import *
from Card import *
from Player import*
import random

class Dori:
    def checkPedi(self, p, n1,n2,n3):
        made_list = []
        sub_list = []
        sub_pedi = 0
        f_n1 = -1
        f_n2 = -1
        f_n3 = -1
        if n1 == n2:
            for x in range(len(p.cardtype)):
                if p.cardtype[x] == n1:
                    if f_n1 == -1:
                        made_list.append(x)
                        f_n1 = x
                    elif f_n2 == -1:
                        made_list.append(x)
                        f_n2 = x
                        if p.number[f_n1] > p.number[f_n2]:
                            f_n1, f_n2 = f_n2, f_n1
                    else:
                        if p.number[f_n1] < p.number[x]:
                            made_list.remove(f_n1)
                            f_n1 = x
                            made_list.append(x)

                elif p.cardtype[x] == n3:
                    if f_n3 == -1:
                        made_list.append(x)
                        f_n3 = x
                    elif p.number[x] >= p.number[f_n3]:
                        made_list.remove(f_n3)
                        f_n3 = x
                        made_list.append(x)
        else:
            for x in range(len(p.cardtype)):
                if p.cardtype[x] == n1:
                    if f_n1 == -1:
                        made_list.append(x)
                        f_n1 = x
                    elif p.number[x] >= p.number[f_n1]:
                        made_list.remove(f_n1)
                        f_n1 = x
                        made_list.append(x)
                elif p.cardtype[x] == n2:
                    if f_n2 == -1:
                        made_list.append(x)
                        f_n2 = x
                    elif p.number[x] >= p.number[f_n2]:
                        made_list.remove(f_n2)
                        f_n2 = x
                        made_list.append(x)
                elif p.cardtype[x] == n3:
                    if f_n3 == -1:
                        made_list.append(x)
                        f_n3 = x
                    elif p.number[x] >= p.number[f_n3]:
                        made_list.remove(f_n3)
                        f_n3 = x
                        made_list.append(x)
        for x in range(len(p.number)):
            if made_list.count(x) == 0:
                sub_list.append(p.number[x])

        # 족보체크
        # 끗 : 0 ~ 9
        # 땡 : 10 ~ 19
        # 광땡 : 113, 118, 138
        sub_list.sort()
        x = sub_list[0]
        y = sub_list[1]

        if x // 4 == 0 and x % 4 == 0:
            if y // 4 == 2 and y % 4 == 0:
                sub_pedi = 113
            if y // 4 == 7 and y % 4 == 0:
                sub_pedi = 118
        elif x // 4 == 2 and x % 4 == 0:
            if y // 4 == 7 and y % 4 == 0:
                sub_pedi =  138
        elif x // 4 == y // 4:
            sub_pedi = 10 + x // 4
        else:
            sub_pedi = ((x//4 + y//4)+2) % 10

        if sub_pedi > p.pedigree:
            for x in range(5):
                p.made_card[x] = 0
            p.pedigree = sub_pedi
            for x in made_list:
                p.made_card[x] = 1
            if 0 <= sub_pedi <=9:
                if sub_pedi == 9:
                    p.Lpedi = ' 갑오'
                elif sub_pedi == 0:
                    p.Lpedi = ' 망통'
                else:
                    p.Lpedi = " " + str(sub_pedi) + "끗"
            elif 10 <= sub_pedi <= 19:
                p.Lpedi = " " + str((sub_pedi % 10) + 1) + '땡'
            elif sub_pedi == 113:
                p.Lpedi = ' 13광땡'
            elif sub_pedi == 118:
                p.Lpedi = ' 18광땡'
            elif sub_pedi == 138:
                p.Lpedi = ' 38광땡'
            return True
        return False



    def checkMade(self, p):
        sub_pedi = 0
        if p.cardtype.count(1) >= 2:
            if p.cardtype.count(8) >= 1:
                p.made = '콩콩팓(1 1 8)'
                p.pedigree = self.checkPedi(p, 1, 1, 8)
        if p.cardtype.count(1) >= 1:
            if p.cardtype.count(2) >= 1:
                if p.cardtype.count(7) >= 1:
                    if self.checkPedi(p,1,2,7):
                        p.made = '삐리칠(1 2 7)'
            if p.cardtype.count(3) >= 1:
                if p.cardtype.count(6) >= 1:
                    if self.checkPedi(p, 1, 3, 6):
                        p.made = '물삼육(1 3 6)'
            if p.cardtype.count(4) >= 1:
                if p.cardtype.count(5) >= 1:
                    if self.checkPedi(p,1,4,5):
                        p.made = '빽새오(1 4 5)'
            if p.cardtype.count(9) >= 1:
                if p.cardtype.count(10) >= 1:
                    if self.checkPedi(p,1,9,10):
                        p.made = '삥구장(1 9 10)'
        if p.cardtype.count(2) >= 1:
            if p.cardtype.count(2) >= 2:
                if p.cardtype.count(6) >= 1:
                    if  self.checkPedi(p,2,2,6):
                        p.made = '니니육(2 2 6)'
            if p.cardtype.count(3) >= 1:
                if p.cardtype.count(5) >= 1:
                    if  self.checkPedi(p,2,3,5):
                        p.made = '이삼오(2 3 5)'
            if p.cardtype.count(8) >= 1:
                if p.cardtype.count(10) >= 1:
                    if  self.checkPedi(p,2,8,10):
                        p.made = '이판장(2 8 10)'
        if p.cardtype.count(3) >= 1:
            if p.cardtype.count(3) >= 2:
                if p.cardtype.count(4) >= 1:
                    if  self.checkPedi(p,3,3,4):
                        p.made = '심심새(3 3 4)'
            if p.cardtype.count(7) >= 1:
                if p.cardtype.count(10) >= 1:
                    if  self.checkPedi(p,3,7,10):
                        p.made = '삼칠장(3 7 10)'
            if p.cardtype.count(8) >= 1:
                if p.cardtype.count(9) >= 1:
                    if  self.checkPedi(p,3,8,9):
                        p.made = '삼빡구(3 8 9)'
        if p.cardtype.count(4) >= 1:
            if p.cardtype.count(4) >= 2:
                if p.cardtype.count(2) >= 1:
                    if self.checkPedi(p,4,4,2):
                        p.made = '살살이(4 4 2)'
            if p.cardtype.count(6) >= 1:
                if p.cardtype.count(10) >= 1:
                    if self.checkPedi(p,4,6,10) :
                        p.made = '사륙장(4 6 10)'
            if p.cardtype.count(7) >= 1:
                if p.cardtype.count(9) >= 1:
                    if  self.checkPedi(p,4,7,9):
                        p.made = '사칠구(4 7 9)'
        if p.cardtype.count(5) >= 1:
            if p.cardtype.count(5) >= 2:
                if p.cardtype.count(10) >= 1:
                    if self.checkPedi(p,5,5,10):
                        p.made = '꼬꼬장(5 5 10)'
            if p.cardtype.count(6) >= 1:
                if p.cardtype.count(9) >= 1:
                    if  self.checkPedi(p,5,6,9):
                        p.made = '오륙구(5 6 9)'
            if p.cardtype.count(7) >= 1:
                if p.cardtype.count(8) >= 1:
                    if self.checkPedi(p,5,7,8):
                        p.made = '오리발(5 7 8)'
        if p.cardtype.count(6) >= 2:
            if p.cardtype.count(8) >= 1:
                if  self.checkPedi(p, 6, 6, 8):
                    p.made = '쭉쭉팔(6 6 8)'
        if p.cardtype.count(7) >= 2:
            if p.cardtype.count(6) >= 1:
                if  self.checkPedi(p, 7, 7,6):
                    p.made = '철철육(7 7 6)'
        if p.cardtype.count(8) >= 2:
            if p.cardtype.count(4) >= 1:
                if  self.checkPedi(p, 8, 8, 4):
                    p.made = '팍팍싸(8 8 4)'
        if p.cardtype.count(9) >= 2:
            if p.cardtype.count(2) >= 1:
                if  self.checkPedi(p, 9, 9, 2):
                    p.made = '구구리(9 9 2)'
        if p.pedigree == -1:
            p.made = '노 메이드'

    def checkWinner(self):
        self.checkMade(self.player1)
        self.checkMade(self.player2)
        self.checkMade(self.player3)
        self.checkMade(self.dealer)

        if self.player1.pedigree != -1:
            for x in range(5):
                if self.player1.made_card[x] == 1:
                    self.LcardPlayer1[x].place(x=80 + x * 70, y=690)
                    if x == 0:
                        self.P1card1.configure(text=str(self.player1.number[0] // 4 + 1), fg='yellow')
                    elif x == 1:
                        self.P1card2.configure(text=str(self.player1.number[1] // 4 + 1), fg='yellow')
                    elif x == 2:
                        self.P1card3.configure(text=str(self.player1.number[2] // 4 + 1), fg='yellow')
                    elif x == 3:
                        self.P1card4.configure(text=str(self.player1.number[3] // 4 + 1), fg='yellow')
                    elif x == 4:
                        self.P1card5.configure(text=str(self.player1.number[4] // 4 + 1), fg='yellow')
        if self.player2.pedigree != -1:
            for x in range(5):
                if self.player2.made_card[x] == 1:
                    self.LcardPlayer2[x].place(x=480 + x * 70, y=690)
                    if x == 0:
                        self.P2card1.configure(text=str(self.player2.number[0] // 4 + 1), fg='yellow')
                    elif x == 1:
                        self.P2card2.configure(text=str(self.player2.number[1] // 4 + 1), fg='yellow')
                    elif x == 2:
                        self.P2card3.configure(text=str(self.player2.number[2] // 4 + 1), fg='yellow')
                    elif x == 3:
                        self.P2card4.configure(text=str(self.player2.number[3] // 4 + 1), fg='yellow')
                    elif x == 4:
                        self.P2card5.configure(text=str(self.player2.number[4] // 4 + 1), fg='yellow')
        if self.player3.pedigree != -1:
            for x in range(5):
                if self.player3.made_card[x] == 1:
                    self.LcardPlayer3[x].place(x=880 + x * 70, y=690)
                    if x == 0:
                        self.P3card1.configure(text=str(self.player3.number[0] // 4 + 1), fg='yellow')
                    elif x == 1:
                        self.P3card2.configure(text=str(self.player3.number[1] // 4 + 1), fg='yellow')
                    elif x == 2:
                        self.P3card3.configure(text=str(self.player3.number[2] // 4 + 1), fg='yellow')
                    elif x == 3:
                        self.P3card4.configure(text=str(self.player3.number[3] // 4 + 1), fg='yellow')
                    elif x == 4:
                        self.P3card5.configure(text=str(self.player3.number[4] // 4 + 1), fg='yellow')
        if self.dealer.pedigree != -1:
            for x in range(5):
                if self.dealer.made_card[x] == 1:
                    self.LcardDealer[x].place(x=480 + x * 70, y=290)
                    if x == 0:
                        self.Dcard1.configure(text=str(self.dealer.number[0] // 4 + 1), fg='yellow')
                    elif x == 1:
                        self.Dcard2.configure(text=str(self.dealer.number[1] // 4 + 1), fg='yellow')
                    elif x == 2:
                        self.Dcard3.configure(text=str(self.dealer.number[2] // 4 + 1), fg='yellow')
                    elif x == 3:
                        self.Dcard4.configure(text=str(self.dealer.number[3] // 4 + 1), fg='yellow')
                    elif x == 4:
                        self.Dcard5.configure(text=str(self.dealer.number[4] // 4 + 1), fg='yellow')


        self.Lplayer1Pts.configure(text=self.player1.made + self.player1.Lpedi,fg='cyan')
        self.Lplayer2Pts.configure(text=self.player2.made+self.player2.Lpedi,fg='cyan')
        self.Lplayer3Pts.configure(text=self.player3.made+self.player3.Lpedi,fg='cyan')
        self.LDealerPts.configure(text=self.dealer.made+self.dealer.Lpedi,fg='cyan')

        if self.dealer.pedigree >= self.player1.pedigree:
            self.P1Lstatus.configure(text='패',fg='red')
        else:
            self.P1Lstatus.configure(text='승',fg='red')
            self.playerMoney += self.P1betMoney * 2


        if self.dealer.pedigree >= self.player2.pedigree:
            self.P2Lstatus.configure(text='패',fg='red')
        else:
            self.P2Lstatus.configure(text='승',fg='red')
            self.playerMoney += self.P2betMoney * 2


        if self.dealer.pedigree >= self.player3.pedigree:
            self.P3Lstatus.configure(text='패',fg='red')
        else:
            self.P3Lstatus.configure(text='승',fg='red')
            self.playerMoney += self.P3betMoney * 2
        self.LplayerMoney.configure(text=str(self.playerMoney)+'만')



    def hitPlayer1(self,n):
        newCard = Card(self.cardDeck[self.deckN])
        number = self.cardDeck[self.deckN]
        self.player1.addCard(newCard)
        self.player1.addNumber(number)
        self.player1.addCardtype(number // 4 + 1)
        self.deckN += 1
        p = PhotoImage(file='GodoriCards/'+newCard.filename())
        self.LcardPlayer1.append(Label(self.window, image=p))
        self.LcardPlayer1[self.player1.inHand()-1].image = p
        self.LcardPlayer1[self.player1.inHand()-1].place(x=80+n*70, y=650)
        if n == 0:
            self.P1card1.configure(text=str(number // 4 + 1))
        elif n == 1:
            self.P1card2.configure(text=str(number // 4 + 1))
        elif n == 2:
            self.P1card3.configure(text=str(number // 4 + 1))
        elif n == 3:
            self.P1card4.configure(text=str(number // 4 + 1))
        elif n == 4:
            self.P1card5.configure(text=str(number // 4 + 1))





    def hitPlayer2(self,n):
        newCard = Card(self.cardDeck[self.deckN])
        number = self.cardDeck[self.deckN]
        self.player2.addCard(newCard)
        self.player2.addNumber(number)
        self.player2.addCardtype(number // 4 + 1)
        self.deckN += 1
        p = PhotoImage(file='GodoriCards/'+newCard.filename())
        self.LcardPlayer2.append(Label(self.window, image=p))
        self.LcardPlayer2[self.player2.inHand()-1].image = p
        self.LcardPlayer2[self.player2.inHand()-1].place(x=480+n*70, y=650)
        if n == 0:
            self.P2card1.configure(text=str(number // 4 + 1))
        elif n == 1:
            self.P2card2.configure(text=str(number // 4 + 1))
        elif n == 2:
            self.P2card3.configure(text=str(number // 4 + 1))
        elif n == 3:
            self.P2card4.configure(text=str(number // 4 + 1))
        elif n == 4:
            self.P2card5.configure(text=str(number // 4 + 1))

    def hitPlayer3(self,n):
        newCard = Card(self.cardDeck[self.deckN])
        number = self.cardDeck[self.deckN]
        self.player3.addCard(newCard)
        self.player3.addNumber(number)
        self.player3.addCardtype(number // 4 + 1)
        self.deckN += 1
        p = PhotoImage(file='GodoriCards/'+newCard.filename())
        self.LcardPlayer3.append(Label(self.window, image=p))
        self.LcardPlayer3[self.player3.inHand()-1].image = p
        self.LcardPlayer3[self.player3.inHand()-1].place(x=880+n*70, y=650)
        if n == 0:
            self.P3card1.configure(text=str(number // 4 + 1))
        elif n == 1:
            self.P3card2.configure(text=str(number // 4 + 1))
        elif n == 2:
            self.P3card3.configure(text=str(number // 4 + 1))
        elif n == 3:
            self.P3card4.configure(text=str(number // 4 + 1))
        elif n == 4:
            self.P3card5.configure(text=str(number // 4 + 1))

    def hitDealer(self,n):
        newCard = Card(self.cardDeck[self.deckN])
        number = self.cardDeck[self.deckN]
        self.dealer.addCard(newCard)
        self.dealer.addNumber(number)
        self.dealer.addCardtype(number // 4 + 1)
        self.deckN += 1
        p = PhotoImage(file='GodoriCards/'+newCard.filename())
        self.LcardDealer.append(Label(self.window, image=p))
        self.LcardDealer[self.dealer.inHand() - 1].image = p
        self.LcardDealer[self.dealer.inHand() - 1].place(x=480 + n * 70, y=250)
        if n == 0:
            self.Dcard1.configure(text=str(number // 4 + 1))
        elif n == 1:
            self.Dcard2.configure(text=str(number // 4 + 1))
        elif n == 2:
            self.Dcard3.configure(text=str(number // 4 + 1))
        elif n == 3:
            self.Dcard4.configure(text=str(number // 4 + 1))
        elif n == 4:
            self.Dcard5.configure(text=str(number // 4 + 1))

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
        self.Lplayer1Pts.configure(text="")
        self.Lplayer2Pts.configure(text="")
        self.Lplayer3Pts.configure(text="")
        self.LDealerPts.configure(text="")
        self.Dcard1.configure(text="",fg='white')
        self.Dcard2.configure(text="",fg='white')
        self.Dcard3.configure(text="",fg='white')
        self.Dcard4.configure(text="",fg='white')
        self.Dcard5.configure(text="",fg='white')
        self.P1card1.configure(text="",fg='white')
        self.P1card2.configure(text="",fg='white')
        self.P1card3.configure(text="",fg='white')
        self.P1card4.configure(text="",fg='white')
        self.P1card5.configure(text="",fg='white')
        self.P2card1.configure(text="",fg='white')
        self.P2card2.configure(text="",fg='white')
        self.P2card3.configure(text="",fg='white')
        self.P2card4.configure(text="",fg='white')
        self.P2card5.configure(text="",fg='white')
        self.P3card1.configure(text="",fg='white')
        self.P3card2.configure(text="",fg='white')
        self.P3card3.configure(text="",fg='white')
        self.P3card4.configure(text="",fg='white')
        self.P3card5.configure(text="",fg='white')



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

        self.P1card1 = Label(text='', width=2, height=1, font=self.fontstyle, bg='green', fg='white')
        self.P1card1.place(x=90, y=600)
        self.P1card2 = Label(text='', width=2, height=1, font=self.fontstyle, bg='green', fg='white')
        self.P1card2.place(x=160, y=600)
        self.P1card3 = Label(text='', width=2, height=1, font=self.fontstyle, bg='green', fg='white')
        self.P1card3.place(x=230, y=600)
        self.P1card4 = Label(text='', width=2, height=1, font=self.fontstyle, bg='green', fg='white')
        self.P1card4.place(x=300, y=600)
        self.P1card5 = Label(text='', width=2, height=1, font=self.fontstyle, bg='green', fg='white')
        self.P1card5.place(x=370, y=600)

        self.P2card1 = Label(text='', width=2, height=1, font=self.fontstyle, bg='green', fg='white')
        self.P2card1.place(x=490, y=600)
        self.P2card2 = Label(text='', width=2, height=1, font=self.fontstyle, bg='green', fg='white')
        self.P2card2.place(x=560, y=600)
        self.P2card3 = Label(text='', width=2, height=1, font=self.fontstyle, bg='green', fg='white')
        self.P2card3.place(x=630, y=600)
        self.P2card4 = Label(text='', width=2, height=1, font=self.fontstyle, bg='green', fg='white')
        self.P2card4.place(x=700, y=600)
        self.P2card5 = Label(text='', width=2, height=1, font=self.fontstyle, bg='green', fg='white')
        self.P2card5.place(x=770, y=600)

        self.P3card1 = Label(text='', width=2, height=1, font=self.fontstyle, bg='green', fg='white')
        self.P3card1.place(x=890, y=600)
        self.P3card2 = Label(text='', width=2, height=1, font=self.fontstyle, bg='green', fg='white')
        self.P3card2.place(x=960, y=600)
        self.P3card3 = Label(text='', width=2, height=1, font=self.fontstyle, bg='green', fg='white')
        self.P3card3.place(x=1030, y=600)
        self.P3card4 = Label(text='', width=2, height=1, font=self.fontstyle, bg='green', fg='white')
        self.P3card4.place(x=1100, y=600)
        self.P3card5 = Label(text='', width=2, height=1, font=self.fontstyle, bg='green', fg='white')
        self.P3card5.place(x=1170, y=600)

        self.Dcard1 = Label(text='', width=2, height=1, font=self.fontstyle, bg='green', fg='white')
        self.Dcard1.place(x=490, y=200)
        self.Dcard2 = Label(text='', width=2, height=1, font=self.fontstyle, bg='green', fg='white')
        self.Dcard2.place(x=560, y=200)
        self.Dcard3 = Label(text='', width=2, height=1, font=self.fontstyle, bg='green', fg='white')
        self.Dcard3.place(x=630, y=200)
        self.Dcard4 = Label(text='', width=2, height=1, font=self.fontstyle, bg='green', fg='white')
        self.Dcard4.place(x=700, y=200)
        self.Dcard5 = Label(text='', width=2, height=1, font=self.fontstyle, bg='green', fg='white')
        self.Dcard5.place(x=770, y=200)

        self.Lplayer1Pts = Label(text='', width=20, height=1, font=self.fontstyle, bg='green', fg='white')
        self.Lplayer1Pts.place(x=90, y=550)

        self.Lplayer2Pts = Label(text='', width=20, height=1, font=self.fontstyle, bg='green', fg='white')
        self.Lplayer2Pts.place(x=490, y=550)

        self.Lplayer3Pts = Label(text='', width=20, height=1, font=self.fontstyle, bg='green', fg='white')
        self.Lplayer3Pts.place(x=890, y=550)

        self.LDealerPts = Label(text='', width=20, height=1, font=self.fontstyle, bg='green', fg='white')
        self.LDealerPts.place(x=490, y=150)

        self.P1Lstatus = Label(text='', width=5, height=1, font=self.fontstyle, bg='green', fg='white')
        self.P1Lstatus.place(x=90, y=500)

        self.P2Lstatus = Label(text='', width=5, height=1, font=self.fontstyle, bg='green', fg='white')
        self.P2Lstatus.place(x=490, y=500)

        self.P3Lstatus = Label(text='', width=5, height=1, font=self.fontstyle, bg='green', fg='white')
        self.P3Lstatus.place(x=890, y=500)


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