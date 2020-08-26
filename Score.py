from Utils import *
#The scores file at this point will consist of only a number.
# That number is the accumulation of the winnings of the user.
class Scores :
    #create class for all informations that must write in the text file "score.txt"
    def __init__(self ,nameP, play, difficult) :
        self.score = 0
        self.diffic = difficult
        self.namep = nameP
        self.Play = play
        self.newscore = 0
    #calculate the final score and write all informations in "score.txt"
    def Write_Score(self):
        #calculate the score of player
        self.score = self.diffic * 3 + 5
        #convert score in string value
        self.score = str(self.score)
        #create new player score for file
        self.newscore = Utils(self.namep, self.Play, self.score)
        #write in file player data with his score
        self.newscore.write_score()
    #call function for read the file "score.txt"
    def read(self):
        self.newscore.read_score()