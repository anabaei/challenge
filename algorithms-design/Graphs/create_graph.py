# create Edge list graph 

class Graph():
    def __init__(self, size):
        self.edges = [[] for _ in range(size)]
``
    def addEdge(self, start, end, isUndirect):
        self.edges[start].append(end)
        if(isUndirect):
            self.edges[end].append(start)
    
    def printList(self):``
        print(self.edges)


graph = Graph(4)
graph.addEdge(0,1,False)
graph.printList()

