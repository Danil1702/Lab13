from board import Board
import random
import copy


class Tree:
    '''Class representing binary tree'''
    def __init__(self, board):
        '''
        Initialize new tree
        '''
        self._root = board

    def build_tree(self):
        '''
        Building random binary tree
        '''
        def recurse(board):
            if board.is_filled():
                return

            board.move(random.choice(board.free_cells()), False)
            
            try:
                board_left = copy.deepcopy(board)
                board_left.move(random.choice(board.free_cells()))
                board._left = board_left
                recurse(board_left)


                board_right = copy.deepcopy(board)
                board_right.move(random.choice(board.free_cells()))
                board._right = board_right
                recurse(board_right)
            except IndexError:
                return
        
        recurse(self._root) 

    @staticmethod
    def count_wins(board):
        '''
        Counting the results of the game
        '''
        def recurse(board):
            if board.is_filled():
                return board.check_win() 

            result = 0
            result += recurse(board._left) + recurse(board._right)
            return result

        return recurse(board)                



  


