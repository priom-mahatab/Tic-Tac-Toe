# Tic Tac Toe
A Python-based implementation of the classic Tic Tac Toe game using Minimax algorithm. This allows a player to compete against an AI. The AI ensures a challenging game for any player.

## Features
- **Player vs AI Mode:** Play against an intelligent AI.
  
- **Optimal AI Strategy:** The AI uses the Minimax algorithm to evaluate all possible moves and always choose the best one.
  
- **Customizable Gameplay:** The player can choose to first or second.
  
- **Simple Text-Based Interface:** Easy-to-follow text prompts for gameplay.

## How to Play
1. **Setup the Game:**
   - Clone the repository to your local machine.
     
   - Run the `tic_tac_toe.py` script using Python.
     
   - Rows and columns are indexed from 0 to 2 (0 being the first and 2 being the last).
2. **Make Your Move:**
   - Enter your move in the format `row,col` (e.g., `0,2`).
  
   - Rows and columns are indexed from `0` to `2`.
3. **Winning Conditions:**
   - Align three of your symbols (`X`) in a row, column, or diagonal to win.
  
   - If the board is full without a winner, the game is a draw.
  
## Algorithm Overview
- Uses **minimax** algorithm.
  
- Recursively evaluates all possible moves.
  
- **Maximizing for AI (0):** Chooses moves that maximize the score.
- **Minimizing for Player (X):** Chooses moves that minimize the AI's score.
- Considers all possible game states until the game ends.

## Example Game
```
Current Board:
  X |   |  
 ---+---+---
    | O |  
 ---+---+---
    |   |  

Player's Turn (X):
Enter your move as row,col (0-2): 0,1

Current Board:
  X | X |  
 ---+---+---
    | O |  
 ---+---+---
    |   |  

AI's Move (O):
Current Board:
  X | X |  
 ---+---+---
    | O |  
 ---+---+---
    |   | O
```

## How to Run
**1. Clone the repository:**
  ```
  git clone https://github.com/priom-mahatab/Tic-Tac-Toe.git
  ```
**2. Navigate to the project directory:**
  ```
  cd [folder-name]
  ```
  
**3. Run the game:**
  ```
  python3 tic_tac_toe.py
  ```
