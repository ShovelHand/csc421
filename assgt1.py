
import random
import math
#import pdb; pdb.set_trace()

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
            'o','p','q','r','s','t','u','v','w','x','y','z']
grid = [['0' for i in range(100)] for j in range(100)]
graph = {}
#(upper triangular) adjacency matrix
adjMatrix = [[0 for i in range(len(alphabet))]for j in range(len(alphabet))]


neighbourList = []

def euclidDist(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2 +(y1-y2)**2)

def getFiveNearest(lst, i ,j):
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
                      
def findNeighbours(c, i, j, lst, depth):

    for n in range(100):
        for m in range(100):
            if(grid[m][n] != '0' and (grid[m][n] != c) and ((grid[m][n])) not in lst):
                lst.append(grid[m][n]) 
    
    if(len(lst) >= 10):
        return getFiveNearest(lst, i, j)

#pick 3 of the five cities on the list to be adjacent to current city
def populateAdjMatrix(city, lst):
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

            graph.update({city : x})
            graph[city] += x
        

        
                
def makeGraph():
    #initialize grid
    for j in range(0,100):
        for i in range(0,100):
            grid[i][j] = '0'

    random.seed(18) #let our random numbers be repeatable and debuggable

    for i in alphabet:
        placed = False
        while(placed == False):
            x = random.randrange(100)
            y = random.randrange(100)
            if(grid[x][y] == '0'):
                grid[x][y] = i
                placed = True
 #uncomment to print the grid of letters (not quite to scale)
            
    for j in range(0,100):
        rowOut = ""
        for i in range(0,100):
            if(grid[i][j] == '0'):
                rowOut += " "
        else:
            rowOut += grid[i][j]
        
    print(rowOut )
   
#cities placed in grid. Now determine adjacencies
    for j in range(0,100):
        for i in range(0,100):
           if(grid[i][j] != '0'):
                neighbourList = []
            #    print(grid[i][j])
                neighbourList = findNeighbours(grid[i][j], i, j, neighbourList, 1)
                if grid[i][j] == 't':
                    print(neighbourList)
                #print(neighbourList)
                populateAdjMatrix(grid[i][j], neighbourList)

    
    for j in range(26):
        for i in range(26):
            if adjMatrix[i][j] == 1 and adjMatrix[j][i] ==0:
                adjMatrix[j][i] = 1
                
                
            
makeGraph()

'''# print not to scale layout of cities
for j in range(100):
    row  = ""
    for i in range(100):
        if grid[i][j] != '0':
            row += grid[i][j]
        else:
            row += ' '
    print(row)
'''

print ('   abcdefghijklmnopqrstuvwxyz')
for j in range(26):
    row = alphabet[j]
    row += ': '
    for i in range(26):
        row += str(adjMatrix[i][j])
    print(row)


        
        

      
