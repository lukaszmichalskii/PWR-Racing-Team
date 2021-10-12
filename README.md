# PWR Racing Team - task


## Description

The task of this project was to implement solution to PWR Racing Team task.

## Instructions
The robot moves between 4 hangars (A, B, C, D) on 3 types 
of roads (red, green, and blue). 
A toll must be paid for driving on each type of road 
(the toll cannot be negative). Roads and hangars map:

![map](https://user-images.githubusercontent.com/76202883/137000402-98fe610d-8713-4b85-8179-1dc76e7065bd.png)

Write a program in Python that you enter accepts:
- The price of travel on the red road, green road, blue road
- The number of hangars visited
- List of hangars visited

Then the program is to provide the price of the trip (the sum of all journeys between the hangars in
the order was given in the input).

## Solution 
The problem can be solved using the graph. 
The picture below represents the structure of the graph 
adopted in the solution.

![graph](https://user-images.githubusercontent.com/76202883/137000220-8c2affce-9c52-40be-b382-5fe55211c613.png)

The easiest and most intuitive way is to find the cheapest path (shortest) 
on the desired path. Since each path element can be stored in an array or list, 
we can indicate the next destination and calculate the cost of travel from the current hangar to the desired hangar. 
Then we need to update our total cost by the cost of "sub travel"

### Finding the cheapest path between two nodes/vertices
To calculate the cheapest cost of travel from hangar A to B, we can use Dijkstra's algorithm
of finding the shortest path in undirected, connected, weighted graphs.
For more information see:
- [Dijkstra's algorithm](https://en.wikipedia.org/wiki/Boids)
- [Dijkstra's Shortest Path Algorithm](https://brilliant.org/wiki/dijkstras-short-path-finder/)

Algorithm time complexity is O(|E| + |V|log|V|) and in our program in the worst-case we need to make N calculations where
N is the length of a given path.

***Total time complexity: O(N * (|E| + |V|log|V|))***

### Optimizations
We could store the counted paths in memory because the plot is undirected,
hence the shortest path from A -> B is equal to the shortest path from
B -> A, so we would not have to count this value again.


### Additional information
The program has built-in simple error handling methods 
that will need to be optimized or corrected in the future

## Requirements
- pip~=21.1.2
- wheel~=0.36.2
- networkx~=2.6.3
- setuptools~=57.0.0

