#import all game
from GuessGame import  *
from CurrencyRouletteGame import *
from MemoryGame import *
#import sleep
from time import sleep

def welcome(name):
    print("Hello %s ! Welcome in World of Game!!! "% name)
    print("Here you can find many cool games to play ")

#create a function for the player can choose what's game he want
def load_game():
    valideplay = True
    while valideplay == True:
        try :
            # enter the number of game that wants play and verify that a number
            play=int(input("Please choose a game to play: \n 1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back \n 2. Guess Game - guess a number and see if you chose like the computer \n 3. Weather Roulette - Guess the current temperature currently in Jerusalem \n"))
            if 1 <= play <= 3 : #if the number entered is between 1 and 3 the game was choosed
                valideplay = False #and it's the end of loop
            else:
                raise ValueError("your choice is invalide") #else if a the number entered it's more 3 or less 1

        except ValueError:
            #if the error its value eror show this message
            print("****please enter a valid value ****** \n ********************* \n")
    #here the player choose the difficulty with he wants play
    validedif = True
    while validedif == True:
        try :
            # enter the number of difficulty that wants play and verify that a number
            difficult = int(input("choose a dificult betwin 1 and 5 \n "))
            if 1 <= difficult <=5 : #if the number entered is between 1 and 5 the difficulty was choosed
                validedif = False#and it's the end of loop
            else :
                raise ValueError("your choice is invalide") #else if a the number entered it's more 3 or less 1
        except ValueError:
            # if the error its value eror show this message
            print("****please enter a valid value**** \n ********************\n")
    #show the game was choosed
    if play == 1 :
        print("you choose to play to Memory Game")
    elif play == 2:
        print("you choose to play to Guess Game")
    elif play == 3:
        print("you choose to play to Weather Roulette")
    #show the difficulty was choosed
    if difficult == 1 :
        print("difficult is easy")
    elif difficult == 2:
        print("difficult is easy plus")
    elif difficult  == 3:
        print("difficult is hard")
    elif difficult == 4:
        print("difficult is hard plus")
    elif difficult  == 5:
        print("difficult is very Hard")
    #i need the game and the difficulty were choosed
    return play, difficult

def play_game(playGame, level):
    sleep(3)
    #start the game choosed
    if playGame == 2:
        for i in range(20):
            print('')
        print('**************************************')
        print('***** WELCOME TO THE GUESS GAME ******')
        print('**************************************')
        for i in range(3):
            print('')
        game = GuessGame() #call the object game
        game.generat_number(level) # enter the level of difficulty and increment th game
        game.compare_result() #play at the game
    elif playGame == 1:
        for i in range(20):
            print('')
        print('**************************************')
        print('***** WELCOME TO THE MEMORY GAME ******')
        print('**************************************')
        for i in range(3):
            print('')
        game = MemoryGame(level)#call the object game
        game.play()#play at the game
    elif playGame == 3:
        for i in range(20):
            print('')
        print('**************************************')
        print('***** WELCOME TO THE ROULETTE GAME ******')
        print('**************************************')
        for i in range(3):
            print('')
        game = CurrencyRouletteGame(level)#call the object game
        game.play()#play at the game