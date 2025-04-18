from board import Board
from interface import Grid_UI

def main():
    board = Board(10)
    ui = Grid_UI(board)
    ui.show()

    
main()
