import pygame
from game_config import *
from game_logic import *
from algo import *

frames = 20
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Checkers Game implementation using Pygame package")
pygame.mixer.init()


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def main():
    # define difficulty level
    level = 3
    play = True
    game_instance = checkersGame(window)
    clock = pygame.time.Clock()

    while play:
        clock.tick(frames)
        if game_instance.winner() != None:
            if game_instance.winner() == "PLAYER":
                print("Congrats! You win!")
                pygame.mixer.Sound("resources/win.mp3").play()
            else:
                print("Sorry! AI win!")
                pygame.mixer.Sound("resources/loose.mp3").play()
            while (pygame.mixer.get_busy()):
                pygame.time.delay(1000)
            
            play = False
            continue

        if game_instance.turn == AI_COLOR:
            # Implementing Game Levels on the basics of difficulty by changing the depth
            # level = 3
            # EASY
            if level == 1:
                value, new_board = alphabeta_max(
                    game_instance.get_board(),
                    float("-inf"),
                    float("+inf"),
                    1,
                    game_instance,
                )

            # MEDIUM
            elif level == 2:
                value, new_board = alphabeta_max(
                    game_instance.get_board(),
                    float("-inf"),
                    float("+inf"),
                    2,
                    game_instance,
                )

            # HARD
            elif level == 3:
                value, new_board = alphabeta_max(
                    game_instance.get_board(),
                    float("-inf"),
                    float("+inf"),
                    3,
                    game_instance,
                )

            else:
                value, new_board = alphabeta_max(
                    game_instance.get_board(),
                    float("-inf"),
                    float("+inf"),
                    level,
                    game_instance,
                )

            # deadlock for ai
            if new_board == None:
                game_instance.board.ai_left = 0
                continue
            game_instance.ai_move(new_board)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Game Closed")
                play = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game_instance.select(row, col)

        game_instance.update()
    pygame.quit()

if __name__ == "__main__":
    main()
