from board import Board
import pandas
from datetime import datetime
class Chess():

    

    #This class is the game chess, and takes a board w/ pieces, has a timestamp

    def __init__(self, board, timestamp, turn= True):
        self.board = board
        self.timestamp = timestamp
        self.turn = turn


    def promotion(self):
    # add any parameters necessary and replace the body with
    # functionality on promoting a Pawn that has reached the 
    # end of the board
        pass

    def move(self):
    # add any parameters necessary and replace the body with
    # functionality of moving a a piece from its current location
    # to a destination
        pass

    def uploadSQL(self):
    # this will patch a new record to a table for each move
        pass
    
    def print_boardstate(self):
        Board.print_board(self)
        
myboard =  Board().board

currentboardstate = Chess(myboard, datetime.now())

Chess.print_boardstate(currentboardstate)
