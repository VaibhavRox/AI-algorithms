def print_state(state):
    for row in state:
        print(' '.join(map(str, row)))
    print()

# Find the position of the empty tile (0)
def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Check if (r, c) is within bounds
def is_valid(r, c):
    return 0 <= r < 3 and 0 <= c < 3

# Convert 2D list to hashable form
def serialize(state):
    return tuple(tuple(row) for row in state)

# Generate new states by sliding 0
def get_neighbors(state):
    neighbors = []
    r, c = find_zero(state)
    
    directions = {
        'Up': (-1, 0),
        'Down': (1, 0),
        'Left': (0, -1),
        'Right': (0, 1)
    }

    for move, (dr, dc) in directions.items():
        nr, nc = r + dr, c + dc
        if is_valid(nr, nc):
            # Manual deep copy workaround
            new_state = [row[:] for row in state]
            new_state[r][c], new_state[nr][nc] = new_state[nr][nc], new_state[r][c]
            neighbors.append((new_state, move))
    return neighbors

# DFS Algorithm
def dfs(start, goal, max_depth=50):
    stack = [(start, [], 0)]  # (state, path, depth)
    visited = set()
    
    while stack:
        state, path, depth = stack.pop()
        serialized = serialize(state)
        
        if serialized in visited:
            continue
        visited.add(serialized)
        
        if state == goal:
            return path
        
        if depth >= max_depth:
            continue
        
        for neighbor, move in get_neighbors(state):
            stack.append((neighbor, path + [move], depth + 1))
    
    return None  # No solution found

# Take user input for a 3x3 puzzle
def get_input(prompt):
    print(f"\nEnter {prompt} state (3 rows, space-separated, use 0 for blank):")
    state = []
    for _ in range(3):
        row = list(map(int, input().strip().split()))
        state.append(row)
    return state

# Main
if __name__ == "__main__":
    start_state = get_input("start")
    goal_state = get_input("goal")

    print("\nStarting DFS...")
    solution = dfs(start_state, goal_state)

    if solution:
        print("\n✅ Solution found!")
        print("Number of moves:", len(solution))
        print("Moves:", solution)
        print("\n🏁 Goal state:")
        print_state(goal_state)
    else:
        print("\n❌ No solution found (try increasing depth or check solvability).")
