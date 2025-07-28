from collections import deque

# Global graph dictionary
graph = {}

# Single function to create the graph (includes edge addition)
def create_graph():
    global graph
    n = int(input("Enter number of edges: "))
    print("Enter each edge as two nodes (e.g., A B or 1 2):")
    for _ in range(n):
        u, v = input().split()

        # Add edge u -> v
        if u not in graph:
            graph[u] = []
        graph[u].append(v)

        # Add edge v -> u (undirected)
        if v not in graph:
            graph[v] = []
        graph[v].append(u)

# BFS traversal
def bfs(start):
    visited = set()
    queue = deque([start])
    print("\nBFS traversal:", end=' ')
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex, end=' ')
            visited.add(vertex)
            queue.extend(neighbor for neighbor in graph[vertex] if neighbor not in visited)

# DFS (recursive)
def dfs_recursive(vertex, visited=None):
    if visited is None:
        visited = set()
        print("\nDFS Recursive traversal:", end=' ')
    print(vertex, end=' ')
    visited.add(vertex)
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(neighbor, visited)

# DFS (iterative)
def dfs_iterative(start):
    visited = set()
    stack = [start]
    print("\nDFS Iterative traversal:", end=' ')
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            print(vertex, end=' ')
            visited.add(vertex)
            stack.extend(reversed(graph[vertex]))

# Main
if __name__ == "__main__":
    create_graph()
    start_node = input("\nEnter start node for traversal: ")

    bfs(start_node)
    dfs_recursive(start_node)
    dfs_iterative(start_node)
