from collections import defaultdict

class Graph:
    def __init__(self,vertices):
        self.map = {} # adjacency list
        self.vertices= vertices # count of vertices 
        for index in range(vertices):
            # initialise map with empty list
            self.map[index] = []     
            
    # Function to add an edge to graph 
    def addEdge(self, u, v):
         #Add w to v list  DIRECTED GRAPH 
        self.map[u].append(v)

        
    def dfs(self, currentNode, visited, result) :
        visited[currentNode] = True 

        for i in self.map[currentNode] :
            if visited[i] == False :
                self.dfs(i, visited, result)
  
        result.insert(0, currentNode)

      # The function to do Topological Sort. It uses recursive  
    # topoSortvisit()
    def topologicalSort(self) :
        visited = [False] * self.vertices
        result = []

        for currentNode in range(self.vertices) :
            if visited[currentNode] == False :
                self.dfs(currentNode, visited, result)

        return(result)
        
g = Graph(5)
g.addEdge(0, 1)
g.addEdge(0, 3)
g.addEdge(1, 2)
g.addEdge(2, 3)
g.addEdge(2, 4)
g.addEdge(3, 4)


print(g.topologicalSort())