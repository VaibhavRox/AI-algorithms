import math

# ----------- Step 1: Representing the board -----------
board = [" " for _ in range(9)]  # 3x3 board stored as a list of 9 cells

# ----------- Step 2: Helper Functions -----------

def print_board():
    """Display the board in a 3x3 format."""
    for i in range(0, 9, 3):  # 0, 3, 6
        row = board[i:i+3]   # Take 3 elements at a time
        print(f"| {row[0]} | {row[1]} | {row[2]} |")


def check_winner(brd):
    """Check if there is a winner or if it's a tie."""
    win_patterns = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for pattern in win_patterns:
        if brd[pattern[0]] == brd[pattern[1]] == brd[pattern[2]] != " ":
            return brd[pattern[0]]  # Return "X" or "O"
    if " " not in brd:
        return "Tie"
    return None  # No winner yet

def available_moves(brd):
    """Return a list of available cell indices."""
    moves = []                     # Create an empty list
    for i in range(len(brd)):      # Go through all cells by index
        if brd[i] == " ":          # If the cell is empty
            moves.append(i)        # Add its index to the list
    return moves                   # Return the final list
# ----------- Step 3: Minimax Algorithm -----------

def minimax(brd,  is_maximizing):
    """Recursive minimax algorithm to choose the best move for AI."""
    result = check_winner(brd)
    if result == "O":  # AI wins
        return 1
    elif result == "X":  # Human wins
        return -1
    elif result == "Tie":
        return 0

    if is_maximizing:
        best_score = -math.inf
        for move in available_moves(brd):
            brd[move] = "O"  # AI makes a move
            score = minimax(brd, False)
            brd[move] = " "  # Undo move
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for move in available_moves(brd):
            brd[move] = "X"  # Human makes a move
            score = minimax(brd, True)
            brd[move] = " "
            best_score = min(score, best_score)
        return best_score

def best_move():
    """Find the best move for AI using minimax."""
    best_score = -math.inf
    move_chosen = None
    for move in available_moves(board):
        board[move] = "O"
        score = minimax(board, False)
        board[move] = " "
        if score > best_score:
            best_score = score
            move_chosen = move
    return move_chosen

# ----------- Step 4: Main Game Loop -----------

def play_game():
    print("Welcome to Tic Tac Toe!")
    print_board()

    while True:
        # Human turn
        move = int(input("Enter your move (0-8): "))
        if board[move] != " ":
            print("Invalid move! Try again.")
            continue
        board[move] = "X"

        if check_winner(board):
            print_board()
            print(f"Game Over! Result: {check_winner(board)}")
            break

        # AI turn
        ai_move = best_move()
        board[ai_move] = "O"

        print("\nAI made its move:")
        print_board()

        if check_winner(board):
            print(f"Game Over! Result: {check_winner(board)}")
            break

# Run the game
play_game()
