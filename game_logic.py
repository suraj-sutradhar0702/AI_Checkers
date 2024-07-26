import pygame
from game_config import *
from checkers_board import Board


class checkersGame:
    def __init__(self, win):
        self._init()
        self.win = win
        pygame.mixer.init()
        self.notify_sound = pygame.mixer.Sound("resources/notify.mp3")
        self.capture_sound = pygame.mixer.Sound("resources/capture.mp3")
        self.move_sound = pygame.mixer.Sound("resources/move.mp3")

    def reset(self):
        self._init(self)

    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def winner(self):
        return self.board.winner()

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = PLAYER_COLOR
        self.valid_moves = {}

    def _move(self, row, col):
        token = self.board.get_token(row, col)
        if token == 0 and (row, col) in self.valid_moves:
            k = self.board.player_kings
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if self.board.player_kings != k:
                print("player kings increased")
                self.notify_sound.play()
            elif skipped:
                print("ai piece(s) captured")
                self.board.remove(skipped)
                self.capture_sound.play()
            else:
                print("player normal move")
                self.move_sound.play()

            self.flip_chance()
        else:
            return False

        return True

    def select(self, row, col):
        token = self.board.get_token(row, col)
        if self.selected:
            moved = self._move(row, col)
            if not moved and token!=0 and token.color == self.turn:
                self.selected = None
                self.select(row, col)
        else:
            if token != 0 and token.color == self.turn:
                self.selected = token
                self.valid_moves = self.board.get_valid_moves(token)
                # deadlock for player
                if (
                    self.valid_moves == {} and self.board.player_left == 1
                ) or self.check_tr():
                    self.board.player_left = 0
                return True
        return False

    def check_tr(self):
        return self.board.check_trap(self.turn)

    def ai_move(self, board):
        a1 = self.board.player_left
        a2 = self.board.ai_kings
        self.board = board
        b1 = board.player_left
        b2 = board.ai_kings
        if b2 > a2:
            print("ai kings increased")
            self.notify_sound.play()
        elif b1 < a1:
            print("player piece(s) captured")
            self.capture_sound.play()
        else:
            print("ai normal move")
            self.move_sound.play()
        self.flip_chance()

    def flip_chance(self):
        self.valid_moves = {}
        if self.turn == PLAYER_COLOR:
            self.turn = AI_COLOR
        else:
            self.turn = PLAYER_COLOR

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(
                self.win,
                VALID_MOVES_COLOR,
                (
                    col * SQUARE_SIZE + SQUARE_SIZE // 2,
                    row * SQUARE_SIZE + SQUARE_SIZE // 2,
                ),
                15,
            )

    def get_board(self):
        return self.board
