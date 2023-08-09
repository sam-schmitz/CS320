#quickHull.py
#By: Sam Schmitz w/ help from Brice Rhodes
#An implementation of the quick hull algortithm
#this program requires the installation of matplotlib if this is not installed open a
#comand prompt and enter in C:\Users\Your Name>pip install matplotlib
#numPy also needs to be installed. Can be installed with C:\USers\Your Name>pip install numpy
#numPy should be installed if matplotlib is also installed

import random
import matplotlib.pyplot as plt
import numpy as np

def quickHull(points):
    #input: A list of ordered pairs representing points
    #output: A list of segments(pairs of points), that describe the convex hull polygon
    #find p1 and pn
    indices = range(len(points))
    p1Index = min(indices, key=points.__getitem__)
    pnIndex = max(indices, key=points.__getitem__)

    #split the points above to s1 and below to s2
    s1, s2 = [], []
    dets1, dets2 = [], []
    p1 = points[p1Index]
    pn = points[pnIndex]
    for i in range(len(points)):
        if i is not p1Index and i is not pnIndex:
            if determ(p1, pn, points[i]) >= 0:
                s1.append(points[i])
                dets1.append(determ(p1, pn, points[i]))
            else:
                s2.append(points[i])
                dets2.append(-determ(p1, pn, points[i]))
    #constuct the 2 halfhulls and merge them
    return halfHull(p1, pn, s1, dets1) + halfHull(pn, p1, s2, dets2)

def halfHull(p1, pn, s, determs):    #finds a hull between a line and a set of points
    #s is a set of points left of p1pn (make sure that s does not include p1 and pn)
    if not s:  #base case for empty list
        return [(p1, pn)]
    #find pmax
    indices = range(len(determs))
    pmax = s[max(indices, key=determs.__getitem__)]
    s1, s2 = [], []
    s1Determs, s2Determs = [], []
    for i in s:
        if determ(p1, pmax, i) > 0:
            s1.append(i)
            s1Determs.append(determ(p1, pmax, i))
        if determ(pmax, pn, i) > 0:
            s2.append(i)
            s2Determs.append(determ(pmax, pn, i))
    #s2 = all points in s left of pmaxpn
    return halfHull(p1, pmax, s1, s1Determs) + halfHull(pmax, pn, s2, s2Determs)

def determ(p1, p2, p3): #returns positive when p3 is left, negetive when p3 is right
    return (p1[0]*p2[1] + p3[0]*p1[1] + p2[0]*p3[1] - p3[0]*p2[1] - p2[0]*p1[1] - p1[0]*p3[1])

def doGraphing(points, hull):   #plot the results in a graph
    xpoints, ypoints = [], []
    for i in points:    #plot the points
        xpoints.append(i[0])
        ypoints.append(i[1])
    plt.plot(xpoints, ypoints, 'o')
    #plot the hull
    xpHull, ypHull = [hull[0][0][0]], [hull[0][0][1]]
    for i in hull:
        xpHull.append(i[1][0])
        ypHull.append(i[1][1])
    plt.plot(xpHull, ypHull)
    plt.xlabel("x - axis")
    plt.ylabel("y - axis")
    plt.title("Convex Hull")
    plt.show()    #show the graph

if __name__ == "__main__": #a driver program that demonstrates quickHull()
    print("This program implements the quickhull algorithm")
    print("Please enter the number of points: ", end="")
    n = int(input())  #n = number of points
    points = []
    for i in range(n):  #generate a random set of n points(n=user input)
        pair = random.randrange(0, 100+n), random.randrange(0, 100+n)
        points.append(pair)
    hull = quickHull(points)    #compute the convex hull
    doGraphing(points, hull)    #show the results graphically by ploting them
