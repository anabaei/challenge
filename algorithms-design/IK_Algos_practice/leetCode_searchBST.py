
# search through a BST

"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
def search_node_in_bst(root, value):
    """
    Args:
     root(BinaryTreeNode_int32)
     value(int32)
    Returns:
     bool
    """
    # Write your code h
    curr = root
    while curr is not None:
        if curr.value == value: 
            return True
        elif(curr.value > value):
            curr = curr.left
        elif(value > curr.value):
            curr = curr.right
    return False