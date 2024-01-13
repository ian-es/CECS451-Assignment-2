"""
genetic.py
Ian Escalante
9/22/2023

CECS 451 Fall 23
Professor Kate Nguyen
Cal State Long Beach
"""
import board
import math
import random
import time


def main():
    start = time.time()
    end_gene = genetic(5,8)
    stop = time.time()
    print(f"Running time: {((stop - start)*1000):.0f}ms")
    # format the matrix into - and x
    print(format_board_output(get_map_board(end_gene)))


def genetic(queens,states):
    # get the fitness score that means no pairs are attacking
    win_condition = math.comb(queens, 2)
    winning_board = None

    # create 4 initial states of boards with 5 queens
    game_boards = [board.Board(queens) for _ in range(states)]
    # turn the initial game boards into gene strings
    game_boards = [get_board_string(game_board) for game_board in game_boards]

    while winning_board is None:
        boards_fitnesses = []
        total_fitness = 0
        for board_gene in game_boards:
            board_fitness = win_condition - check_fitness(board_gene)
            if board_fitness == win_condition:
                return board_gene
            boards_fitnesses.append(board_fitness)
            total_fitness += board_fitness

        # calculate reproductive chance for each individual gene (board_fitness/total_fitness)
        boards_fitnesses = [(x/total_fitness) for x in boards_fitnesses]
        new_boards = []

        # pick the surviving genes
        for i in range(states):
            gene_picker = random.random()
            for j in range(states):
                if gene_picker < sum(boards_fitnesses[:(j+1)]):
                    new_boards.append(game_boards[j])
                    break

        # crossover
        for i in range(int(states/2)):
            cross = random.randint(1, queens-1)
            swap1 = new_boards[2*i]
            swap2 = new_boards[(2*i)+1]
            new_boards[2*i] = swap1[:cross] + swap2[cross:]
            new_boards[(2*i)+1] = swap2[:cross] + swap1[cross:]

        # mutation
        for i in range(states):
            mutate = random.randint(0, queens-1)
            new_boards[i] = new_boards[i][:mutate] + str(random.randint(0, queens-1)) + new_boards[i][mutate+1:]

        game_boards = new_boards
        # repeat


# given a game board (2 dimensional array of 0 and 1)
# returns a string representing the location of the queens
def get_board_string(game_board):
    board_map = game_board.map
    board_string = ["" + "0" for _ in range(len(board_map))]
    board_string = "".join(board_string)

    for row in range(len(board_map)):
        for col in range(len(board_map[0])):
            if board_map[row][col] == 1:
                board_string = board_string[:col] + str(len(board_map)-1-row) + board_string[col+1:]
                break
    return board_string


# given a string representing the "gene" of a board
# must check diagonals, columns, and rows
# returns the number of attacking pairs
def check_fitness(board_gene):
    new_board = board.Board(len(board_gene))
    new_board.map = get_map_board(board_gene)
    fitness = new_board.get_fitness()

    # find horizontal fitness
    for i in range(len(board_gene)-1):
        if board_gene[i] == board_gene[i+1]:
            fitness += 1

    return fitness


# given a string representation of the location of the queens
# return a game board
def get_map_board(board_gene):
    board_map = [[0 for _ in range(len(board_gene))] for _ in range(len(board_gene))]

    for i in range(len(board_gene)):
        board_map[i][int(board_gene[i])] = 1

    return board_map


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
