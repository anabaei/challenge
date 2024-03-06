
# Traversing a heap or binary tree is not cache freindly
# Traversing an array is cach freindly because you dont need to go over all around cpu, everything 
# is in excuted order 


from heapq import heappop, heappush

def heap_sort(array):
    h = []
    for element in array:
        heappush(h, element)

    print(h)
    # While we have elements left in the heap
    ordered = []
    while h:
        ordered.append(h(heap))

    return ordered

array = [13, 21, 15, 5, 26, 4, 17, 18, 24, 2]
print(heap_sort(array))