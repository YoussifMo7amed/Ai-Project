from copy import deepcopy
import pygame

RED = (255, 0, 0)
WHITE = (255, 255, 255)

def minimax(position, depth, max_player, game, cond=float('inf')):
    if depth == 0 or position.winner() != None:
        return position.evaluate(), position

    moves = get_all_moves(position, WHITE if max_player else RED, game)
    if not moves:
        # لو مفيش حركات نرجع التقييم الحالي
        return position.evaluate(), position

    if max_player:
        maxEval = float('-inf')
        best_move = None
        for move in moves:
            evaluation = minimax(move, depth-1, False, game, maxEval)[0]
            if evaluation >= cond:
                break
            if evaluation > maxEval:
                maxEval = evaluation
                best_move = move
        return maxEval, best_move
    else:
        minEval = float('inf')
        best_move = None
        for move in moves:
            evaluation = minimax(move, depth-1, True, game, minEval)[0]
            if evaluation <= cond:
                break
            if evaluation < minEval:
                minEval = evaluation
                best_move = move
        return minEval, best_move

def simulate_move(piece, move, board, game, skip):
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)
    return board

def get_all_moves(board, color, game):
    moves = []
    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        for move, skip in valid_moves.items():
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, game, skip)
            moves.append(new_board)
    return moves
