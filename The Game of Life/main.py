from board import Board
from select_preset import get_preset
from os import system
from time import sleep


text = get_preset()

board = Board.from_string(text)  # board creation

while True:
    system('cls')
    board.print_board()
    board.change_generations()
    sleep(0.01)
