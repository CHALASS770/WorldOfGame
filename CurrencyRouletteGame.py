from random import *
from time import sleep
#in this game we must find the trust conversion from USD to ILS
class  CurrencyRouletteGame:
    def __init__(self, difficult):
        self.total_money = int(randint(5,1000)) #random the money in USD that the player must fnd the convert in ils
        self.intermin = 0
        self.intermax = 0
        self.difficult = difficult
        self.useramount = 0
    #this function create an interval of error for the convert
    #the intervall depend of the difficulty of the game
    def get_money_interval(self):
        self.intermin=self.total_money - (5 - self.difficult)
        self.intermax=self.total_money + (5 - self.difficult)
    #the player enter the conversion
    def get_guess_from_user(self):
        print(self.total_money,' USD')
        self.useramount=int(input('enter a value in ILS'))

    def play(self):
        #call function create money
        self.get_money_interval()
        #call function enter value by th player
        self.get_guess_from_user()
        #verify if the player entered is in between the interval for win
        if self.intermin<self.useramount<self.intermax:
            print('you win')
        else:
            print('you lost')
            print(self.intermin,'< ',self.useramount,'< ',self.intermax)