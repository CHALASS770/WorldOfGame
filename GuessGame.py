from random import *
class  GuessGame : #it's a play where we have a number's random that we must find
    # this guess number and the number of chance for find this depends of the difficulty's game
    #we have 5 level of play
    # for level n the secret number is between 0 and n*10
    # the max number of chances is (5+1)-n

    def __init__(self): # define variable of GuessGame
        self.secretNumber = 1
        self.choice= -1
        self.chance=5

    def generat_number(self, difficulty):
        self.secretNumber = int(randint(0, difficulty*10)) # for level n the secret number is between 0 and n*10
        self.chance=self.chance+1-difficulty # the max number of chances is (5+1)-n
    def get_secret_number(self):
        return self.secretNumber # return the random number
    def guess_from_user(self): #user try to find the true number
        valideplay = True
        while valideplay == True:
            try:
                self.choice = int(input("enter a number")) #enter the user's number and verify that a number
                valideplay = False #if choice isn't "int" enter we ask a good enter
            except:
                print('please enter a numeric value')
    def guet_guess_from_user(self): #return the choice of difficulty
        return self.choice
    def compare_result(self):
        print('Good luck')
        #the player can play while he have chance and he don't find the good number
        while self.chance > 0 and self.get_secret_number() != self.guet_guess_from_user():
            print('you have ', self.chance, ' chance') # he can see how many chance he have
            self.guess_from_user() #the player enter his choice
            self.chance = self.chance - 1 #number of chance less 1
        if self.get_secret_number()== self.guet_guess_from_user():
            #if he find the true number he win
            print("you Win")
        elif self.chance == 0:
            #if he didn't find the true number and he haven't more chance he lost
            print("you lost")
            #we tell what was the true number
            print('the value was ', self.secretNumber)