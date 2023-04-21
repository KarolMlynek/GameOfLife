from board import Board
import os
from time import sleep


def main():
    user_rows = int(input('How many rows? '))
    user_columns = int(input('How many columns? '))
    game_of_life_board = Board(user_rows, user_columns)
    game_of_life_board.draw_board()
    user_action = ''
    '''while user_action != 'q':'''
    for i in range(100):
        '''user_action = input('Press enter to add generation or press q to quit:')'''
        '''if user_action == '':'''
        game_of_life_board.update_board()
        os.system('printf \'\\33c\\e[3J\'')
        game_of_life_board.draw_board()
        sleep(0.2)


main()
