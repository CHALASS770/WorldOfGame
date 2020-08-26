#**************************************************************************************#
#**************************************************************************************#
#*** This file will contain general information and operations we need for our game ***#
#**************************************************************************************#
#**************************************************************************************#

class Utils :
    def __init__(self, namePlayer, play ,myscore):
        #create class for write or read in the text file "score.txt"
        self.score_file_name = ""
        self.bad_return_code = -1
        self.chance=5
        self.score=myscore
        self.nameplay = namePlayer
        #init what the user want o play
        if play == 1:
            self.play = "Memorygame"
        elif play == 2:
            self.play = "GuessGame"
        elif play == 3:
            self.play = "Roulette Game"
    '''def Screen_Cleaner():'''

    # create a function for write in the text file
    def write_score(self):
        #open the score.txt file in write mode
        self.score_file_name = open("score.txt", "w")
        #write in the file
        self.score_file_name.write(self.score)
        #close after work
        self.score_file_name.close()
    #create a function for read the text file
    def read_score(self):
        # open the score.txt file in read mode
        self.score_file_name = open("score.txt", "r")
        #display file datas
        print(self.score_file_name.read())
        # close after work
        self.score_file_name.close()