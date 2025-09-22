def is_safe(assignment, row, col):
    """
    Check if we can place a queen at (row, col) given the current assignment.
    assignment is a dictionary {row: column}.
    """
    for r, c in assignment.items():
        if c == col:           # same column
            return False
        if abs(r - row) == abs(c - col):  # same diagonal
            return False
    return True

def backtrack(assignment):
    """
    Backtracking CSP solver:
    - assignment: {row: col} for already placed queens
    """
    if len(assignment) == 4:  # all 4 queens placed
        return assignment

    row = len(assignment)  # choose next row
    for col in range(4):
        if is_safe(assignment, row, col):
            assignment[row] = col
            result = backtrack(assignment)
            if result:
                return result
            del assignment[row]  # backtrack
    return None

def print_board(solution):
    """Pretty print the board with Q for queen and . for empty cell."""
    for r in range(4):
        row = ""
        for c in range(4):
            if solution.get(r) == c:
                row += "Q "
            else:
                row += ". "
        print(row)
    print()

def main():
    print("4-Queens Problem with User Input")
    assignment = {}

    # Step 1: Take user input for initial queens
    n = int(input("How many queens do you want to pre-place? (0 to 3): ") or "0")
    for _ in range(n):
        while True:
            try:
                row = int(input("Enter row (0-3): "))
                col = int(input("Enter column (0-3): "))
                if row in assignment:
                    print("There is already a queen in this row! Choose another row.")
                elif not is_safe(assignment, row, col):
                    print("This position conflicts with existing queens! Choose another position.")
                else:
                    assignment[row] = col
                    break
            except ValueError:
                print("Invalid input. Please enter integers between 0 and 3.")

    print("\nStarting CSP solver...")
    solution = backtrack(assignment.copy())

    if solution:
        print("\nSolution found:")
        print_board(solution)
    else:
        print("\nNo solution possible with given pre-placed queens.")

if __name__ == "__main__":
    main()
