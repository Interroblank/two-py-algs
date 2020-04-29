
# Interroblank, 2019

import sys
import math

def closestPair(file):
    
    # Converting the file into a list of string values.
    fileOpen = open(file, 'r')
    points = fileOpen.read()
    fileOpen.close()
    points = points.split('\n')

    # Converting the list of strings into a list of integer tuples.
    pointList = list()
    for p in points:
        tempList = p.split()
        if len(tempList) > 0:
            tempTuple = (int(tempList[0]), int(tempList[1]))
            pointList.append(tempTuple)

    # Recursively determining the closest pair of points in the list.
    return closestPairH(pointList)

def closestPairH(points):

    # Base case for list of size three or less.
    if len(points) <= 3:
        return minDist(points)

    # Sorting the list by the x-coordinate of each point.
    points = sortX(points)

    # Determining the midpoint and endpoint of the sorted list of points.
    pointsMid = points[len(points) // 2]
    pointsMidIndex = len(points) // 2
    pointsEndIndex = len(points) - 1

    # Recursively determining the closest pair of points on the left and right.
    minL = closestPairH(points[0:pointsMidIndex])
    minR = closestPairH(points[pointsMidIndex:pointsEndIndex])

    # Determining the smaller of the two values.
    minLR = 0
    if minL < minR:
        minLR = minL
    elif minR < minL:
        minLR = minR
    else:
        minLR = minL

    # Assembling the 'strip'.
    strip = list()
    for p in points:
        if abs(regDist(p, pointsMid)) < minLR:
            strip.append(p)

    # Sorting the strip by the y-coordinate of each point.
    strip = sortY(strip)

    # Traversing the 'strip' and determining its minimum distance.
    stripMin = sys.maxsize
    for i in strip:
        for j in strip:
            if (j[1] - i[1]) < minLR and i != j:
                if regDist(i, j) < stripMin:
                    stripMin = regDist(i, j)

    # Determining and returning the true minimum distance.
    if stripMin < minLR:
        return stripMin
    else:
        return minLR

def regDist(p1, p2):
    # Calculating the distance between two points.
    return math.sqrt(math.pow((p1[0] - p2[0]), 2) +
                     math.pow((p1[1] - p2[1]), 2))

def minDist(points):
    # Calculating the closest pair of points in a list of points.
    # This is a brute force utility algorithm for the base case.
    minimum = sys.maxsize
    for i in points:
        for j in points:
            if regDist(i, j) < minimum and i != j:
                minimum = regDist(i, j)
    return minimum 

def sortX(points):
    # Sorting the list by the first value in each tuple.
    # 'Timsort', Python's sorting algorithm, runs in linearithmic time.
    pointsX = points
    pointsX.sort(key = lambda val: val[0])
    return pointsX
    
def sortY(points):
    # Sorting the list by the second value in each tuple.
    # 'Timsort', Python's sorting algorithm, runs in linearithmic time.
    pointsY = points
    pointsY.sort(key = lambda val: val[1])
    return pointsY
