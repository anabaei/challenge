
# keybase is a tool to share secrets

# DFS Depth First Search
# hands on experience on Google Cloud Platform (GCP) installing and upgrading Kubernetes clusters including worker nodes, VPC, firewalls,  auto scaling with horizental pods and trouble shooting at cluster level
# Extensively implemented Terraform to create/manage cloud infrastructure
# Design and develop restful API and mvc pattern using Flask Python and node.js 

# To remember them always say there are three ways
    # Visit node from left -> Preorder 
        # before visiting the rest of nodes print it
    # Visit node from bottom -> Inorder 
        # after visiting left child and before visiting right child print it
    # Visit node from right -> Postorder
        # after visiting left and right child print the node val

#     a
#    / \
#   b   c
# Preorder: abc
# In order: bac
# Post Order: bca


#        1
#      /   \
#     2     3
#    / \      \
#   4   5      6
#      / \    / 
#     7   8  9

# preorder -> 124578369
# inorder  -> 427581396 -> print all smaller nodes first then its own node then node rest so -> 
# print the nodes in sorted or ascending order in bst -> give us a new sorted algo
# BST insertion is nlogn
# postorder -> 478529631 

def dfs(root):

#1 print before visit any subordinate 
    if(root.left):
        dfs(root.left) 
#2 print before visit right node and after visiting left node
    if(root.right):
        dfs(root.right)
#3 print after visiting left and right node



#                 TOC 
#           /               \
#    section1                 section2 
#       /  \                   /     \
# sec1.1   sec1.2           sec2.1   sec2.2
#           /  \                     /   \
#    sec1.2.1   sec1.2.2      sec2.2.1   sec2.2.2 
# Example 
# display above as 

# section1:
#  sec1.1
#  sec1.2 
#     sec1.2.1
#     sec1.2.2
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

a = BinaryTreeNode(2)
a.left = BinaryTreeNode(5)
a.right = BinaryTreeNode(4)
a.left.left = BinaryTreeNode(0)
a.left.right = BinaryTreeNode(1)


def helper(root, level):
    print(root.value, level)
    for l in range(level):
        print("*", end=' ')
    if(root.left):
        helper(root.left, level+1)
    if(root.right):
        helper(root.right, level+1)

def preorder(root):
    helper(root, 0)

preorder(a)


## If we have folder of files system in computer as 
## Tree and want to show the total size need to accomulate 
## all of them in postorder 

def postorder(root):
    du = node.space
    while node has child:
        du += du + postorder(child) 



### Preorder  return as an array so we need a helper method
def helper(node, result):

    result.append(node.value)
    if(node.left):
        helper(node.left, result)
    if(node.right):
        helper(node.right, result)
    return result
    


def preorder(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    result = []
    if (root == None):
        return result
    result = helper(root, result)
        
    
   
    return result