#graphalgs.py
#By: Sam Schmitz
#Uses the Graph class to implement the k-clique problem

from graph import *

def has_clique(g, k):   #check if a graph has a clique of size k in an undirected graph
    for i in g.vertex_iter():   #start looking at each vertex
        if _has_clique_sub(g, int(k), [], i):    #start the sub function to look for clique
            return True
        return False

def _has_clique_sub(g, count, chain, vc):
    #count = k - # of vertices in the chain
    #chain = chain of vertices
    #vc = vertex current
    chain.append(vc) #add current vertex to the chain
    count = count - 1 #down tick the count
    adj = g.adjacent(vc)    #get the list of adjacent vertices
    #print(vc, chain, adj, count)
    if count == 0:  #if the desired size of clique is reached
        for i in adj:   #search through the adjacent vertices
            if i == chain[0]:   #check if the starting vertex is adjacent
                return True
        return False    #if starting vertex is not adjacent not a clique
    else:   #continue to extend the length of the clique
        for i in adj:   #search throught the adjacent vertices
            if i not in chain:  #make sure that the vertex isn't in the current chain
                if _has_clique_sub(g, count, chain, i): #if clique found in recurse return true
                    return True
        return False    #clique does not go through here

def main():
    print("This program calculates if the graph contains a clique of size k")
    #print("Enter k: ", end="")
    #k = input()
    print("looking for clique of size 3")
    k = 3
    g = Graph(["a", "b","c" ,"d" ,"e"])
    g.add_edge("a", "b")
    g.add_edge("b", "c")
    g.add_edge("a", "c")
    if has_clique(g, k):
        print("The graph contains a clique of size", k)
    else:
        print("The graph doesn't contain a clique of size", k)

main()
