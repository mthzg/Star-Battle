from board import Board
from interface import Interface


def main():
    board = Board(10)
    board.display_grid()
    ui = Interface(board)
    ui.show()

    
main()
