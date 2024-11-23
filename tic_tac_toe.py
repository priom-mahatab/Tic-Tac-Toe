def create_board():
    board = [["" for _ in range(3)] for _ in range(3)]
    return board

def print_board(board):
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < len(board) - 1:
            print("--" * 3)

def check_winner(board):

    for i in range(3):
    # winner across row
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != "":
            return board[i][0]
    # winner across column
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != "":
            return board[0][i]

    # winner diagonally
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "":
        return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] and board[0][2] != "":
        return board[0][2]

    return None

def is_board_full(board):
    for row in board:
        for cell in row:
            if cell == "":
                return False
    return True

def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == "0":
        return 1 # AI winner
    elif winner == "X":
        return -1 # AI loser
    elif is_board_full(board):
        return 0 # draw

    if is_maximizing: # AI's turn
        best_score = -float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == "":
                    board[row][col] = "0"
                    score = minimax(board, depth + 1, False)
                    board[row][col] = ""
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == "":
                    board[row][col] = "X"
                    score = minimax(board, depth + 1, True)
                    board[row][col] = ""
                    best_score = min(score, best_score)
        return best_score

def best_move(board):
    """Determines the best move for AI"""
    best_score = -float('inf')
    move = None
    for row in range(3):
        for col in range(3):
            if board[row][col] == "":
                board[row][col] = "0"
                score = minimax(board, 0, False)
                board[row][col] = ""
                if score > best_score:
                    best_score = score
                    move = (row, col)
    return move

def player_move(board):
    move_made = False
    while not move_made:
        try:
            row, col = map(int, input("Enter your move as row, col (0-2): ").split(","))
            if board[row][col] == "":
                board[row][col] = "X"
                move_made = True
            else:
                print("This cell is already occupied. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. please enter row, col as per instructions.")

def play_game():
    board = create_board()
    game_over = False


    player_choice = input("Do you want to go first or second? (f/s): ").lower()
    if player_choice == 'f':
        player_turn = True
    else:
        player_turn = False

    print("Tic Tac Toe")
    print_board(board)

    while not game_over:
        if player_turn:
            # Player's turn first
            print("Player's turn (X):")
            player_move(board)
            if check_winner(board):
                print("You win")
                game_over = True
                continue
            if is_board_full(board):
                print("It's a tie!")
                game_over = True
                continue
        else:
            print("Computer's Turn (0):")
            move = best_move(board)
            if move:
                board[move[0]][move[1]] = "0"
            print_board(board)
            if check_winner(board):
                print("Computer wins!")
                game_over = True
                continue
            if is_board_full(board):
                print("It's a tie!")
                game_over = True
                continue

        player_turn = not player_turn

def main():
    play_game()

if __name__ == "__main__":
    main()