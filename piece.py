class Piece():
    ## this is where all piece types and rules are defined
    def __init__(self, color):
        # add any additional parameters
        # standard initiation of a piece 
        self.name = ''
        self.color = color

    def is_valid_move(self):
        return False

    def is_white(self):
        pass

    def __str__(self):
        # replace the body and return a string with how you want your piece
        # to be printed as when `print([A Piece Object])` is called
        return ""
        
# I'll add which parameters I generally used for the specific subclasses
# in the following Rook class, but note you may need more or less depending
# on your specific implementation

class Rook(Piece):
    def __init__(self, color):
        """
        Same as base class Piece, except `first_move` is used to check
        if this rook can castle.
        """
        super().__init__(color)
        self.name = 'Rook'
    
    def is_valid_move(self, board, start, to):
        pass

class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = 'Knight'

    def is_valid_move(self):
        pass

class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = 'Bishop'

    def is_valid_move(self):
        pass

class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = 'Queen'

    def is_valid_move(self):
        pass

class King(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = 'King'

    def is_valid_move(self):
        pass
    
    # I added an extra method for the King class
    def can_castle(self):
        pass

# Class to represent a pseudo pawn that can be taken when
# en passant is possible
class GhostPawn(Piece):
    def __init__(self, color):
        pass

    def is_valid_move(self):
        return False

class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = 'Pawn'

    def is_valid_move(self):
        pass
    