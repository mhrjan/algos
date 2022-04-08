class Graph:
    def __init__(self,vertices):
        self.map = {}
        self.vertices = vertices
        for index in range(vertices):
            self.map[index] = []
    
    def addEdge(self,u,v):
        self.map[u].append(v)
        self.map[v].append(u)
    
    def print_graph(self):
        for index in range(self.vertices):
            print(index,"->",self.map[index])

g = Graph(6)
g.addEdge(0,1)
g.addEdge(2,1)
g.addEdge(1,3)
g.print_graph()