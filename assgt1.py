
import random
import math
import collections
import time
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

exploredCount = []

def setExploredCount(x):
    exploredCount = x

def getExploredCount():
    return exploredCount

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

    for n in range(100):
        for m in range(100):
            if(grid[m][n] != '0' and (grid[m][n] != c) and ((grid[m][n])) not in lst):
                lst.append(grid[m][n]) 
    
    if(len(lst) >= 10):
        return getFiveNearest(grid, lst, i, j)

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
                placed = True
 #uncomment to print the grid of letters (not quite to scale)

#cities placed in grid. Now determine adjacencies
    
    for j in range(0,100):
        for i in range(0,100):
           if(grid[i][j] != '0'):
                neighbourList = []
            #    print(grid[i][j])
                neighbourList = findNeighbours(grid,grid[i][j], i, j, neighbourList, 1)
            #    print(neighbourList)
                populateAdjMatrix(grid[i][j], neighbourList, adjMatrix, graph)

    
    for j in range(26):
        for i in range(26):
            if adjMatrix[i][j] == 1 and adjMatrix[j][i] ==0:
                adjMatrix[j][i] = 1
                
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
    discoveredList.append(v) #discovered list is the frontier here
    exploredList = []

    while(len(discoveredList) > 0):
        u = discoveredList.pop(0)
        exploredList.append(u)
    #    print(u)
        if u == goal:
            exploredCount.append(len(exploredList))
            print("found it")
            break

        for x in G[u]:
            if x[0] not in discoveredList and x[0] not in exploredList:
                discoveredList.append(x[0])
                if(x[0] == goal):
                    break

#adapted from pseudocode from depth-first search wikipedia entry
def depthFirstSearch(G, v, goal):
    discoveredList.append(v)
   
    if( goal in discoveredList):
        success = "found " + goal
        print(success)
        return
 #   print(v)
    for x in G[v]:
        if x[0] not in discoveredList:
            depthFirstSearch(G, x[0], goal)
    
def menu():
    print("Top Menu")
    print("enter an option by number")
    print("1: create 100 different graphs with user input random seed")
    print("2: print a graph dictionary by index")
    print("3: depth-first-search on graph by index")
    print("4: run DFS on all graphs and output stats")
    print("5: run BFS on graph by index")
    print("6: run BFS on on all graphs and output stats")
    option = input("what next?")

    if option == '1':
      #  graphList = []
        seed = input("input random seed")
        random.seed(int(seed))
        print("making 100 graphs from seed")
        for x in range(4):  #will be 100, but not spending the time on that now
            makeGraph()
                
        menu()

    if option == '2':
        index = input("enter an index (integer)")
        graph = graphList[int(index)]

        for x in alphabet: #this way we get it in alpha order instead of
            print(x, graph[x])#dictionary key order. Much more readable
            
        menu()

    if option == '3':
        discoveredList.clear()
        index = input("enter an index (integer)")
        depthFirstSearch(graphList[int(index)], 'a', 'z')
        menu()

    if option == '4':
        averageTime = 0
        averageNodesVisited = 0
        for x in graphList:
            print('\n')
            discoveredList.clear()
            t0 = time.time()
            depthFirstSearch(x, 'a','z')
            averageTime += time.time() - t0
            averageNodesVisited += len(discoveredList)
        averageTime /= len(graphList)
        averageNodesVisited /= len(graphList)
        output = "average time of DFS on all graphs was " + str(averageTime)
        print(output)
        output = "average nodes visited (space complexity of discovered list) was " + str(averageNodesVisited)
        print(output)
        menu()

    if option == '5':
        discoveredList.clear()
        index = input("enter an index (integer)")
        breadthFirstSearch(graphList[int(index)], 'a', 'z')
        menu()

    if option == '6':
        averageTime = 0
        averageNodesVisited = 0
        exploredCount.clear()

        for x in graphList:
            print('\n')
            discoveredList.clear()
            t0 = time.time()
            breadthFirstSearch(x, 'a','z')
            averageTime += time.time() - t0

        for x in exploredCount:
            averageNodesVisited += x

        averageNodesVisited += len(discoveredList)
        averageTime /= len(graphList)
        averageNodesVisited /= len(graphList)
        output = "average time of DFS on all graphs was " + str(averageTime)
        print(output)
        output = "average nodes visited (space complexity of discovered list) was " + str(averageNodesVisited)
        print(output)
        menu()
menu()


        
    
    

      
