
import random

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
            'o','p','q','r','s','t','u','v','w','x','y','z']
grid = [['0' for i in range(100)] for j in range(100)]
#(upper triangular) adjacency matrix
adjMatrix = [[0 for i in range(len(alphabet))]for j in range(len(alphabet))]
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
''' #uncomment to print the grid of letters
for j in range(0,100):
    rowOut = ""
    for i in range(0,100):
     if(grid[i][j] == '0'):
         rowOut += " "
     else:
         rowOut += grid[i][j]
        
    print(rowOut )  
'''
#cities placed in grid. Now determine adjacencies

