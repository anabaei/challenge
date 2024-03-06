// Define the TreeNode class
class TreeNode {
    constructor(value) {
        this.value = value;
        this.children = [];
    }
}
// Function to perform Breadth-First Search (BFS) and return an array
function bfsTraversal(root) {
    const result = [];
    const queue = [root];
    while (queue.length > 0) {
        const node = queue.shift(); // Dequeue the front node
        // Visit the current node
        result.push(node.value);
        // Enqueue children nodes
        for (const child of node.children) {
            queue.push(child);
        }
    }
    return result;
}

// Example usage:
const root = new TreeNode(1);
const node2 = new TreeNode(2);
const node3 = new TreeNode(3);
const node4 = new TreeNode(4);
const node5 = new TreeNode(5);

root.children.push(node2);
root.children.push(node3);
node2.children.push(node4);
node2.children.push(node5);

const bfsArray = bfsTraversal(root);
console.log(bfsArray); // Output will be [1, 2, 3, 4, 5]
