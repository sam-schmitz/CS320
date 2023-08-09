#graph.py
#By: Sam Schmitz
#a Graph class that implements and tests variuos graph algorithms

class Graph:
    def __init__(self, vertices, directed=False):
        self.vs = vertices  #create a list of the veritices
        self.directed = directed    #mark directed vs underected
        self.edges = {} #create an empty list of the edges
        for i in self.vs:
            self.edges[i] = {}

    def add_edge(self, v1, v2, weight=1):   #add an edge to the graph
        self.edges[v1][v2] = weight    #dict w/in dict that cooresponds weight to v2
        if self.directed == False:
            self.edges[v2][v1] = weight #if undirected need to make an edge for v2 as well

    def has_edge(self, v1, v2): #returns a Boolean indecating v1 is adjacent to v2
        if self.edges[v1].has_key(v2):  #check for key v2 within the dict assoc w/ v1
            return True
        return False

    def weight(self, v1, v2):   #returns the weight of edge from v1 to v2
        return self.edges[v1][v2]

    def vertex_iter(self):  #returns an iterator for vertices
        for i in self.vs:
            yield i
        #yield (i for i in self.vs)    #yields the vertices in the order they were given in

    def edge_iter(self):    #returns an iterator for edges
        for i in self.edges:
            yield i
        #yield (i for i in self.edges)    #use yeild/generator

    def adjacent(self, v):  #returns adjacency list for v as a dictionary
        a = []
        for key in self.edges[v]:
            a.append(key)
        return a

def fromfile(filename): #returns a graph from a given file
    f = open(filename, "rt") #open the file
    directed = False
    direct = f.readline().split()
    if direct[0] == "directed":    #if directed change variable
        directed = True
    vertices = f.readline().split()
    g = Graph(vertices, directed)   #create the graph
    while True: #read the edges line by line
        edge = f.readline().split() #grab the next line and split it into a list
        if len(edge) == 0:  #if the list is empty there is no more edges break loop
            break
        if len(edge) == 2:  #unweighted edges
            g.add_edge(edge[0], edge[1])
        else:   #weighted edges
            g.add_edge(edge[0], edge[1], edge[2])
    f.close()   #close the file
    return g
