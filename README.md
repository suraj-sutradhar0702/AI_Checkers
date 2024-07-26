# AI_Checkers

Welcome to **AI_Checkers**, an implementation of the classic Checkers game with AI capabilities. This project utilizes Alpha-Beta Pruning to enhance the gameplay experience by providing a challenging opponent.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [How It Works](#how-it-works)
- [Levels](#levels)
- [Screenshots](#screenshots)

## Introduction

**AI_Checkers** is a Checkers game built using Python's Pygame library for the graphical user interface. It integrates an AI opponent that uses the Alpha-Beta Pruning algorithm to make strategic decisions. This project is designed to offer an engaging experience for players of all levels.

## Features

- **Play Against AI**: Challenge an AI opponent with advanced decision-making capabilities.
- **Graphical User Interface**: Intuitive and user-friendly interface built with Pygame.
- **Alpha-Beta Pruning**: Efficient search algorithm to enhance AI performance.
- **Game History**: Keep track of game moves and history.
- **Adjustable AI Difficulty Levels**: Customize the difficulty of the AI opponent.

## How It Works

The AI_Checkers game leverages the Alpha-Beta Pruning algorithm for its AI opponent. Here’s a brief overview:

1. **Game Setup**: The game initializes with a standard 8x8 Checkers board setup.
2. **Player Moves**: Players can make moves using the Pygame GUI, which updates the board state.
3. **AI Moves**: The AI evaluates potential moves using Alpha-Beta Pruning, optimizing its decisions to challenge the player.
4. **Game End**: The game continues until a win or draw condition is met, with appropriate messages displayed.

For a detailed explanation of the AI algorithm and game logic, refer to the algo and game_logic files in the project.

## Levels

The game includes adjustable AI difficulty levels. The `level` variable can be modified before running play_checkers.py to set the AI's difficulty. Changing `level` variable increases the depth (number of moves which the program tries to explore) for searching the best possible move.

## Screenshots
- Initial Game Setup
  <br><br>
  <img src="https://github.com/user-attachments/assets/741791d2-b8ed-425f-a9b7-e2597fd595dc" width="500" />
  <br><br>
- Single Move Example
  <br><br>
  <img src="https://github.com/user-attachments/assets/e1da24a0-1341-4cb3-96ac-b44deb3ec636" width="500" />
  <br><br>
- Multiple Move Example
  <br><br>
  <img src="https://github.com/user-attachments/assets/d28d41f1-4eac-4924-a457-24086b1ec6bb" width="500" />
  <br>
