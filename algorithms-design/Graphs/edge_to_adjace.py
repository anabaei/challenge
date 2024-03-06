# Convert Edge List To Adjacency List

n= 5
edges= [
[0, 1],
[1, 4],
[1, 2],
[1, 3],
[3, 4]
]

# expect 
# [
# [1],
# [0, 2, 3, 4],
# [1],
# [1, 4],
# [1, 3]
# ]
# The graph won't contain self loops.

def partion(arr, start, end):
    
    pivot = arr[0]
    if(start < end):
        while(arr[pivot] >= arr[start]):
            start +=1
        while(arr[pivot] < arr[end]):
            end -=1
        arr[start], arr[end] = arr[end], arr[start]
        start +=1
        end -=1
    pivot = start - 1
    return pivot 

def helper(arr, start, end):
    
    if (start > end):
        return arr
    pivot = partion(arr, start, end)
    helper(arr, pivot+1, end)
    helper(arr, start,pivot-1)



def qsort(arr):
    # take a pivot 
    helper(arr, 0, len(arr)-1)

    return(arr)

def convert_edge_list_to_adjacency_list(n, edges):
    adjacency_list = [[] for _ in range(n)]
    for edge in edges:
        u, v = edge
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)
    return adjacency_list

print(convert_edge_list_to_adjacency_list(5, edges))