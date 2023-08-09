#subsets.py
#By: Sam Schmitz
#finds all subsets in a list of items

def subsets_bu(lst):    #the bottom-up version of the reecursive subsets
    set = [[]]
    for i in lst:   #repeat for each item in the given list
        sub = []    #create a list for new subset parts
        for j in set:   #for each item in set
            sub.append(j + [i]) #combine the current item in set with i for a new subset
        set = set + sub #add the new subsets to the list
    return set


def subsets_td(lst):    #the top-down version of the recursive
    if len(lst) == 0:   #if the list is empty return nothing
        return [[]]
    c = lst.pop()   #the element to add on this recurse
    set = subsets_td(lst)  #get the list of subsets before this element
    nSet = []   #the things you will add to the list of subsets
    for i in set:  #for each element in subs add the new version to adds
        sub = []
        for j in i: #add each element from set[i] to sub
            sub.append(j)
        sub.append(c) #add c to the sub(copy of set[i])
        nSet.append(sub)  #add the new sub to the new sets
    #print(c, set, nSet)
    subset = set + nSet #combine the old set and the new one
    #print(c, subset)
    return subset

def main():
    print(subsets_bu([1, 2, 3]))
    print(subsets_td([1, 2, 3]))

main()
