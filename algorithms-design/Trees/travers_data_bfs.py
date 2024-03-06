

## Traversal is a systematic way to visiting all nodes in tree

## In array you can traverse using index
## In linked list you can use while loop to go next
## For trees you can traverse level by level (BFS) or path in depth as (DFS)
## BFS search takes o(n) space and time o(n)
## Insert BFS
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

## Create a tree representing data
## BFS is one way to visiting all nodes
# [
# [2],
# [5, 4],
# [0, 1, 3, 6]
# ]
a = BinaryTreeNode(2)
a.left = BinaryTreeNode(5)
a.right = BinaryTreeNode(4)
a.left.left = BinaryTreeNode(0)
a.left.right = BinaryTreeNode(1)

a.right.left = BinaryTreeNode(3)
a.right.right = BinaryTreeNode(6)

### Level order traversal
# BFS 
# len(queue) is outside of the while loop which pops one by one, so
# it means regardless of how many we append into queue, the len decreases one by one based on first len which it started
# for example:
#  [1],
#  [2,3],
#  [4,5,6,7]
# first len of queue is 1 -> currSize =1 -> it pops value, insert into currList, insert left and child into queue, decreases currSize by one end while
# second len of queue is 2 -> currSize = 2 -> it pops two values and added them into currList, added their childs into queueu 
# third len of queue is 4 -> currSize = 4 -> ....
def levelOrder(root):
    result = []
    queue = []
    queue.append(root)
    while queue:
        currSize = len(queue) # always one step behind 
        currList = []
        while currSize > 0:
            currNode = queue.pop(0)
            currList.append(currNode.value) 
            currSize -= 1
            queue.append(currNode.left) if currNode.left else None 
            queue.append(currNode.right)  if currNode.right else None 
        result.append(currList)
    print(result) 

## BFS or LevelOrderTraverse if you want levels as well
levelOrder(a)

## BFS is simpler if you don't need to keep track of levels
## queue = root
## while queue is not empty
    ## print root.value 
    ## root.left push to queue
    ## root.right push to queue




