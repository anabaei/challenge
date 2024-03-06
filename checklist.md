
# Checklist

1- Sorting
2- arrays 
2- Trees
3- Graphs
3.5 - Dynamic programming
4- Node.js
5- React





### Sorting 
* Quick sort average and best O(nlogn), worse O(n^2)
* Merge sort average, best, worst O(nlogn)
* Quick-sort is in place sorting which doesn't need axillary array but merge-sort need it
* Both quick-sort and merge-sort are recursive which needs call stack space
* If array size is billions then quick sort takes 12 min, merge-sort takes 18 minutes and insertion-sort takes 317 years!!
* quick sort works better in big inputs
* quick sort is in place but merge-sort is not
* Merge sort does have advantage of stability
  
### Stability (in sorting)
* It means if two items in have same key values, when sorting their location stay with no change 
* `Selection sorting` is not stable (because we swap values). 
nested loop array on each index, select min from the rest of array, use temp var to save min_val, and replace it at the end then add one to index.
* `Bubble sorring` is stable. It only compares itself with the next to it, but in selection it compares through whole array
* `Insertion sort` is stable (check one by one push to right ). Nested loop only check with previose if it is smaller then, left to right and check again. This logic is as 
```javascript
while j >= 0 and  key < arr[j]:
                arr[j+1] = arr[j]
                j = j-1
            arr[j+1] = key 
```
* `Merge sort` is stable (two array with same value, the left one goes first)
* `Quick sort` no it is not stable (because we swap values)

* `Java` uses quicksort for primitives and merge-sort for objects to keep stability
* `Timsort` is stable and python use it

# Which of the following algorithms are stable?
* Bubble, Insertion, Merge

### Mergesort
```javascript
- take midpoint, split into half
- recurse on each half, until we left element of size 1
- then merge them, take two pointers and put smallest in first index
- Time: O(nlogn)
- Space: O(n)
- Stability: true, 
```
### Quicksort
```python
- select a pivot
- compare all elements with pivot
- set a pointer to left most index, 
- if smaller, put in the left most index and increase one the index
- then decrease the left most index by one, swap with pivot and return it as final pivot
- time O(nlogn)
- worst case if it is sorted and you take the last one as pivot, it would be O(n^2)
- Space: O(1) 
- stability: false
```

## Trees 
### BST Binary Search Tree (at trees)
* create, insert, delete and traverse 
  * treavers inorder, preorder, levelorder (did this example)

### BFS and DFS
 * Write BFS traversal
 * Write DFS and 3 versions 
 * Bottom up level order traversal (associate with dfs)

### Time Complexity
* DFS time complexity is O(n) -> need to touch each node once, space complexity - > O(logn) height of tree
* BFS space complexity - > O(n) number of leaves
  
Difference between Binary Tree & Binary Search Tree
```
Binary Tree has only two childs
Binary Search Tree left child is less than root, right child bigger than root
```
```
this pseudocode compute the sum of all the keys in a t

def computesum(TreeNode root):
    if root is null, return 0
    leftsum = computesum(root.left)
    rightsum = computesum(root.right)
    return root.key + leftsum + rightsum
```
* What is the worst-case time complexity of searching for an element in the following data structures with n nodes: unbalanced binary tree/ balanced binary tree/ unbalanced binary search tree / balanced binary search tree / binary search in a sorted array
```
n/n/n/logn/logn
```

### Binary Heap (priority queue)
* Is a basic binary tree, which the most important element is the root(min or max) could be. 
* Sorting in binary heap takes logn and extract is 1. So extract n elements from a binray heap and insert into array takes nlogn to create a sorted array   
```javascript
time: O(nlogn) : no worse case 
space: O(1)
```

4+6/2 = 5, 4 + 6-4/2 = 5 

merge sort 
```javascript
helper_merge(arr, start, end)
   
   if(arr.length<2)
      return 
   pivot = start+ (end-start)/2
   rightpart = helper_merge(arr,pivot+, end)
   leftpart = helper_merge(arr,start, pivot)
  
  k=0
  i=0
  j=0
  while(i < rightpart.length && j < leftpart.length)
     if(rightpart[i]< leftpart[j])
       result[k] = rightpart[i
       i++
       k++
  ...

  while(i < rightpart.length)
       result[k] = rightpart[i
       i++


  

  pivot(arr, left, right)

  if(arr>1)
  privot = left
  leftmostindex = left+1

  for i in range(left+1, right+1)


    helper_qs(arr, left, right)
    if(left < right)
    pivot = partition(arr, left, right)
    helper_qs(arr, left, pivot-1)
    helper_qs(arr, pivot+1, right)
     
     if()
    pivot = partition(arr, pivot)


qs(arr)
{
 
  helper_qs(arr, 0,arr.length)
}
```
## Sample Questions

### FullStack 

<details> 
  <summary> Given a webpage, create accordions and sort lists amz </summary>

</details>
<details> 
  <summary> Create Sort list based on the types, wmo </summary>

</details>
<details> 
  <summary> Calculate average speed of two cars in specific time, wmo </summary>

</details>
<details> 
  <summary> Rewrite select className but selecting items using classList, children element, class list combination  zlt</summary>

</details>


### Array Manipulation

<details> 
  <summary> Move Zeros to Center </summary>

* Traverse array `[0, 2, 3, 0, 0, 4, 5, 0, 6]`, 
* Find zeros length `const zeroCount = arr.filter(item => item===0 ).length;`
* Create result array, define zeros left, then traverse via array push to result and finally add zeros to right
* Time and space complexity is O(n).
* To improve using O(1) spaces, we can use two pointers, 
* `i` check index, if not equal to zero in leftzeros or right zeros zone, move `j` to right and swap with the first `0` occurance,
* if it is in after leftzone index, then swap with the last index and decrease `j` by one

</details>

<details> 
  <summary> Given numbers i,j, k ibm</summary>

create a function to provide below question


given three integers, i, j and k, a sequence sum to be value of i + (i+1) + (i+2) + (i+3) ... + j + (j-1) + (j-2) + (j-3) + .... + k(increment from i until it equals j, then decrement from j until it equals to k. 


example
I = 5, j =9, k=6 sum all values from I to j and k back to K: 5+6+7+8+9+8+7+6 = 56
complete the function getSequeneceSum 

I= 0, j = 5, k =-1  expected output should be 24

</details>
<details> 
  <summary> Convert Integers to Roman Values </summary>

*  write a function to get an integer convert to roman equivalent 
```
example numbers = [1,49,23]  output ["I", xlix, 'xxiii']

xl.    1.   I. 40
l.     2  II  50
xc 3  III 90
c  4 IV 100
cd 5 V 400
d 6 VI 500
cm 7 VII 900
m 8 VIII 1000 
9 IX
10 X

```
* Solutions
```javascript
"use strict";

function intToRoman(num) {
  const romanNumerals = [
    { value: 1000, numeral: "M" },
    { value: 900, numeral: "CM" },
    { value: 500, numeral: "D" },
    { value: 400, numeral: "CD" },
    { value: 100, numeral: "C" },
    { value: 90, numeral: "XC" },
    { value: 50, numeral: "L" },
    { value: 40, numeral: "XL" },
    { value: 10, numeral: "X" },
    { value: 9, numeral: "IX" },
    { value: 5, numeral: "V" },
    { value: 4, numeral: "IV" },
    { value: 1, numeral: "I" },
  ];

  let result = "";
  for (const numeral of romanNumerals) {
    while (num >= numeral.value) {
      result += numeral.numeral;
      num -= numeral.value;
    }
  }

  return result;
}

// Example usage:
const numbers = [1, 49, 23];
const romanNumerals = numbers.map(intToRoman);
console.log(romanNumerals); // Output: ['I', 'XLIX', 'XXIII']

```

</details>


<details> 
  <summary> Convert selectByClass,  big companies </summary>

* Write a function to replace selectByClass, imagine classes could be a combination of two or more words
* Here is an example of body
```html
<!DOCTYPE html>
<html>
<head>
    <title>HTML Body with a Div</title>
    <style>
        /* Example CSS for styling the div */
        .my-div {
            background-color: lightblue;
            padding: 20px;
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="my-div">
        <h1>Welcome to My Web Page</h1>
        <p>This is a sample HTML body with a div element.</p>
    </div>
</body>
</html>
```
* Rewrite functions to read body, select classes using classLists, not select byClass or other tools.


</details>

<details> 
  <summary> Find all the words in any direction in 2d array, varicent </summary>

* 

</details>

<details> 
  <summary> 3sum </summary>

* 3 pointers one current, another travers from right end, another travers after i
* Since it is sorted so we know when we should move which,
* if left+right+ current > target => move right poiner to left, if bigger move left pointer to right
* do while left < right
* Need to sort input as 
```
arr.sort((a,b)=> a-b))
```


</details>

<details>
   <summary> TickTakToe</summary>

* There are unlimite of cakeTypes, make most of profit based on their values while considering you only have limited capacity
```javascript
const cakeTypes = [
  { weight: 7, value: 160 },
  { weight: 3, value: 90 },
  { weight: 2, value: 15 },
];

const capacity = 20;

maxDuffelBagValue(cakeTypes, capacity);
// Returns 555 (6 of the middle type of cake and 1 of the last type of cake)
```

</details>

<details>
   <summary> TickTakToe</summary>

* create 3*3 
* input receive position with X:O
* checkfunction:
* There are 8 possible solutions, so 

</details>


<details>
   <summary> Move zeros to center in 2d array, varicent</summary>

* Travers trough each row, col by col, if zero is not in the eachside zeros, then put zero there
* 
</details>

<details>
   <summary> Given a an array of objects find all possible ways they connect each other, aws</summary>

* 

</details>


<details>
   <summary> Given an array of monyes with values, give us change with biggest moneys </summary>

* 
</details>


#### System

<details>
   <summary> Design a waiting room, aws</summary>

</details>
<details>
   <summary> Design an app to show current location of cars </summary>

</details>

<details>
   <summary> Design an live camera detector</summary>

</details>

#### Linked List

<details>
    <summary>
    Delete a node
    </summary>

* Delete a node
```javascript
  class LinkedListNode {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

  function  deleteNode(b){
  
    const nextnode = b.next;
    if(nextnode.value){
        b.value = nextnode.value;
        b.next = nextnode.next;
      
    }
    else(
      console.log('cant delete node which is the last one with this technique')
    )
   
} 

const a = new LinkedListNode('A');
const b = new LinkedListNode('B');
const c = new LinkedListNode('C');

a.next = b;
b.next = c;

deleteNode(b);
```

* Need to traverse via linkedlist, keep one pointer behind the current, find the value, from poiner b, changed the next value to the next value of pointer a
* `Better Solution` Take the next node value and next and put it into the current node you want to delete. (we can't delete the last node with this technique), but we can create a null node and replace it in this case
* Also another problem is we just replace node b with a new value, if in some cases there are other pointers to this node which expect to have the old value then it would be issue
* the node c would be a dangling node then sence no node reach it out again (we basically duplicate it)

##### Complexity

* O(1) time and O(1) space
* In-place operations like this can save time and/or space, but they're risky and can cause other parts of the surrounding system to break.
</details>

#### FE

<details>
   <summary>stup Design a todo with modules which can inheritate from each other state using context</summary>

</details>

<details>
   <summary>waymo Design a list to retrieve from third party and sort them b ased on name, date using REACT</summary>

</details>

<details>
   <summary>amz Create Accordions using only html, javascript</summary>

</details>

<details>
   <summary>amz Create a form, to submit infos, save them into an object, order them and display only html, javascript</summary>

</details>

<details>
   <summary>ibm, convert a selectbyclass using classlist, when class is two or three words javascript</summary>

</details>
<details>
   <summary>ibm, convert a an array of digits to roman numbers javascript</summary>

</details>






