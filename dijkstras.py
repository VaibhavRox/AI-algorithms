import heapq

# Global distance dictionary
distances = {}

# Function to initialize distances
def initialize_distances(graph, start):
    global distances
    distances = {}
    for node in graph:
        distances[node] = float('inf')
    distances[start] = 0

# Dijkstra's algorithm
def dijkstra(graph, start):
    global distances
    initialize_distances(graph, start)

    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        if current_dist > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

# User input handling
def main():
    graph = {}
    num_nodes = int(input("Enter number of nodes: "))
    for _ in range(num_nodes):
        node = input("Enter node name: ")
        graph[node] = []

    num_edges = int(input("Enter number of edges: "))
    for _ in range(num_edges):
        u = input("Enter start node: ")
        v = input("Enter end node: ")
        w = int(input("Enter weight: "))
        graph[u].append((v, w))
        # Uncomment below if graph is undirected:
        # graph[v].append((u, w))

    start_node = input("Enter starting node: ")
    dijkstra(graph, start_node)

    print(f"\nShortest distances from {start_node}:")
    for node in graph:
        print(f"{start_node} -> {node}: {distances[node]}")

if __name__ == "__main__":
    main()
