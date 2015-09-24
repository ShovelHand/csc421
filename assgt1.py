
import random
import math
#import pdb; pdb.set_trace()

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
            'o','p','q','r','s','t','u','v','w','x','y','z']
grid = [['0' for i in range(100)] for j in range(100)]
#(upper triangular) adjacency matrix
adjMatrix = [[0 for i in range(len(alphabet))]for j in range(len(alphabet))]
neighbourList = []
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
 #uncomment to print the grid of letters
for j in range(0,100):
    rowOut = ""
    for i in range(0,100):
     if(grid[i][j] == '0'):
         rowOut += " "
     else:
         rowOut += grid[i][j]
        
    print(rowOut )  

def euclidDist(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2 +(y1-y2)**2)

#this function doesn't work properly and should get fixed    
def findNeighbours(c, i, j, lst, depth):
    addRight = 0; #when increasing the search bounds and encountering an array edge,
    addBottom = 0;  

    leftCol = i - depth
    if(leftCol < 0):
       # addRight =  abs((i - depth))
        leftCol = 0

    rightCol = i + depth + addRight
    if(rightCol > 100):
        leftCol -= (depth)
        rightCol = 100

    topRow = j - depth 
    if(topRow < 0):
      #  addBottom = abs(j - depth)
        topRow = 0
   
    bottomRow = j + depth + addBottom
    if(bottomRow > 100):
        topRow -= ( depth)
        bottomRow = 100


        
    for n in range(topRow, bottomRow):
        for m in range(leftCol, rightCol):
            
            if(grid[m][n] != '0' and (grid[m][n] != c) and ((grid[m][n])) not in lst):
                lst.append(grid[m][n]) 
    if(len(lst) >= 5):
        print (c)
        print  (lst)
        if( c == 'l'):
            print(i,j)
        return lst
    else:
        if(depth < 100):
            findNeighbours(c, i, j, lst, depth+1)

            
#cities placed in grid. Now determine adjacencies
for j in range(0,100):
    for i in range(0,100):
        if(grid[i][j] != '0'):
            neighbourList = []
            neighbourList = findNeighbours(grid[i][j], i, j, neighbourList, 1)
           
       
           # neighbourList = []

#print(adjMatrix)
      
