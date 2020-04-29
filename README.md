# two-py-algs
Simple and clean Python implementations of two essential algorithms (Closest Pair of Points and Dijkstra's).
## Closest Pair of Points (cpp.py):
Accepts a plain text file in the following format:
```
3646 2874
354 54
243 6574
-44 452
52 426
534 8243
1324 3542
1443 645
243 6847
1010 -9475
274 371
183 495
293 495
2019 4753
4816 3425
```
Where each value is a set of Cartesian coordinates for each point.

Will print the distance between the closest pair of points.
## Dijkstra's (dijkstra.py):
Accepts a plain text file in the following format:
```
10
A G 10
G D 5
D C 11
D E 7
E C 76
E B 6
G F 51
F D 3
F B 19
C H 12
E I 42
B J 10
```
Where the first value is a double-digit integer indicating number of vertices, and the following values are directed edges and their respective weights. For example:
```
A G 10
```
Represents a directed edge from vertex 'A' to vertex 'G' of weight 10. All vertices must be denoted by a capital English letter. Note that if the number of vertices is less than ten, the first number in the text file must still be at least ten.

Will print the shortest path from vertex 'A' to vertex 'B' and the total weight of said path.
