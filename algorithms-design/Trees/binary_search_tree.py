

################## BST Advantage over Sorted Array ####################
# - Insert is faster
# - Delete is faster 
##########################################################################
# - BST uses more space than array
# - BST search is not faster than sorted array
# - A none balance BST has no advantage over sorted array
# - A newly inserted node will always be a leaf in a BST
# - The successor of a node in a BST must always be found in its right subtree. If it has no right subtree, there is no successor. ?????
########################################################################


### Check null in python
   # key.data != None 

# predecessor : yeki ghabl az the node, the largest that is smaller than the root
# successor: yeki baed az node, the smalest that is bigger than the node.

# Find successor -> bigger element of a key
# Find predecessor -> smaller element of a key

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

############################################       
################ BST INSERT #################
################################################
    def insert(self, data):
    # Compare the new value with the parent node
      if self.data:
         if data < self.data:
            if self.left is None:
               self.left = Node(data)
            else:
               self.left.insert(data)        
         elif data > self.data:
               if self.right is None:
                  self.right = Node(data)
               else:
                  self.right.insert(data)
      else:
         self.data = data

    # Print the tree Min
    def PrintTreeInOrder(self):
        if self.left:
            self.left.PrintTreeInOrder()
        print( self.data)
        if self.right:
            self.right.PrintTreeInOrder()   
   # Print the tree Max
   # Print the tree Min would be self.left = left instead
   #  def PrintTreeMax(self):
   #      while self.right:
   #             self = self.right
   #      print(self.data)
   #      return None 
   # # Print the NofMin
   #  def findNmMin(self, n):
   #        cnt = 0
   #        self.findNmMinHelper(n, cnt)
   #  def findNmMinHelper(self, n, cnt):
   #      if self.left:
   #          self.left.findNmMinHelper(n, cnt)
   #      print(self.data, n, cnt)
   #      cnt +=1
   #      if self.right:
   #          self.right.findNmMinHelper(n, cnt) 
        
       
##############################################       
################ BST Search ###################
################################################
    def searchTree(self, key):
         # while current is not null  
            # if root = key return key
            # else if key < node.key 
            # key = node.left
            # else 
            # key = node.right
         while(self and self.data != None):
            
            print(self.data)
            if (self.data == key):
                  return key
            if (self.data == None):
                  return None
            elif(self.data > key):
               self = self.left 
            elif(self.data < key):
               self = self.right
         
         
         if self == None or self.data == None:
            return None
         print(key)




def delete(node, key):
 
      root = node 
      #search
      prev= None
      while(node != None and node.data != key): 
         if( key > node.data):
               prev = node 
               node = node.right  
         elif(key < node.data):
               prev = node 
               node = node.left 
         
      if(node == None):
            return False
      
      

      # Delete A Leaf Node
      elif(node.data == key and node.left == None and node.right == None):
            ## delete it
            
            if(prev.left == node):
                  prev.left = None
            elif(prev.right == node):
                  prev.right = None 
            # when it is root
            elif(prev.data == None):
                  root.data = key 
            return True 
      # Delete a node with one Child               
      elif(node.data == key and (node.left == None or node.right == None)):
            
            if(node.left != None):
               # root
               if(prev == None):
                     root = node.left
               elif(prev.left == node):
                     prev.left = node.left
               elif(prev.right == node):
                     prev.right = node.left
            elif(node.right != None):
                  # root
                  if(prev == None):
                        root = node.right
                  elif(prev.left == node):
                     prev.left = node.right 
                  elif(prev.right == node):
                     prev.right = node.right
         # Delete node with two subtrees, replace it with successor and remove successor
            else:
                  #find successor
                  successor = node  
                  nodelefprev = None 
                  if(node.data == key):
                     prev = node 
                     node = node.right 
                     while(node.left != None):
                           nodelefprev = node 
                           node = node.left
                     successor = node.data
                     #remove successor if successor doesnt have right child
                     # remmeber, successor (node here) don't have any left child, either has right or not
                     if(nodelefprev.right == node):
                        nodelefprev.right = node.right  
                     elif(nodelefprev.left == node):
                         nodelefprev.left = node.right 

root = Node(44)
root.insert(17)
root.insert(88)
root.insert(8)
root.insert(32)
root.insert(65)
root.insert(97)
root.insert(28)
root.insert(54)
root.insert(82)
root.insert(93)
root.insert(29)
root.insert(76)
root.insert(68)
root.insert(80)
#print(root.searchTree())
#root.PrintTreeInOrder()
#root.PrintTreeMax()
#root.findNmMin(2)
# delete(root, 97)
delete(root, 44)
root.PrintTreeInOrder()
#print("ss")



# Notice: nested function in python is acceptable:
# def oneLayer:
#     def secondLayer:

class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def search_node_in_bst(root, value):
        print(root)

# one class to create node on each insert
# one node to keep connected
# leetcode example 
def insert_bst(arr):
    def insert_array(root, item):
        if root is None:
            root = BinaryTreeNode(item)
            return root
        if (root.value is not None):
            if(item > root.value):
                root.right = insert_array(root.right, item)
            else:
                root.left = insert_array(root.left, item)
            return root

    root = BinaryTreeNode(arr[0])
    for item in range(1, len(arr)):
        insert_array(root,arr[item])
    return root
        

def travers_bst(node):
    if(node is None):
        return 
    travers_bst(node.left)
    print("node = ",node.value)
    travers_bst(node.right)



def find_max_bst(node):
    if node is None:
        return 
    # while(node.left):
    #     node = node.left
    # print(node.value)
    while(node.right):
        node = node.right
    print(node.value)


#### To delete if node has children, need to replace the node with its successor 

#### Successor of a node is another node with the next largest key (could be several level down)
#### Successor smallest in right tree
#### If node has right subtree, then next largest key is inside the right child  
####  -- and the closest of that would be the min number in right subtree
#### If node doesn't have right child, look at parents. 
##### --- If node is the left child of its parent, then its parent is successor
##### --- If node is the right child, go back til you find a node is 
##### left child of ancestor then that is successor
##### -------- first traverse from root to the node, then save the last time you saw node.left as ancestor var. 


#### Predecessor The predecessor is the largest node that is smaller than the root 
#### Predecessor is same as Successor, just need to change left to right or largest on the left tree
### If node has left subtree, then it would be the max value of that subtree 





arr = [7,5,9,4,1,5,7,99,3]
root = insert_bst(arr)



#travers_bst(root)
find_max_bst(root)