from game_config import *
import pygame


class Token:
    PADDING = 15
    OUTLINE = 4

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        if color == AI_COLOR:
            self.outline_color = OUTLINE_COLOR_AI
        else:
            self.outline_color = OUTLINE_COLOR_PLAYER

        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def make_king(self):
        if self.king == False:
            self.king = True
            return True
        else:
            return False

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    def draw(self, win):
        radius = SQUARE_SIZE // 2 - self.PADDING
        pygame.draw.circle(
            win,
            self.outline_color,
            (self.x + self.OUTLINE, self.y + self.OUTLINE),
            radius,
        )
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        if self.king:
            win.blit(
                CROWN,
                (self.x - CROWN.get_width() // 2, self.y - CROWN.get_height() // 2),
            )

    def __repr__(self):
        return str(self.color)
