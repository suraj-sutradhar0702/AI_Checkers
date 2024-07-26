import pygame
from game_config import *
from tokens import Token


class Board:
    def __init__(self):
        self.board = []
        self.player_left = self.ai_left = NO_OF_TOKENS
        self.player_kings = self.ai_kings = 0
        self.create_board()

    def draw_squares(self, win):
        win.fill(BOARD_LIGHT_COLOR)
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(
                    win,
                    BOARD_DARK_COLOR,
                    (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE),
                )

    def move(self, token, row, col):
        self.board[token.row][token.col], self.board[row][col] = (
            self.board[row][col],
            self.board[token.row][token.col],
        )
        token.move(row, col)

        if row == 0 or row == ROWS - 1:
            if token.make_king():
                if token.color == PLAYER_COLOR:
                    self.player_kings += 1
                elif token.color == AI_COLOR:
                    self.ai_kings += 1

    def get_token(self, row, col):
        return self.board[row][col]

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Token(row, col, AI_COLOR))
                    elif row > ROWS - 4:
                        self.board[row].append(Token(row, col, PLAYER_COLOR))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                token = self.board[row][col]
                if token != 0:
                    token.draw(win)

    def evaluate(self):
        return (
            self.ai_left * 7
            + self.ai_kings * 10
            - self.player_left * 5
            - self.player_kings * 9
        )

    def get_all_tokens(self, color):
        tokens = []
        for row in self.board:
            for token in row:
                if token != 0 and token.color == color:
                    tokens.append(token)
        return tokens

    def get_valid_moves(self, token):
        moves = {}
        left = token.col - 1
        right = token.col + 1
        row = token.row

        if token.color == PLAYER_COLOR or token.king:
            moves.update(
                self._travel_l(row - 1, max(row - 3, -1), -1, token.color, left)
            )
            moves.update(
                self._travel_r(row - 1, max(row - 3, -1), -1, token.color, right)
            )

        if token.color == AI_COLOR or token.king:
            moves.update(
                self._travel_l(row + 1, min(row + 3, ROWS), 1, token.color, left)
            )

            moves.update(
                self._travel_r(row + 1, min(row + 3, ROWS), 1, token.color, right)
            )
        return moves

    def _travel_l(self, start, stop, step, color, left, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break
            current = self.board[r][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, left)] = last + skipped
                else:
                    moves[(r, left)] = last

                if last:
                    if step == -1:
                        row = max(r - 3, -1)
                    else:
                        row = min(r + 3, ROWS)

                    moves.update(
                        self._travel_l(
                            r + step, row, step, color, left - 1, skipped=last
                        )
                    )
                    moves.update(
                        self._travel_r(
                            r + step, row, step, color, left + 1, skipped=last
                        )
                    )
                break
            elif current.color == color:
                break
            else:
                last = [current]

            left -= 1
        return moves

    def _travel_r(self, start, stop, step, color, right, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= COLS:
                break
            current = self.board[r][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, right)] = last + skipped
                else:
                    moves[(r, right)] = last

                if last:
                    if step == -1:
                        row = max(r - 3, -1)
                    else:
                        row = min(r + 3, ROWS)

                    moves.update(
                        self._travel_l(
                            r + step, row, step, color, right - 1, skipped=last
                        )
                    )
                    moves.update(
                        self._travel_r(
                            r + step, row, step, color, right + 1, skipped=last
                        )
                    )
                break
            elif current.color == color:
                break
            else:
                last = [current]

            right += 1

        return moves

    def check_trap(self, color):
        moves = {}
        for row in range(ROWS):
            for col in range(COLS):
                token = self.board[row][col]
                if token != 0 and token.color == color:
                    moves.update(self.get_valid_moves(token))
        if not moves:
            return True
        return False

    def remove(self, tokens):
        for token in tokens:
            self.board[token.row][token.col] = 0
            if token != 0:
                if token.color == PLAYER_COLOR:
                    self.player_left -= 1
                else:
                    self.ai_left -= 1

    def winner(self):
        if self.player_left <= 0:
            return "AI"
        elif self.ai_left <= 0:
            return "PLAYER"
        return None
