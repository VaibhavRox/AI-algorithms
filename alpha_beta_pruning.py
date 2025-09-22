"""
alpha_beta_demo.py

Beginner-friendly alpha-beta pruning demo.
- User inputs branching factor (b) and depth (d).
- The program expects b**d leaf values (space-separated). Press Enter to use a small default example.
- The program prints alpha/beta at every visited node and announces prunes.
- It also reports how many leaf nodes were skipped (pruned).
"""

import math
import random
import sys

def build_tree_from_leaves(leaves, branching, depth):
    """
    Build a complete tree (nested lists) from a flat list of leaves.
    Leaves are grouped bottom-up: at each iteration we group consecutive
    items into lists of size `branching` until we reach the root.
    """
    nodes = list(leaves)
    for _ in range(depth):
        if len(nodes) % branching != 0:
            raise ValueError("Number of nodes at this level is not divisible by branching factor.")
        new_nodes = []
        for i in range(0, len(nodes), branching):
            new_nodes.append(nodes[i:i+branching])
        nodes = new_nodes
    # nodes[0] is the root subtree (nested lists)
    return nodes[0]

def count_leaves(node):
    """Return how many leaves are in this subtree."""
    if not isinstance(node, list):
        return 1
    return sum(count_leaves(child) for child in node)

def alpha_beta(node, depth, alpha, beta, maximizing_player, path, prune_counter):
    """
    Recursive alpha-beta with:
    - prune_counter: dictionary to keep total pruned leaves across recursion
    - simpler path display
    """
    indent = "    " * depth

    # Base case: leaf
    if not isinstance(node, list):
        print(f"{indent}Leaf {path}: value = {node}")
        return node

    if maximizing_player:
        value = -math.inf
        print(f"{indent}MAX {path}: alpha={alpha}, beta={beta}")
        for i, child in enumerate(node):
            child_path = path + [i]  # path is now a list of indices
            child_value = alpha_beta(child, depth+1, alpha, beta, False, child_path, prune_counter)
            print(f"{indent}  Returned from {child_path}: {child_value}")
            value = max(value, child_value)
            alpha = max(alpha, value)
            print(f"{indent}  Updated MAX {path}: best={value}, alpha={alpha}, beta={beta}")
            if alpha >= beta:
                # Count pruned leaves
                remaining_leaves = sum(count_leaves(node[j]) for j in range(i+1, len(node)))
                prune_counter["count"] += remaining_leaves
                print(f"{indent}  PRUNE at MAX {path}! Skipping {remaining_leaves} remaining leaves")
                return value
        return value

    else:
        value = math.inf
        print(f"{indent}MIN {path}: alpha={alpha}, beta={beta}")
        for i, child in enumerate(node):
            child_path = path + [i]
            child_value = alpha_beta(child, depth+1, alpha, beta, True, child_path, prune_counter)
            print(f"{indent}  Returned from {child_path}: {child_value}")
            value = min(value, child_value)
            beta = min(beta, value)
            print(f"{indent}  Updated MIN {path}: best={value}, alpha={alpha}, beta={beta}")
            if alpha >= beta:
                remaining_leaves = sum(count_leaves(node[j]) for j in range(i+1, len(node)))
                prune_counter["count"] += remaining_leaves
                print(f"{indent}  PRUNE at MIN {path}! Skipping {remaining_leaves} remaining leaves")
                return value
        return value


def main():
    print("Alpha-Beta Pruning Demo (complete tree).")
    try:
        b = int(input("Enter branching factor (b, e.g. 2): ").strip() or "2")
        d = int(input("Enter depth (d, number of levels to leaves, e.g. 3): ").strip() or "3")
    except ValueError:
        print("Please enter integer values for branching and depth.")
        return

    if b <= 0 or d <= 0:
        print("Both branching and depth must be positive integers.")
        return

    leaves_needed = b ** d
    print(f"\nThis tree will require {leaves_needed} leaf values (b**d = {b}^{d}).")
    raw = input(f"Enter {leaves_needed} integer leaf values separated by space, or press Enter to use a default example: ").strip()

    if raw == "":
        # default example used for demonstration
        # For b=2, d=3 example we use: 3 5 6 9 1 2 0 -1
        default = [3, 5, 6, 9, 1, 2, 0, -1]
        if len(default) != leaves_needed:
            # generate deterministic default of proper length
            default = [i for i in range(leaves_needed)]
        leaves = default
        print("Using default leaves:", leaves)
    else:
        tokens = raw.split()
        if len(tokens) != leaves_needed:
            print(f"Expected {leaves_needed} values but got {len(tokens)}. Please run again and provide correct number.")
            return
        try:
            leaves = [int(t) for t in tokens]
        except ValueError:
            print("All leaf values should be integers.")
            return

    # Build tree
    root = build_tree_from_leaves(leaves, b, d)

    print("\nStarting alpha-beta search (root is a MAX node).")
    prune_counter = {"count": 0}
    best_value = alpha_beta(root, depth=0, alpha=-math.inf, beta=math.inf, maximizing_player=True, path=[], prune_counter=prune_counter)
    print("\nSearch complete.")
    print(f"Minimax value at root: {best_value}")
    print(f"Total pruned leaf nodes: {prune_counter['count']}")

if __name__ == "__main__":
    main()
