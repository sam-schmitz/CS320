This is a collection of the work I did in CS320. An important aspect of the class was sorting algorithms. We learned several aproaches to sorting including arrays, trees and hashing. Another topic was graphs 

Course Description: Introduction to intermediate data structures and deepening understanding of elementary data structures introduced in CS220. Graph representations, balanced trees, multi-lists, hash tables, files. Relationship between data structures and run-time and space efficiency.

Projects: 

seive.py:
	An implementation of the Sieve Algorithm
	Seive Algorithm: Based on the Sieve of Eratosthenes, which is used to find all prime numbers up to a given limit. 
	By: Sam Schmitz

compare_count_sort.py:
	An implementation of the comparison count sort from the textbook
	By: Sam Schmitz

bubble_sort.py:
	An implementation of the Bubble Sort Algorithm
	Bubble Sort: A basic comparison-based sorting algorithm that repeatedly steps through the list of elements to be sorted, compares adjacent elements, and swaps them if they are in the wrong order.
	By: Sam Schmitz

selection_sort.py:
	An implementation of the Selection Sort Algorithm
	Selection Sort: A simple comparison-based sorting algorithm that works by repeatedly selecting the minimum (or maximum) element from the unsorted portion of the array and swapping it with the first element of the remaining unsorted portion. It continues this process until the entire array is sorted.
	By: Sam Schmitz

bubble_sort_exp.py:
	A comparison between Bubble Sort and an expriemental version of it. Results are found in Bubble Sort Exp.txt
	By: Sam Schmitz

graph.py:
	The general Graph class that will be used to implement and test graph algorithms A classic mathematic graph. 
	By: Sam Schmitz

graphalgs.py:
	Uses the Graph class to implement the k-clique problem. Uses graphD.txt
	K-Clique Problem: It involves finding whether a graph contains a clique of size k or more, where a clique is a subset of vertices in a graph such that every pair of vertices in the subset is connected by an edge.
	By: Sam Schmitz

topsort.py:
	An implementation of the source removal algorithm for topological sort
	Toplological Sort: An ordering of the vertices of a directed acyclic graph (DAG) in such a way that for every directed edge (u, v), vertex u comes before vertex v in the ordering. In other words, it's a linear ordering of the vertices that respects the direction of the edges in the graph.
	By: Sam Schmitz

subsets.py:
	2 ways of finding all subsets of a list of items
	By: Sam Schmitz

insertion_sort.py:
	An implementation of the insertion sort algorithm
	Insertion Sort:  A simple and straightforward comparison-based sorting algorithm. It works by building a sorted sequence of elements, one at a time, by repeatedly inserting a new element into the correct position within the already sorted portion of the array or list.
	By: Sam Schmitz

nlogn_sorts.py:
	An implementation of the merge sort and quick sort algorithms. Results can be found in nlogn_sorts_results.txt
	Merge Sort: Uses a divide-and-conquer approach to sort an array or a list of elements. It's known for its stable performance and guaranteed time complexity of O(n log n), making it efficient for sorting large datasets.
	Quick Sort: A divide-and-conquer strategy to sort an array or a list of elements. It's known for its average-case time complexity of O(n log n).
	By: Sam Schmitz

graphAlgsExp.py:
	Uses the Graph class to implement the Depth First Search and Breadth First Search. Uses graph1.txt
	Deapth First Search: A graph traversal algorithm used to explore all the vertices and edges of a graph. It traverses as far as possible along each branch before backtracking.
	Bradth First Search:  A graph traversal algorithm used to explore all the vertices and edges of a graph in a systematic manner, starting from a specified source vertex. It  explores all the vertices at the current level before moving to the next level.
	By: Sam Schmitz

quickhull.py:
	An implementation of the quick hull algorithm.
	Quick Hull: A geometric algorithm used to compute the convex hull of a set of points in a two-dimensional or three-dimensional space.
	By: Sam Schmitz with help from Brice Rhodes

23tree.py:
	An implementation of the 2-3 Tree data structure.
	2-3 Tree: A type of self-balancing tree data structure that maintains sorted data while ensuring relatively balanced height.
	By: Sam Schmitz

pq.py:
	Contains the class PriorityQueue and the heapsort() method.
	Priority Queue: A data structure that stores a collection of elements along with their associated priorities. The main characteristic of a priority queue is that it allows efficient access to and removal of the element with the highest (or lowest) priority.
	Heapsort: A comparison-based sorting algorithm that uses the properties of a binary heap data structure to efficiently sort an array or a list of elements. It is an in-place sorting algorithm, meaning it doesn't require additional memory proportional to the size of the input data.
	By: Sam Schmitz

dp_traceback.py:
	Implements a memorized recursive version of the Knapsack Problem.
	Knapsack problem: Given a set of items, each with a weight and a value, determine the maximum value that can be obtained by selecting a subset of the items while ensuring that the total weight of the selected items does not exceed a given weight capacity (the "knapsack" constraint).
	By: Sam Schmitz (Starter code provided by John Zelle)

23treeCoord.py:
	An implementation of the Tree23 class that sorts points based on how close they are to a given point.
	By: Sam Schmitz

	