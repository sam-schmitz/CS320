#topsort.py
#By: Sam Schmitz
#topological sort algorithm

from graph import *

def topsort(g): #returns a list of vertex labels of a grpah in topsort order/returns none if topsort is impossible
    chain = []  #a list of vertices that have already been acsessed/popping off order
    for i in g.vertex_iter():   #go through all vertices
        if i not in chain:  #check that they are not already in the list
            chain.append(_sub_topsort(g, chain, i)) #run the recureive function
            chain.pop()
    #print(chain)
    chain.reverse()
    return chain  #return the reversed chain

def _sub_topsort(g, chain, v): #helper function for topsort()
    #print(v)
    adj = g.adjacent(v) #grab the adjacent vertices
    for i in adj:   #go through all adjacent vertices not already in the chain
        if i not in chain:
            chain.append(_sub_topsort(g, chain, i)) #run the recursion
            chain.pop()
            #print(chain, "b")
    chain.append(v) #add current vertex to the chain
    #print(chain, "c")
    return chain    #return the chain

def main():
    g = fromfile('graphD.txt')
    print(topsort(g))

main()
