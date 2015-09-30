
import random
import math
import collections
import time
from enum import Enum
#import pdb; pdb.set_trace()

#some global variables, global for convenience

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
            'o','p','q','r','s','t','u','v','w','x','y','z']

#list of graphs generated pseudo-randomly
graphList = [] 
#used to keep track of nearest neighbours of a node when determining adjacency
neighbourList = [] 

#list of vertices discovered (traversed) in DFS
discoveredList = []
exploredList = []
SLDlist =[]
#the following x,y are used to get coords of goal city (z)
xGoal = -1
yGoal = -1

exploredCount = []

foundList = []

nodesTraversed = 0

#determines the distance between city1(x1,y1) and city2(x2,y2)
def euclidDist(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2 +(y1-y2)**2)

#graph generating functions
#none of this is done efficiently at the moment 
#return nearest five cities by euclidean distance
def getFiveNearest(grid, lst, i ,j):
    nearestFive = []
    for city in lst:
        for y in range(100):
            for x in range(100):
                if(grid[x][y] == city):
                    dist = euclidDist(i,j,x,y)
                    nearestFive.append((city, dist))
    nearestFive.sort(key = lambda x : x[1])
   # print(nearestFive[:5])
   
    return nearestFive[:5]
                      
def findNeighbours(grid, c, i, j, lst, depth):
    leftCol = i -depth
    if leftCol < 0:
        leftCol = 0
    rightCol = i + depth
    if rightCol > 100:
        rightCol = 100
    top = j - depth
    if top < 0:
        top = 0
    bottom = j + depth
    if bottom > 100:
        bottom = 100
    for n in range(top, bottom):
        for m in range(leftCol, rightCol):
            if(grid[m][n] != '0' and (grid[m][n] != c) and ((grid[m][n])) not in lst):
                lst.append(grid[m][n])
                
    if(len(lst) >= 5):
        return getFiveNearest(grid, lst, i, j)
    else:
         return findNeighbours(grid, c, i, j, lst, depth+1)

#pick 3 of the five cities on the list to be adjacent to current city
def populateAdjMatrix(city, lst, adjMatrix, graph):
    #city = grid[i][j]
    del lst[random.randrange(len(lst))]
    del lst[random.randrange(len(lst))]
    #get city adjacency row
    row = alphabet.index(city)
    adjacencies = 0    
    for x in lst:

        for s in range(26):   #we add adjacencies until the node is connected to three others
            if adjMatrix[s][row] == 1:
                adjacencies += 1         
        
        neighbourAdjacencies = 0

        for t in range(26):
            if adjMatrix[t][alphabet.index(x[0])] == 1:
                neighbourAdjacencies += 1
                
        if adjacencies <= 3 and neighbourAdjacencies <3:
            adjMatrix[alphabet.index(x[0])][row] = 1
            adjMatrix[row][alphabet.index(x[0])] = 1
            
            graph[city].append(x)
            graph[x[0]].append([city, x[1]])

#make list of SLD from all cities to goal, sld to z is last element in every
#entry of the graph dictionary
def makeSLDlist(graph, grid):
    global xGoal
    global yGoal
    foundGoal = False
    lst =[]
    for j in range(100):
        for i in range(100):
            if grid[i][j] in alphabet:
                lst.append((grid[i][j], euclidDist(i,j,xGoal,yGoal)))
                #graph[grid[i][j]].append(euclidDist(i,j,xGoal,yGoal))
               #print(graph[grid[i][j]][0][0])
    sorted(lst, key=lambda x: x[0])
    SLDlist.append(lst)

                
def makeGraph():
    grid = [['0' for i in range(100)] for j in range(100)]

    graph = dict()
    graph = { 'a' : [],'b': [],'c': [],'d': [],'e': [],'f': [],
          'g': [],'h': [],'i': [],'j': [],'k': [],'l': [],
          'm': [],'n': [], 'o': [],'p': [],'q': [],'r': [],
          's': [],'t': [],'u': [],'v': [],'w': [],'x': [],'y': [],'z': [] }
    adjMatrix = [[0 for i in range(len(alphabet))]for j in range(len(alphabet))]

    #initialize grid
    for j in range(0,100):
        for i in range(0,100):
            grid[i][j] = '0'

    for i in alphabet:
        placed = False
        while(placed == False):
            x = random.randrange(100)
            y = random.randrange(100)
            if(grid[x][y] == '0'):
                grid[x][y] = i
                if(i == 'z'):
                    global xGoal
                    global yGoal
                    xGoal = x
                    yGoal = y
                placed = True
 #uncomment to print the grid of letters (not quite to scale)

#cities placed in grid. Now determine adjacencies
    
    for j in range(0,100):
        for i in range(0,100):
           if(grid[i][j] != '0'):
                neighbourList = []
            #    print(grid[i][j])
                neighbourList = findNeighbours(grid,grid[i][j], i, j, neighbourList, 1)
           #     print(neighbourList)
                populateAdjMatrix(grid[i][j], neighbourList, adjMatrix, graph)

    
    for j in range(26):
        for i in range(26):
            if adjMatrix[i][j] == 1 and adjMatrix[j][i] ==0:
                adjMatrix[j][i] = 1

    makeSLDlist(graph, grid)
    sorted(graph.items(), key=lambda x: x[0]) 
    graphList.append(graph)  

'''
# print not to scale layout of cities
    for j in range(100):
        row  = ""
        for i in range(100):
            if grid[i][j] != '0':
                row += grid[i][j]
            else:
                row += ' '
        print(row)
'''
#print an adjacency matrix
'''
print ('   abcdefghijklmnopqrstuvwxyz')
for j in range(26):
    row = alphabet[j]
    row += ': '
    for i in range(26):
        row += str(adjMatrix[i][j])
#    print(row)
'''
'''
for x in graph:
    print(x, graph[x])
'''

#adapted from pseudocode from breadth-first search wikipedia entry
def breadthFirstSearch(G, v, goal):
    global nodesTraversed
    discoveredList.append(v) #discovered list is the frontier here

    while(len(discoveredList) > 0):
        u = discoveredList.pop(0)
        exploredList.append(u)
        nodesTraversed += 1
    #    print(u)
        if u == goal:
            exploredCount.append(len(exploredList))
            print("found it")
            foundList.append(1)
            return
        
        for x in G[u]:
            if x[0] not in discoveredList and x[0] not in exploredList:
                discoveredList.append(x[0])
                exploredList.append(x[0])
                if(x[0] == goal):
                    break

#adapted from pseudocode from depth-first search wikipedia entry
def depthFirstSearch(G, v, goal):
    global nodesTraversed
    discoveredList.append(v)
    nodesTraversed += 1
    if( v == goal):
        success = "found " + goal
        print(success)
        foundList.append(1)
        return
    print(v)
       
    for x in G[v]:
        if x[0] not in discoveredList:
            depthFirstSearch(G, x[0], goal)
            

#code adapted from class text
#recursive depth limited search. return 1 for success, 2 for limit cutoff, 0 for failure
def recursiveDLS(G, v, goal, limit):
    global nodesTraversed
    nodesTraversed += 1
    print(v)
    print(limit)

    if v == goal: #found goal state
        success = "found " + goal
        print(success)
        foundList.append(1)
        output = "found with depth limit " + str(limit)
        print(output)
        foundList.append(1)
        return 1

    elif limit == 0:
        discoveredList.clear()
        return 2

    else:
        if limit > 0:
            
            for x in G[v]:
                if x[0] not in discoveredList:
                    discoveredList.append(v)
                    return recursiveDLS(G, x[0], goal, limit - 1)
                
    return 0

    
def iterativeDeepeningSearch(G,v,goal):
    for depth in range(0,100):
        discoveredList.clear()
        result = recursiveDLS(G,v,goal,depth)
        if result !=2:
            return result
        
                
#params are graph, vertex, and x,y coords of goal
def greedySearch(G,v,goal):
    global nodesTraversed
    nodesTraversed += 1
    print(v)
    exploredList.append(v)
    found = False
    if v == goal: #found goal state
        success = "found " + goal
        print(success)
        foundList.append(1)
        output = "found with depth limit " + str(limit)
        print(output)
        foundList.append(1)
        found = True
        return 1
    
    adjacencies = []
   
    for x in G[v]:
        if x[0] not in discoveredList:
            discoveredList.append(x[0])
            adjacencies.append((x[0], x[-1]))
            
    adjacencies.sort(key=lambda x: x[0])
    print(adjacencies)
    for x in adjacencies:
        if x[0] not in exploredList:
            return greedySearch(G, x[0], goal)
                
    return 0
    
def menu():
    print('\n')
    print("Top Menu")
    print("enter an option by number")
    print("1: create 100 different graphs with user input random seed")
    print("2: print a graph dictionary by index")
    print("3: depth-first-search on graph by index")
    print("4: run DFS on all graphs and output stats")
    print("5: run BFS on graph by index")
    print("6: run BFS on on all graphs and output stats")
    print("7: run recursiveDLS on graph by index")
    print("8: run IDFS on all graphs and output stats")
    print("9: perform greedy search on graph by index")
    option = input("what next?")

    if option == '1':
      #  graphList = []
        seed = input("input random seed")
        random.seed(int(seed))
        print("making 100 graphs from seed")
        for x in range(8):  #will be 100, but not spending the time on that now
            makeGraph()
                
        menu()

    if option == '2':
        index = input("enter an index (integer)")
        graph = graphList[int(index)]

        for x in alphabet: #this way we get it in alpha order instead of
            print(x, graph[x])#dictionary key order. Much more readable
        print(SLDlist[int(index)])
            
        menu()

    if option == '3':
        discoveredList.clear()
        index = input("enter an index (integer)")
        depthFirstSearch(graphList[int(index)], 'a', 'z')

        menu()

    if option == '4':
        totalTime = 0
        global nodesTraversed
        nodesTraversed = 0
        foundList.clear()
        averageNodesVisited = 0
        for x in graphList:
            discoveredList.clear()
            t0 = time.time()
            foundList.append(depthFirstSearch(x, 'a','z'))
            totalTime += time.time() - t0
            averageNodesVisited += len(discoveredList)
        
        foundCount = 0

        for x in foundList:
            if x == 1:
                foundCount +=1
                
        output = "found the goal " + str(foundCount) + "of " + str(len(graphList)) + "times"
        print(output)
        output = "Total time to run DFS on all graphs: " + str(totalTime)
        print(output)
        output = "average nodes visited (time complexity) was " + str(nodesTraversed / len(graphList))
        print(output)
        output = "average space complexity (list of visted nodes) was " + str(averageNodesVisited /len(graphList))
        print(output)
        menu()

    if option == '5':
        discoveredList.clear()
        index = input("enter an index (integer)")
        breadthFirstSearch(graphList[int(index)], 'a', 'z')
        menu()

    if option == '6':
        totalTime = 0
        global nodesTraversed
        nodesTraversed = 0
        averageNodesVisited = 0
        exploredCount.clear()
        foundList.clear()
        
        for x in graphList:
            print('\n')
            discoveredList.clear()
            exploredList.clear()
            t0 = time.time()
            breadthFirstSearch(x, 'a','z')
            totalTime += time.time() - t0
            averageNodesVisited += len(exploredList)
        foundCount = 0
        
        for x in foundList:
            if x == 1:
                foundCount +=1
        output = "found the goal " + str(foundCount) + "of " + str(len(graphList)) + "times"
        print(output)
        averageNodesVisited
        output = "total time to run BFS on all graphs: " + str(totalTime)
        print(output)
        output = "average nodes visited (time complexity) was " + str(nodesTraversed / len(graphList))
        print(output)
        output = "average space complexity (list of visted nodes) was " + str(averageNodesVisited / len(graphList))
        print(output)
        menu()

    if option == '7':
        discoveredList.clear()
        index = input("enter an index (integer)")
        print(str(iterativeDeepeningSearch(graphList[int(index)], 'a', 'z')))
        menu()

    if option == '8':
        totalTime = 0
        global nodesTraversed
        nodesTraversed = 0
        averageNodesVisited = 0
        exploredCount.clear()
        foundList.clear()
        
        for x in graphList:
            print('\n')
            discoveredList.clear()
            t0 = time.time()
            iterativeDeepeningSearch(x, 'a','z')
            totalTime += time.time() - t0
            averageNodesVisited += len(discoveredList)
        foundCount = 0
        
        for x in foundList:
            if x == 1:
                foundCount +=1
        output = "found the goal " + str(foundCount) + "of " + str(len(graphList)) + "times"
        print(output)
        nodesTraversed /= len(graphList)
        output = "total time to run IDFS on all graphs: " + str(totalTime)
        print(output)
        output = "average nodes visited (time complexity) was " + str(nodesTraversed)
        print(output)
        output = "average space complexity (list of visted nodes) was " + str(averageNodesVisited / len(graphList))
        print(output)
        menu()

    if option == '9':
        exploredList.clear()
        discoveredList.clear()
        index = input("enter an index (integer)")
        greedySearch(graphList[int(index)], 'a', 'z')
        menu()
       
            
menu()


        
    
    

      
