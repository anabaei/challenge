

def convert_edge_list_to_adjacency_matrix(n, edges):
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    for edge in edges:
        u,v = edge
        res[u][v] = 1
        res[v][u] = 1
    return edges 



edges=  [
[0, 1],
[1, 4],
[1, 2],
[1, 3],
[3, 4]]

convert_edge_list_to_adjacency_matrix(5, edges)
# [0, 1, 0, 0, 0],
# [1, 0, 1, 1, 1],
# [0, 1, 0, 0, 0],
# [0, 1, 0, 0, 1],
# [0, 1, 0, 1, 0]

class Graph:

    