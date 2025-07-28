from collections import deque

def can_measure_water_bfs(A, B, C):
    if C > A + B:
        return False

    visited = set()
    q = deque()
    q.append((0, 0))  # Start from empty jugs

    while q:
        a, b = q.popleft()
        if a == C or b == C or a + b == C:
            return True

        if (a, b) in visited:
            continue
        visited.add((a, b))

        # Possible states:
        q.append((A, b))             # Fill Jug A
        q.append((a, B))             # Fill Jug B
        q.append((0, b))             # Empty Jug A
        q.append((a, 0))             # Empty Jug B

        # Pour A → B
        pour = min(a, B - b)
        q.append((a - pour, b + pour))

        # Pour B → A
        pour = min(b, A - a)
        q.append((a + pour, b - pour))

    return False