from board import Board
from btree import Tree
import random
import copy


def main():
    '''
    Launches the tic-tac-toe game
    '''
    board = Board()
    free_list = board.free_cells()
    choice = random.choice(free_list)
    board.move(choice)

    while not board.is_filled():
        board.draw()  
        
        #move of the player
        try:
            move = input("The coordinates of your move: ").split(",")
            board.move((int(move[0]),int(move[1])) , False)
        except IndexError:
            continue

        #move of the computer
        tree = Tree(copy.deepcopy(board))
        tree.build_tree()
        right_wins = tree.count_wins(tree._root._right)
        left_wins = tree.count_wins(tree._root._left)
        if right_wins > left_wins:
            move = board.last_move(tree._root._right)
        else:
            move = board.last_move(tree._root._left)  
        board.move(list(move)[0])      
        
        #check for winning combination
        win = board.check_win()
        if win == 1:
            return "You lose the game!"
        elif win == -1:
            return "You win the game!"        
    
    return "The draw!"


if __name__ == "__main__":
    print(main())        
