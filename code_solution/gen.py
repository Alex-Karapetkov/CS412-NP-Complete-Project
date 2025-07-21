import string
from itertools import combinations

def generate_vertex_labels(n):
    labels = list(string.ascii_lowercase)
    while len(labels) < n:
        labels += [s + t for s in labels for t in string.ascii_lowercase]
    return labels[:n]

def calculate_distance(p1, p2):
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5

def translate_data():
    n = int(input("Enter the number of cities: "))
    vertices = generate_vertex_labels(n)
    
    print("Enter the city coordinates:")
    coordinates = []
    for _ in range(n):
        _, x, y = map(float, input().split())
        coordinates.append((x, y))
    
    edges = []
    for i, j in combinations(range(n), 2):
        w = calculate_distance(coordinates[i], coordinates[j])
        edges.append((vertices[i], vertices[j], w))
    
    m = len(edges)
    with open('output.txt', 'w') as f:
        f.write(f"{n} {m}\n")
        for edge in edges:
            f.write(f"{edge[0]} {edge[1]} {edge[2]}\n")

translate_data()
