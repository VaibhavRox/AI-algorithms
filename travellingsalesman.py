from itertools import permutations

def read_input():
    # Step 1: Number of cities
    n = int(input("Enter the number of cities: "))

    # Step 2: Read city names
    city_names = []
    print("Enter the names of the cities:")
    for _ in range(n):
        city = input().strip()
        city_names.append(city)

    # Step 3: Read distance matrix (nested loop)
    graph = []
    for i in range(n):
        row = []
        for j in range(n):
            val = int(input(f"Enter distance from {city_names[i]} to {city_names[j]}: "))
            row.append(val)
        graph.append(row)

    # Step 4: Read starting city name
    start_city_name = input(f"Enter the starting city name (from {', '.join(city_names)}): ").strip()
    if start_city_name not in city_names:
        print("Invalid city name. Please restart and enter a valid one.")
        exit()

    start_city_index = city_names.index(start_city_name)
    return graph, city_names, start_city_index

def tsp_brute_force(graph, city_names, start):
    n = len(graph)
    cities = list(range(n))
    cities.remove(start)

    min_path = []
    min_cost = float('inf')

    for perm in permutations(cities):
        current_cost = 0
        k = start
        path = [start]

        for j in perm:
            current_cost += graph[k][j]
            k = j
            path.append(j)

        current_cost += graph[k][start]
        path.append(start)

        if current_cost < min_cost:
            min_cost = current_cost
            min_path = path

    # Convert numeric path to city name path
    named_path = [city_names[i] for i in min_path]
    return named_path, min_cost

# --- Main Program ---
graph, city_names, start_city = read_input()
path, cost = tsp_brute_force(graph, city_names, start_city)

# --- Output ---
print("\nShortest path:", ' → '.join(path))
print("Minimum cost:", cost)
