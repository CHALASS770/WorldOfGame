from random import *
from time import sleep
#classical play of memori with how many numbers
class  MemoryGame :
    #init variables for the game
    def __init__(self, difficult):
        self.my_sequence = []
        self.list_from_user = []
        self.difficulty = difficult*2
        #self.valid=0

    def generate_sequence(self):
        # generate a sequence number who must remember
        # my sequence must have *2 number on the difficulty choice
        # in the level 1 for the debutents i need remember 2 numbers
        # in the level 5 for the experts i need remember 10 numbers
        for lenght in range(self.difficulty):
            self.my_sequence.append(int(randint(0, 101)))
        #show the sequence 7 second at the player
        print('the sequence is : ', self.my_sequence)
        sleep(0.7)
        #do desappear the sequnce after 7 second
        for i in range(30):
            print('')

    def get_list_from_user(self):
        # the player enter the number that he remember
        for lenght in range(self.difficulty):
            self.list_from_user.append(int(input('enter the value ')))

    def is_list_equal(self):

        valid=0 #"valid" it's a count of the good response entered by the player
        for lenght in self.my_sequence:
            for list_user in self.list_from_user:
                if lenght == list_user: #verify if my_sequence and the enter player are equal
                    valid = valid + 1
        if valid == self.difficulty:#if i finded all numbers return true
            return True

        else:
            return False #if i didn't finded all numbers return false


    def play(self):
        #Call function for play
        self.generate_sequence()
        self.get_list_from_user()
        #if the i find all number i win
        if self.is_list_equal()==True :
            print('you win')
        else:
            print('you lost')