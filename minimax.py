import math

import pygame
import board as boardd
import random
import win as win
from variables import *
def evaluate_window(window_four, piece):
    score = 0
    opp_piece = PLAYER_PIECE
    # if piece == PLAYER_PIECE:
    #     opp_piece = AI_PIECE

    if window_four.count(piece) == 4:
        score += 1000
    elif window_four.count(piece) == 3 and window_four.count(EMPTY) == 1:
        score += 5
    elif window_four.count(piece) == 2 and window_four.count(EMPTY) == 2:
        score += 2
    if window_four.count(opp_piece) == 3 and window_four.count(EMPTY) == 1:
        score -= 4
    if window_four.count(opp_piece) == 2 and window_four.count(EMPTY) == 2:
        score -= 2

    return score



def score_pos(board, piece):
    score = 0

    center_array = [int(i) for i in list(board[:, COLUMN//2])]          #col 3 center
    count_center = center_array.count(piece)
    score += count_center * 3

    for r in range(ROW):            #Horizontal Score
        row_array = [int(i) for i in list(board[r, :])]
        for c in range(COLUMN-3):
            window_four = row_array[c: c+WINDOW_SIZE]
            score += evaluate_window(window_four, piece)+(7-r)
    for c in range(COLUMN):           #Vertical Score
        col_array = [int(i) for i in list(board[:,  c])]
        for r in range(ROW-3):
            window_four = col_array[r: r+WINDOW_SIZE]
            score += evaluate_window(window_four, piece)+(7-r)

    for r in range(ROW-3):              #Positive Slope Score
        for c in range(COLUMN-3):
            window_four = [board[r+i][c+i] for i in range(WINDOW_SIZE)]
            score += evaluate_window(window_four, piece)+(7-r)

    for r in range(3, ROW):             #Negative Slope Score
        for c in range(COLUMN-3):
            window_four = [board[r-i][c+i] for i in range(WINDOW_SIZE)]
            score += evaluate_window(window_four, piece)+(7-r)

    return score

def get_valid_locations(board):
    valid_locations = []
    for col in range(COLUMN):
        if boardd.valid_location(board, col):
            valid_locations.append(col)
            # print(valid_locations)
    return valid_locations

def terminal_board(board):
    return win.wining_move(board, PLAYER_PIECE) or win.wining_move(board, AI_PIECE) or len(get_valid_locations(board)) == 0

def minimax(board, depth, alpha, beta, maximizing_player):
    is_terminal = terminal_board(board)
    valid_locations = get_valid_locations(board)
    if depth == 0 or is_terminal:
        if is_terminal:
            if win.wining_move(board,AI_PIECE):
                return (None,1000000000)
            elif win.wining_move(board,PLAYER_PIECE):
                return (None, -1000000000)
            else :
                return (None, 0)  #When Game has no remaining moves full board
        else:
            return (None, score_pos(board,AI_PIECE))
    if maximizing_player:
        value = -math.inf
        cols = random.choice(valid_locations)
        for col in valid_locations:
            row = boardd.next_row(board, col)
            new_board = board.copy()
            boardd.drop_piece(new_board, row, col, AI_PIECE)
            new_score = minimax(new_board, depth-1, alpha, beta, False)[1]               #from return we take value ---->[1]
            if new_score > value:
                value = new_score
                cols = col
            alpha = max(alpha, value)
            if beta <= alpha:             #beta smaller than alpha break
                break

        return cols, value
    else:
        value = math.inf
        cols = random.choice(valid_locations)
        for col in valid_locations:
            row = boardd.next_row(board, col)
            new_board = board.copy()
            boardd.drop_piece(new_board, row, col, PLAYER_PIECE)
            new_score = minimax(new_board, depth - 1, alpha, beta, True)[1]
            if new_score < value:
                value = new_score
                cols = col
            beta = min(beta, value)
            if beta <= alpha:               #beta smaller than alpha break
                break

        return cols, value


def minimax_2(board, depth, maximizing_player):
    is_terminal = terminal_board(board)
    valid_locations = get_valid_locations(board)
    if depth == 0 or is_terminal:
        if is_terminal:
            if win.wining_move(board,AI_PIECE):
                return (None,1000000000)
            elif win.wining_move(board,PLAYER_PIECE):
                return (None, -1000000000)
            else :
                return (None, 0)  #When Game has no remaining moves full board
        else:
            return (None, score_pos(board,AI_PIECE))
    if maximizing_player:
        value = -math.inf
        cols = random.choice(valid_locations)
        for col in valid_locations:
            row = boardd.next_row(board, col)
            new_board = board.copy()
            boardd.drop_piece(new_board, row, col, AI_PIECE)
            new_score = minimax_2(new_board, depth-1, False)[1]               #from return we take value ---->[1]
            if new_score > value:
                value = new_score
                cols = col

        return cols, value
    else:
        value = math.inf
        cols = random.choice(valid_locations)
        for col in valid_locations:
            row = boardd.next_row(board, col)
            new_board = board.copy()
            boardd.drop_piece(new_board, row, col, PLAYER_PIECE)
            new_score = minimax_2(new_board, depth - 1, True)[1]
            if new_score < value:
                value = new_score
                cols = col

        return cols, value



def best_move(board, piece):
    valid_locations = get_valid_locations(board)
    best_score = -1000
    best_col = random.choice(valid_locations)
    for col in valid_locations:
        row = boardd.next_row(board, col)
        try_board = board.copy()
        boardd.drop_piece(try_board, row, col, piece)
        score = score_pos(try_board, piece)
        if score > best_score:
            best_score = score
            best_col = col
        # print(best_col)
    return best_col

