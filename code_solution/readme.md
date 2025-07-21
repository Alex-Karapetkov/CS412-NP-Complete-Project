# 🧠 Code Solutions – TSP Project

This folder contains the core implementations for solving the Traveling Salesman Problem (TSP) using both approximation and exact algorithms.

## Files

- `cs412_tsp_approx.py` – 2-approximation algorithm using Prim’s MST and preorder DFS
- `cs412_tsp_optimal.py` – Exact solution using the 2-Opt heuristic
- `gen.py` – Utility to generate graph inputs from (x, y) coordinates
- `test_cases/` – Contains all input/output test files and scripts for automated testing

## Input/Output Format

Both the approximation and exact solutions accept input in the following format:

**Example Input:**
```
3 3
a b 3
b c 4
a c 5
```

- The first line contains the number of vertices `n` and the number of edges `m`.
- Each of the next `m` lines describes an edge in the format `u v w`, representing an edge between vertices `u` and `v` with weight `w`.

**Example Output:**
```
12
a b c a
```
- The first line is the total cost of the tour.
- The second line is the tour path, listing each visited vertex in order, ending back at the starting vertex to complete the cycle.

For usage instructions and project details, refer to the main [README](../README.md).
