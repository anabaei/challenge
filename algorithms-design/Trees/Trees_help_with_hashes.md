
# Hashes in Abstract Data types
* There are two different ADT: Contiguous one like arrays and link lists
* Trees helps us to optimize time in arrays and linked lists

## Arrays with Hash tables
#### When keys are not integer
* if keys are just numbers like
```
red -> 3       
blue -> 25
green ->22
purple ->11
orange -> 9
// Above is called hash function
```
* careful to not have collisions because of having the same index
* then use mode%14 to get smaller integers. use numbers as indices
* So we do insert, search and delete in O(1) time

## Linked List with hash table (create a bst)

* Sorted Linked List: search, delete, insertion are O(n)
* Unsorted Linked list: search, delete = O(n), insert O(1)
* We can define a binary tree using linked list. it means it start from root and on the left and right are two leafs and etc..
* Should be balance binrary search tree
* 
  