"""
    name: Alex Karapetkov
    412 NP-Complete Project:
        Traveling Salesman Problem
        Optimal Solution
"""

# References:
    # https://numpy.org/doc/stable/reference/routines.math.html
    # https://en.wikipedia.org/wiki/2-opt
    # https://slowandsteadybrain.medium.com/traveling-salesman-problem-ce78187cf1f3

"""
Input Specs:
Input is weighted graph specified by line containing the number of vertices n and the
number of edges m followed by m lines containing the edges given in u v w format,
representing an edge between u and v of weight w. TSP graphs are undirected and
edges will be listed only once and the graph will be a complete graph.

The output contains two lines: the length of the path on one line (as an integer)
followed by a list of vertices for the path/cycle on the second line

Example TSP input:
3 3
a b 3
b c 4
a c 5

Example TSP output:
12
a b c a
"""

import numpy as np

# calculate the total distance of the tour
def tour_distance(tour, dist_matrix):
    return np.sum([dist_matrix[tour[i-1]][tour[i]] for i in range(len(tour))])

# perform 2-opt swap
# takes current route, index of first node to be swapped, and index of second node to swap
def two_opt_swap(route, i, k):
    # copy current route
    new_route = route[:]
    # reverse order of nodes between indices i and k
    new_route[i:k+1] = reversed(route[i:k+1])
    return new_route

# 2-opt algorithm
# distance matrix as input; represents the distance between each pair of cities
def two_opt(dist_matrix):
    num_cities = len(dist_matrix)
    # initialize best_route as list containing indices of cities in order they are visited
    best_route = list(range(num_cities))
    # calculate total distance of initial tour with tour_distance function
    best_distance = tour_distance(best_route, dist_matrix)

    # stay in improvement loop until no more improvements can be made in any iteration
    improvement = True
    while improvement:
        improvement = False
        # iterate over all pairs of cities where i is index of starting city and k is index of ending city
        for i in range(num_cities):
            for k in range(i+1, num_cities):
                # for each pair of cities, generate new route by performing 2-opt swap on current best route
                new_route = two_opt_swap(best_route, i, k)
                # calculate total distance of new route
                new_distance = tour_distance(new_route, dist_matrix)

                # if new route distance is less than current best route distance, update current best route
                if new_distance < best_distance:
                    best_route = new_route
                    best_distance = new_distance
                    # continue iterating
                    improvement = True

    return best_route, best_distance


# All modules for CS 412 must include a main method that allows it
# to imported and invoked from other python scripts
def main():
    # read input
    n, m = map(int, input().split())

    # initialize empty dictionary to store the distances between vertices
    distances = {}

    # read edges and their weights
    for _ in range(m):
        u, v, w = input().split()

        # initialize distances for vertices u and v if not already created
        if u not in distances:
            distances[u] = {}
        if v not in distances:
            distances[v] = {}

        # add the edge weight to distance dictionaries of both vertices
        distances[u][v] = float(w)
        distances[v][u] = float(w)

    # create a list of vertices
    vertices = sorted(distances.keys())

    # create 2D numpy array to store distance matrix
    dist_matrix = np.zeros((n, n))

    # fill the distance matrix with the edge weights
    for i, u in enumerate(vertices):
        for j, v in enumerate(vertices):
            # use 'inf' if no direct edge between u and v exists
            dist_matrix[i][j] = distances[u].get(v, float('inf'))

    # solve the TSP
    route, distance = two_opt(dist_matrix)

    # map the route indices back to vertex labels
    route_labels = [vertices[i] for i in route]

    # append first node to end of route to complete hamiltonian cycle
    route_labels.append(route_labels[0])

    print(distance)
    tour_str = ' '.join(route_labels)
    print(tour_str)

    pass

if __name__ == "__main__":
    main()
