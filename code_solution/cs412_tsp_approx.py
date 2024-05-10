"""
    name: Alex Karapetkov
    412 NP-Complete Project:
        Traveling Salesman Problem
        Approximate Solution
"""
"""
CREDIT: Approximation method pseudocode is from CS 412 lecture on approximation algorithms

Approximate TSP Tour:

key idea: utilize the minimum spanning tree to find the shortest path

APPROX-TSP-TOUR(G, c)
    select a vertex r, an element of G.V, to be a "root" vertex
    compute a minimum spanning tree T for G from root r
        using MST-PRIM(G, c, r)
    let H be a list of vertices, ordered according to when they are first visited
        in a preorder tree walk of T
    return the hamiltonian cycle H


Performance Analysis:
    C: tour cost of approximate TSP tour
    C*: tour cost of optimal TSP tour
    C <= 2C*: 2-approximate algorithm
"""

import heapq

# function to create graph based on input edges
def create_graph(edges):
    graph = {}
    for edge in edges:
        node1, node2, weight = edge
        # add nodes and corresponding edges to graph
        if node1 not in graph:
            graph[node1] = []
        if node2 not in graph:
            graph[node2] = []
        graph[node1].append((weight, node1, node2))
        graph[node2].append((weight, node2, node1))
    return graph

# Prim's algorithm to find the minimum spanning tree
def prim(edges):
    graph = create_graph(edges)
    start_node = edges[0][0]
    # dictionary to track visited nodes
    visited = {node: False for node in graph}
    mst_edges = []
    edge_list = []

    # start from the first node
    visited[start_node] = True
    for edge in graph[start_node]:
        # add edges of root vertex to the priority queue
        heapq.heappush(edge_list, edge)

    # while there are still edges from original graph
    while edge_list:
        # find node from old graph with the smallest connecting edge to the new graph T
        weight, node1, node2 = heapq.heappop(edge_list)
        if visited[node2] == False:
            visited[node2] = True
            # add the edge and connected node to the minimum spanning tree
            mst_edges.append((node1, node2, weight))

            # add edges connected to the new node to the priority queue
            for edge in graph[node2]:
                if visited[edge[2]] == False:
                    # if connecting node has not been visited, add to pq
                    heapq.heappush(edge_list, edge)

    return mst_edges

# function performs dfs on the MST to generate list of vertices in the order they are visited
def preorder_walk(tree, root):
    def dfs(v):
        visited.add(v)
        tour.append(v)
        for w, _ in tree.get(v, []):
            if w not in visited:
                dfs(w)
    
    visited = set()
    tour = []
    dfs(root)
    return tour

# function computes MST using prim function, then generates the preorder walk of the MST using preorder function
# and then returns the Hamiltonian cycle formed by the preorder walk
def approx_tsp_tour(edges):
    # compute minimum spanning tree using Prim's algorithm
    mst_edges = prim(edges)
    root = edges[0][0]
    tree = {}

    # Build tree from MST edges
    for node1, node2, weight in mst_edges:
        if node1 not in tree:
            tree[node1] = []
        if node2 not in tree:
            tree[node2] = []
        tree[node1].append((node2, weight))
        tree[node2].append((node1, weight))

    # generate preorder walk of the minimum spanning tree
    H = preorder_walk(tree, root)
    H.append(root)

    # calculate total weight of hamiltonian cycle
    total_weight = 0
    for w in range(len(H) - 1):
        for node, weight in tree[H[w]]:
            if node == H[w + 1]:
                total_weight += weight
                break
    
    # add weight of edge from last node to first node
    for edge in edges:
        if (edge[0] == H[-2] and edge[1] == H[0]) or (edge[1] == H[-2] and edge[0] == H[0]):
            total_weight += edge[2]
            break

    return H, total_weight


# All modules for CS 412 must include a main method that allows it
# to imported and invoked from other python scripts
def main():

    # read input
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v, w = input().split()
        edges.append((u, v, float(w)))

    # compute TSP tour and print results
    tour, weight = approx_tsp_tour(edges)
    print(weight)
    tour_str = ' '.join(tour)
    print(tour_str)

    pass

if __name__ == "__main__":
    main()
