"""
hill.py
Ian Escalante
9/22/2023

CECS 451 Fall 23
Professor Kate Nguyen
Cal State Long Beach
"""
import board
import time
import copy


def main():
    start = time.time()
    # create a new board with 5 randomly placed queens
    game_board = board.Board(5)

    # create the random restart for if the hill climb gets stuck on a local maximum
    # otherwise if there are no collisions, take that board as final
    while game_board.get_fitness() != 0:
        game_board = hill_climb(board.Board(5))
    stop = time.time()

    print(f"Running time: {((stop - start)*1000):.0f}ms")
    print(format_board_output(game_board.get_map()))


# given a game board
#
def hill_climb(game_board):
    local_max = False

    # loop until the game board has no collisions
    # or a local max is reached (the whole board is searched without any lower fitness values found)
    while game_board.get_fitness() != 0 and local_max is False:
        local_max = True
        queens = len(game_board.get_map())
        temp = copy.copy(game_board)
        fitness = game_board.get_fitness()
        to_change = board.Board(queens)

        # look through each row and column for the move that gives the best fitness value
        for row in range(queens):
            for col in range(queens):
                temp_row = [0 for _ in range(queens)]
                temp_row[col] = 1

                temp.map = copy.copy(game_board.map)
                temp.map[row] = temp_row
                temp_fitness = temp.get_fitness()

                if temp_fitness < fitness:
                    local_max = False
                    to_change = copy.copy(temp)
                    fitness = temp_fitness

        # change the board to the move that gives the best fitness
        game_board = copy.copy(to_change)

    return game_board


# given a board map
# return a string formatted with - and x representing spaces and queens respectively
def format_board_output(board_map):
    board_string = ""

    for row in board_map:
        for col in row:
            if col == 1:
                board_string += "1 "
            else:
                board_string += "- "
        board_string += "\n"

    return board_string


main()
