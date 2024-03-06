# check_if_eulerian_cycle_exists
    # Check if there exists any eulerian cycle in 
    # a given undirected connected graph. 
    # The Euler cycle is a path in the graph that 
    #visits every edge exactly once and starts and 
    # finishes at the same vertex.

# Solution
# check each edge has even degree
# check if all vertices visited 

# To check Eulerian Path exist, check there are only 2 vertic only with odd numbers
[0,0] [0,1] [1,1] [0,1] 
a  -   b  -   c -  d - a  



edges = {
"n": 5,
"edges": [
[0, 1],
[0, 2],
[1, 3],
[3, 0],
[3, 2],
[4, 3],
[4, 0]
]
}


def check_if_eulerian_cycle_exists(n, edges):
    
    edge_cnter = {}
    if(len(edges["edges"]) == 0 or edges is None):
        return False
    for edge in edges["edges"]:
        for vertex in edge:
            # edge_cnter[vertex] +=1 if vertex in edge_cnter else false_val
            if( vertex in edge_cnter):
                edge_cnter[vertex] +=1
            else:
                edge_cnter[vertex] = 1

    if(len(edge_cnter)!= n):
        return False
    
    for key in edge_cnter:
        if(edge_cnter[key]%2 == 1):
            return False 
        if(edge_cnter[key] == 0):
            return False 
    return True


print(check_if_eulerian_cycle_exists(5, edges))

