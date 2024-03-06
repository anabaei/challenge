# while we may only use from heapq import heappop, heappush 
# some cases we may need to know how this heap priority queue is implemented



# Insert element to heap then do heapify-up
# 1- add to the last node
# 2- compare with parent if is bigger( in max heap), swap
# 3- continue swapping til the element isn't bigger than parent

# Remove element (pop max)
# 1- Take element from the root
# 2- Put the last element from leaf to the root
# 3- then heapify-down
#  a- compare with left and right
#  b- smaller than both then compare two child, then swap it with the bigger one
#  c- swap until element is bigger than its child's

# In place heap sort
# - when poping the max, swap it with the last element, but keep a pointer 
# to know where is the array ends, do it 

# Heap sort in 