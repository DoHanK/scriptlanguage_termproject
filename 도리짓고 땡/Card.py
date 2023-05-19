class Card:
    def __init__(self, number):
        self.x = number // 4
        self.value = number % 4 + 1

    def getsuit(self):
        suits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        return suits[self.x]

    def filename(self): #
        return self.getsuit()+ str(self.value)+'.gif'

    def getValue(self):
        return self.value
