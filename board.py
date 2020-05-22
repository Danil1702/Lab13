class Board:    
    '''Class represnting tic-tac-toe game board'''
    
    CROSS = '✖'
    CIRCLE = 'O'
    
    def __init__(self):
        '''
        Initializing new empty board
        Last move is None by default
        '''
        self._board = [[" ", " ", " "] for i in range(3)]
        self._left = None
        self._right = None

    def draw(self):
        '''
        Visual representation of the board
        '''
        for row in self._board:
            print("-----")
            print("|".join(row))
        print("-----")   

    def move(self, position, cross=True):
        '''
        Sets the corresponsdent cell
        of the board to cross if cross is True,
        circle otherwise       
        '''
        item = Board.CROSS if cross else Board.CIRCLE
        self._board[position[0]][position[1]] = item

    def is_filled(self):
        '''
        Checks if the game
        board is empty
        '''
        number_free = 0
        for row in self._board:
            number_free += row.count(" ")

        return number_free == 0    

    def free_cells(self):
        '''
        Returns the list of available positions
        to make a move
        '''
        list_cells = []
        for i in range(3):
            for j in range(3):
                if self._board[i][j] == " ":
                    list_cells.append((i, j))
        return list_cells            

    def last_move(self, other):
        '''
        Finds the last move of X
        '''
        self_cross_positions = set()
        other_cross_positions = set()
        for i in range(3):
            for j in range(3):
                if self._board[i][j] == Board.CROSS:
                    self_cross_positions.add((i, j))
                if other._board[i][j] == Board.CROSS:
                    other_cross_positions.add((i, j)) 
        return other_cross_positions.difference(self_cross_positions)               
    
    def check_win(self):
        '''
        Check if there is a winning combination
        and returns 1 if computer wins, -1 if loses
        and 0 if there is a draw
        '''
        win_positons = [
            set([(0, 0), (0, 1), (0, 2)]),
            set([(1, 0), (1, 1), (1, 2)]),
            set([(2, 0), (2, 1), (2, 2)]),
            set([(0, 0), (1, 1), (2, 2)]),
            set([(0, 0), (1, 0), (2, 0)]),
            set([(0, 1), (1, 1), (2, 1)]),
            set([(0, 2), (1, 2), (2, 2)]),
            set([(2, 0), (1, 1), (0, 2)]),
        ]
         
        cross_positions = set()
        circle_positions = set()
        for i in range(3):
            for j in range(3):
                if self._board[i][j] == Board.CROSS:
                    cross_positions.add((i, j))
                elif self._board[i][j] == Board.CIRCLE:
                    circle_positions.add((i, j))  

        def win(positions):    
            for position in win_positons:
                if position.issubset(positions):
                    return True

        if win(cross_positions) and win(circle_positions):
            return 0
        elif win(cross_positions):
            return 1
        elif win(circle_positions):
            return -1   
        else:
            return 0         
             

