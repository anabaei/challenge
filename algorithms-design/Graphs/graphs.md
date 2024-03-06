
# Graphs 
* Epic example is salesman. To solve a graph problem you need to do the following
```
Could the problem be model as a graph
Would a simple graph traverse solve it
Would some popular extensions helps to solve it
Code it
```

### Adjlist
* 2d array of arrays. 
* Initialize 
```python
# edges= [(0,1),(2,1),(1,2)]
adjlist = [[] for _ in range(n)]
adjlist = [[-1] for _ in range(4)]

for edge in edges:
  adjlist[edge(0)].append(edge(1))
```
* If graph is not dense, we use adjlist. If it is dense we use adjmatrix


### BFS Graph (you should do it in 2 min)

```python
TC: O(E+V) # we traverse each edge and on each eadge we check nodes that not visited, so it is all edges + all nodes
SC: O(V+V+E) ~ O(V+E) # need to save vertices in qs, for adjlist needs E
```
* Is level by level traverse a graph. For this we need a queue to holds all neighbours to be visited in next round
* Start from node A, save it into a hash table call visited nodes, put negbours in the queue, check them if they are not visited yet, then continue until the queue is empty.
* FIFO  
```graph
Adjacy List
a -> b,e
b -> c,f,a
c -> d,b,g
d -> c,e,g 
e -> a,d
f -> b,g
g -> d,f,c
```
```python
a = {}
a["a"] = []
a["a"].append("b")
```
```python

def bfs(s):
  visited[s] = 1
  q.push(s)
  while q not empty:
    v = q.pop()
    for w in Adj(v):
      if visited[w] == 0 then
        visited[w] = 1, parent[w] = v
        q.push(w)  
```
### DFS Graph
* At any point, we get as deep as possible, then if not anymore not visited vertex, it recursively back to previous node
* FILO
```python
def dfs(source):
  visited[source] = 1
  for neighbor in adjlist[source]:
    if visited[source] == -1:
      dfs(neighbor)
```

### Number of connected components in a graph
* We have a give graph, we want to know how many components is it, it means how many separated graphs
```python
create adjlist

for each node:
  if visited[node] == -1:
      do bfs
      cnt++

return cnt
```

### Find a Cycle
* Use BFS, add one condition at then end
```python
bfs ...
# add below 
 parent[vertex] = edge
 if visited[vertex] == 1 and parent[vertex] != vertex
    return false  
```

### How to know if a graph is tree
* A valid tree is a graph that
  * No cycle
  * all vertices connected (check connected components less than 2)
* You can find it with BFS/DFS
```python
Number of connected ...
  if cnt > 1:
    return false
  if findCycle(noe) == true:
    return false
##add connected component here
TC: O(E+V)
TS: O(V+E+V) ~ O(E+V) # Second V is for parent hash table
```
### Bipartite TODO
* You have a graph, you can put nodes in A or B only. 
  * Nodes should connect to other side
  * Nodes should not connect on the same side
* Since every node has two options so number of possibilities are 2^n - 1 in brute force approach
* Solution
```python
If there is any odd cycle inside graph, the graph is not Bipartite
Use BFS
   add distance[node] to each node is visited as
   distance[w] = distance[v] +1

   if(visited[w] == 1 and distance[w] == distance[v]):
     return false
```


### Snake and Ladder TODO
* Similar leetcode "string transforms into another string"
* Given a snake and ladder game, find the min number of throws require to win the game, when reach to 100 
* Create Hmap[i+dice] , dice = 1..6, i = 1..100
```python
Hmap[1] = 38 #ladder
Hmap[2] = 2 #normal
Hmap[3] = 3 #normal
Hmap[4] = 1 #snake

```
* Write a graph as:
```python
for each i in 0 to 100:
  for dice in 1 to 6:
    if i+dice <= 100:
      adjList[i].append(Hmap[i+dice])
#keep distance, 100 of -1 initialize visited = [-1]^101 
distance = [-1,-1, ..., -1]  
TO(V+E) = V + 6*V, where v=100 ~ O(7V) ~ O(V)

```
* To optimization we cen use Dijkstra, Bellmen-ford if there are negative weight gives us shortest path

### BFS (Directed Graph)
* BFS is not good solution to find a cycle in Directed graph because detecting of a backage( a back to other nodes) to crossage is not easy
  
### DFS (Directed Graph)
* Look at all neighbours, if it is not visited look at it recursively
* Use DFS but with small changes calling bookkeeping
* We add one global clock, and everytime we reach to a node, we increase the time to set up arrival time `arr[source]= time++`
* When the node is done with its recuresives, we tag this node as departure time `dep[source]= time++`
```python
time = 0 #new
# arr, dep are arrays recording arrival and departuring time of each node initialize with -1
def dfs(source):
  visited[source]= 1
  arr[source] = time++
  for each vertex in adj[source]:
    if(visited == -1):
      dfs(vertex)
  dep[source] = time++

```


### Degree of Vertex
* Is a number of vertices that are adjacent to the vertex
* A complete graph is a graph that all edges are connected 
* G(V,E) . V is vertex and E is Edge.
* The sum of Vertex degrees is 2E
* Directed Graph has Out-degree and In-degree 

#### Eulerian (Visit All Edges Once)

* Passing all edges exactly once and back to same place -> Euler Cycle
* Passing all edges exactly once and end to another vertice -> Euler Graph 
* To have Euler Cycle there should not be any odd degree vertices all should be even degree 
* If there are exactly two odd degree vertices, and start from one of the odds and end to another it is Euler Path
*  If there is one or more odd degree vertices, then there is no Euler Cycle nor Euler path

* A Hamiltonian graph is a connected graph that contains a Hamiltonian cycle, which is a cycle that passes through every vertex exactly once

* An Eulerian graph is a connected graph that contains an Eulerian cycle, which is a path that passes through every edge exactly once and ends at the starting vertex.

* The main difference between Hamiltonian and Eulerian graphs is that a Hamiltonian graph focuses on visiting each vertex exactly once, while an Eulerian graph focuses on visiting each edge exactly once. Additionally, a Hamiltonian cycle must visit each vertex exactly once and end at the starting vertex, while an Eulerian cycle must visit each edge exactly once and end at the starting vertex

## 1 - Edge List
```
Edge1 -> 1,2
Edge2 -> 3,2
Edge3 -> 1,3   
```
* If you have 4 balls and wants to make pairs of them you can have chose 2 of n as nC2 = n(n-1)/2 where n is 4
* If you have n vertices, number of edges are nC2 or O(n^2)
* A graph with n nodes, with no self loops maximum number of edge are n(n-1)/2
* Put an array list of vertices, put another array list of objects, each object is an edge including their vertices or vertices ids from another list, weight. 

### Traverse 
* Start from one vertice, find edges connected, and go to another vertice 
* Give me list of all neighbors of one vertice,  so traverse the edge list, check each node.
```javascript
Time-> E * n  where E is number of edges and n number of vertices
Max E = n(n-1)/2 
-> Tim O(n^3)

Space 
n space for vertices, edge m --> O(n+m) 
```
## 2 - Adjacency List
* you can put id of each vertice into a list, then on each vertice add the adjacent edges
```javascript
0 -> 1,4,8
1 -> 0,4,6,9
2 -> 3   
```
* If they are not directional, there would be u and v into v and u vertices adjacents list. but if it is directional, then only from u to v then only in u are the list 
```
O(n) -> of array , O(m) -> spaces O(m+n)
```
* Also there would be cases when you look at hashtable of vertices, they point to an object which one of their attribute is adjacent vertices, the rest are other infos
```
0 -> {edgesofCities:1,4,8, edgesofRailroads:3,2,5 }
1 -> {edges:0,4,6,9
2 -> {edges:3   
```

### 3 - Adjacency Matrix
* Another way to store edges is a n*n matrix
* If it is undirected graph, then it should symmetric 
* Add wieght on each eadge, for example put 50 on arr[2][0] = 50
* Advantage is accessing to an edge is O(1)
#### Travers
* To find what are the adjacent to this vertice, need to check the index of the vertice and each one is 1 means in that vertice there is connection and 0 means no connection
* So time complexity on each node is O(n), 
* Space complexity is O(n^2), it doesn't matter how many edges have it is always fix
* So it is good when we have `dense` graph. (means has many edges)
* If number of edges are `sparse` it means number of edges are way more smaller. 
  * Like facebook has more than 2 billion people, average is afew hundereds, so matrix doesn't make sense since total among of storage is 2 billion * 2 billion 
  * Since most graph are `spares` so it is good to use `adjacent list`
  * To quickly tell `spares` tell in O(1) if u is connected to v
```python
import numpy
numpy.zeros((5, 5))
numpy.empty((5, 5))                      # allocate, but don't initialize
numpy.ones((5, 5))
```
### 4 - Adjacency Maps

```javascript
u -> {v:e, w:g}
v -> {u:e, w:f}
```
* It takes O(1) to find out what is adjacent of a vertice to get edge wieght
* 
* A list of array or hash table instead of pointing to list of nodes (adjacent list), it points to object of keys and pairs, where key are vertices and values are edges between that key and the first vertice in index. So if there is weight this edge could be weight 
* Adjacency matrics provides O(1) time, Adjacency map combines the advantage of Adjacency lists(in space) and Adjacency matrics (in time)
* Usually Adjancy map is suggested 
* Adjacency matrixs and map have O(1) access time in query "Is vertex i directly connected to verex j"
* Adjacency list and map have O(degree(i)) in time on "Get all neighbors of vertex i"
* Spaces is O(m+n), where m is number of edges and n vertices on all  3 list expect matrix which is n^2
* If we have 10 vertices and 20 edges and memory is expensive what you select in between two list and martix
  * In general -> Adjacency list 
  * If there is no auxillary data -> Adjacency Matrix


### Python 
* Initial an array with empty array or any object
```python
adjacency_list = [[] for _ in range(n)]
```

### Two dimension graph
* A two dimension array is give as a graph find if there is a loop
* make adjacent hashtable
* recursively check each node neighbours, if reached to that node then it is loop otherwise no
```javascript

```