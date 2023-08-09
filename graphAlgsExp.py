#graphAlgsExp.py
#By: Sam Schmitz
#More graph algorithms

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

def dfs(g):
    chain = []
    for i in g.vertex_iter():   #iterate through each vertex not already in the chain
        if i not in chain:
            chain.append(_dfs(g, chain, i)) #call the sub function and load it with the current chain, and an unsued vertex
            chain.pop() #trim the chain
        return chain

def _dfs(g, chain, v):
    chain.append(v) #add the current vertex to the chain
    adj = g.adjacent(v)
    #print(v, adj)
    for i in adj:   #search through the adjacent vertices
        #print(chain, i)
        if i not in chain:  #weed out the ones already in the chain
            #print(chain, i)
            chain.append(_dfs(g, chain, i)) #recurse
            chain.pop() #trim the chain
    return chain

def bfs(g):
    chain = []  #create a list of vertices that have been searched
    for i in g.vertex_iter():   #iterate through the vertices
        if i not in chain:  #don't include those that have not already been searched
            chain.append(i) #add that vertex to the chain
            chain.append(_bfs(g, chain, i)) #load the sub algorithm with the current chain and a new vertex
            chain.pop() #trim the chain
    return chain

def _bfs(g, chain, v):  #the helper function for the breadth first search
    adj = g.adjacent(v) #get the adjacent vertices
    #print(v, adj, chain)
    ogChain = chain #copy the original chain
    for i in adj:   #check each adjacent vertex to be in the OG chain
        if i not in ogChain:
            chain.append(i) #add that vertex to the new chain
    for i in adj:   #iterate again
        if i not in ogChain:
            chain.append(_bfs(g, chain, i)) #recurse
    return chain

def main():
    g = fromfile('graph1.txt')
    print(dfs(g))
    print(bfs(g))

main()
