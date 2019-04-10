import numpy as np
import random
from time import sleep


# Create a 3x3 grid board
def game_board():

    return np.array([[0,0,0],[0,0,0],[0,0,0]])


# Check for empty places to place a player number
def empty_slots(board):

    empty = list()

    for i in range(len(board)):

        for j in range(len(board)):

            if board[i][j] == 0:
                empty.append((i,j))

    return empty


# Choose a spot for a player randomly among the free/empty spots
def choose_slot(board, player):

    free_spots = empty_slots(board)

    selected = random.choice(free_spots)

    board[selected] = player

    return board


# Check each row to see if the player won or not
def check_row(board,player):

    for i in range(len(board)):

        won = True

        for j in range(len(board)):

            if board[i][j]!=player:
                won = False
                continue

        if won:
            return won

    return won


# Check each column to see if the player won or not
def check_col(board, player):
    for i in range(len(board)):

        won = True

        for j in range(len(board)):

            if board[j][i] != player:
                won = False
                continue

        if won:
            return won

    return won


# Check digonal to see if the player won or not
def check_diag(board, player):

    won = True

    for i in range(len(board)):

        if board[i][i] != player:
            won = False

    return won


# Check anti digonal to see if the player won or not
def check_anti_diag(board, player):
    won = True
    size = len(board)

    for i in range(size):

        if board[i][size - 1 - i] != player:
            won = False

    return won


# Make a decision based on each trial to see if either player has won or not
def decision(board):

    winner = 0

    for player in [1,2]:
        if check_row(board,player) or check_col(board,player) or check_diag(board,player) or check_anti_diag(board,player):
            winner = player

    if np.all(board != 0) and winner == 0:
        winner = "Nobody"

    return winner


# Main function
def lets_play():

    board = game_board()
    winner = 0
    count = 1

    print(board)

    sleep(1)

    while winner == 0:
        for player in [1,2]:
            board = choose_slot(board,player)
            print("Game Board after "+ str(count)+" move(s) ")
            print(board)
            sleep(1)
            count += 1
            winner = decision(board)

            if winner != 0:
                break

    return winner

# Final Output
print(" The Winner is Player : " + str(lets_play()))


