import heapq

# Manhattan distance heuristic
def manhattan(state, goal):
    distance = 0
    for i in range(9):
        if state[i] != 0:
            x1, y1 = divmod(i, 3)
            x2, y2 = divmod(goal.index(state[i]), 3)
            distance += abs(x1 - x2) + abs(y1 - y2)
    return distance

# Get neighbors (possible moves with directions)
def get_neighbors(state):
    neighbors = []
    idx = state.index(0)  # blank position
    x, y = divmod(idx, 3)

    moves = [(-1, 0, "Up"), (1, 0, "Down"), (0, -1, "Left"), (0, 1, "Right")]
    for dx, dy, action in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_idx = nx * 3 + ny
            new_state = list(state)
            new_state[idx], new_state[new_idx] = new_state[new_idx], new_state[idx]
            neighbors.append((tuple(new_state), action))
    return neighbors

def astar(start, goal):
    pq = []
    heapq.heappush(pq, (manhattan(start, goal), 0, start, [], []))
    visited = set()

    while pq:
        f, g, state, path, moves = heapq.heappop(pq)

        if state in visited:
            continue
        visited.add(state)

        if state == goal:
            return path + [state], moves

        for neighbor, action in get_neighbors(state):
            if neighbor not in visited:
                new_g = g + 1
                new_f = new_g + manhattan(neighbor, goal)
                heapq.heappush(pq, (new_f, new_g, neighbor, path + [state], moves + [action]))
    return None, None

# -------- Main Program with User Input --------
def read_puzzle(prompt):
    print(f"Enter {prompt} state (3 rows, space-separated, use 0 for blank):")
    puzzle = []
    for _ in range(3):
        row = list(map(int, input().split()))
        puzzle.extend(row)
    return tuple(puzzle)

if __name__ == "__main__":
    start = read_puzzle("START")
    goal = read_puzzle("GOAL")

    print("\nSolving...\n")
    solution, moves = astar(start, goal)

    if solution:
        print(f"Solution found in {len(solution)-1} moves:\n")
        for i, state in enumerate(solution):
            for r in range(0, 9, 3):
                print(state[r:r+3])
            if i < len(moves):
                print(f"Move: {moves[i]}")
            print()
    else:
        print("No solution exists.")
