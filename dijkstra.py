
# Interroblank, 2019

import re
from heapq import heappush, heappop, heapify

def dijkstra(file):

    # Converting the file into a string value.
    fileOpen = open(file, 'r')
    graph = fileOpen.read()
    fileOpen.close()

    # Slicing off the size value and creating a string value of edges.
    size = int(graph[0:3])
    graph = graph[3:len(graph)]
    graph = graph.split('\n')

    # Initializing vertex list.
    vertices = list()
    for i in range(size):
        vertices.append(vertConvert(i))

    # Initializing edge list.
    edges = list()
    for e in graph:
        tempList = e.split()
        if len(tempList) > 0:
            tempTuple = (tempList[0], tempList[1], int(tempList[2]))
            edges.append(tempTuple)

    # Initializing 'dist' dictionary.
    dist = {}
    for i in range(size):
        dist[vertConvert(i)] = float('inf')
    dist['A'] = 0

    # Initializing 'prev' dictionary.
    prev = {}
    for i in range(size):
        prev[vertConvert(i)] = None

    # Initializing minimum binary heap.
    heap = []
    for v in dist:
        tempTuple = (dist[v], v)
        heappush(heap, tempTuple)
    heapify(heap)

    # Executing Dijkstra's algorithm.
    while len(heap) != 0:
        currentVert = heappop(heap)
        newHeap = list()
        edgeHolder = None
        for e in edges:
            if e[0] == currentVert[1]:
                if dist[e[1]] > (dist[currentVert[1]] + e[2]):
                    dist[e[1]] = dist[currentVert[1]] + e[2]
                    prev[e[1]] = currentVert[1]
                    edgeHolder = e[1]
                    newHeap.append((dist[currentVert[1]] + e[2], e[1]))
                    heapify(heap)
        for v in heap:
            if v[1] != edgeHolder:
                newHeap.append(v)
        heap = newHeap
        heapify(heap)

    # Printing the weight of the shortest path from vertex 'A' to  vertex 'B'.
    print(dist['B'])

    # Building the shortest path from vertex 'A' to  vertex 'B'.
    current = 'B'
    path = 'B'
    while current != 'A':
        for v in prev:
            if v == current:
                path = prev[v] + ' ' + path
                current = prev[v]

    # Printing the shortest path from vertex 'A' to  vertex 'B'.
    print(path)

def vertConvert(vert):
    # Utility function for converting between capital letters and numbers.
    if type(vert) == str:
        return ord(vert) - 65
    elif type(vert) == int:
        return str(chr(vert + 65))
    else:
        return None
