// check if a tree is bst or not

class TreeNode {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

function isBinarySearchTree(
  root,
  min = Number.MIN_SAFE_INTEGER,
  max = Number.MAX_SAFE_INTEGER
) {
  if (!root) {
    // An empty tree is considered a valid BST.
    return true;
  }

  if (root.value <= min || root.value >= max) {
    // The current node's value is outside the valid range.
    return false;
  }

  // Recursively check the left and right subtrees.
  return (
    isBinarySearchTree(root.left, min, root.value) &&
    isBinarySearchTree(root.right, root.value, max)
  );
}

// Example usage:
const root = new TreeNode(4);
root.left = new TreeNode(2);
root.right = new TreeNode(6);
root.left.left = new TreeNode(1);
root.left.right = new TreeNode(3);
root.right.left = new TreeNode(5);
root.right.right = new TreeNode(7);

console.log(isBinarySearchTree(root)); // Output: true
