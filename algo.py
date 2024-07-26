from copy import deepcopy
import pygame
from game_config import *


def alphabeta_max(position, alpha, beta, dep, game):
    if dep == 0 or position.winner() != None:
        return position.evaluate(), position

    maxEval = float("-inf")
    best_move = None

    for move in get_all_moves(position, AI_COLOR, game):
        evaluation, temp = alphabeta_min(move, alpha, beta, dep - 1, game)
        if evaluation > maxEval:
            maxEval = evaluation
            best_move = move
        alpha = max(alpha, maxEval)
        if alpha >= beta:
            break

    return maxEval, best_move


def alphabeta_min(position, alpha, beta, dep, game):
    if dep == 0 or position.winner() != None:
        return position.evaluate(), position
    minEval = float("inf")
    best_move = None

    for move in get_all_moves(position, PLAYER_COLOR, game):
        evaluation, temp = alphabeta_max(move, alpha, beta, dep - 1, game)
        beta = min(beta, minEval)
        if evaluation < minEval:
            minEval = evaluation
            best_move = move
        if beta <= alpha:
            break

    return minEval, best_move


def get_all_moves(board, color, game):
    moves = []
    for token in board.get_all_tokens(color):
        valid_moves = board.get_valid_moves(token)
        for move, skip in valid_moves.items():
            temp_board = deepcopy(board)
            temp_token = temp_board.get_token(token.row, token.col)
            new_board = simulate_move(temp_token, move, temp_board, game, skip)
            moves.append(new_board)
    return moves


def simulate_move(token, move, board, game, skip):
    board.move(token, move[0], move[1])
    if skip:
        board.remove(skip)
    return board
