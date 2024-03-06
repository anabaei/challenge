* while we may only use from heapq import heappop, heappush 
* some cases we may need to know how this heap priority queue is implemented



* Insert element to heap then do heapify-up
* 1- add to the last node
* 2- compare with parent if is bigger( in max heap), swap
* 3- continue swapping til the element isn't bigger than parent

* Remove element (pop max)
* 1- Take element from the root
* 2- Put the last element from leaf to the root
* 3- then heapify-down
*  a- compare with left and right
*  b- smaller than both then compare two child, then swap it with the bigger one
*  c- swap until element is bigger than its child's

* In place heap sort
* - when poping the max, swap it with the last element, but keep a pointer 
* to know where is the array ends, do it 



### Do Heap sort in O(n)
* take an array, check only parents value with their childs, if they are smaller then swap. continue then it until it is bigger than its children 

### Calculate Heapify-down time
* Need to go down from root to the worse case to leaf which is h 
* Root needs logn or h time to reach to leaf
* leafs needs zero time 
```
      number of nodes * height need
leafs: 2^h * 0 
one above leaf: 2^h-1 * 1
...
root: 1 * h
```
* Above sum would be
```
2^h * 0 + 2^h-1 * 1 + 2^h-2 * 2 + .... + 2 * h < 2^h * 0 + 2^h-1 * 1 + 2^h-2 * 2 + .... + infinity
```
* It would be equal to a series of as below, i is a number of levels above the leaf
```
Z 2^h-i * i
2^h Z i/2^i < 2^h * 2 < n
```
* so worse case is O(n)
### Stable and inplace
* There are many `swaps` in Heap sorting, which is not `stable`
*  It is inplace
*  The largest number of keys that a heap of height h can contain is: 2^h+1 -1 : h=2 -> 7 nodes
*  The smallest number of keys that a heap of height h can contain is: 2^h