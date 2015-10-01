import assgt1
   
def menu():
    print('\n')
    print("Top Menu")
    print("enter an option by number")
    print("1: input a random seed and generate graphs")
    print("2: print a graph dictionary by index")
    print("3: depth-first-search on graph by index")
    print("4: run DFS on all graphs and output stats")
    print("5: run BFS on graph by index")
    print("6: run BFS on on all graphs and output stats")
    print("7: run recursiveDLS on graph by index")
    print("8: run IDFS on all graphs and output stats")
    print("9: perform greedy search on graph by index")
    print("10: perform A* search on a graph by index")
    print("11: run greedy search on all graphs")
    print("12: run A* search on all graphs")
    print("13: run all searches on all graphs and outputStats")
    option = input("what next?")
    global found
    global nodesTraversed
    global foundCount
    if option == '1':
      #  graphList = []
        seed = input("input random seed")
        random.seed(int(seed))
        print("making 100 graphs from seed")
        for x in range(20):  #will be 100, but not spending the time on that now
            makeGraph()
                
        menu()

    if option == '2':
       
        index = input("enter an index (integer)")
        printGraph(int(index))

    if option == '3':
        found = False
        discoveredList.clear()
        index = input("enter an index (integer)")
        depthFirstSearch(graphList[int(index)], 'a', 'z')

        menu()

    if option == '4':
        totalTime = 0
        nodesTraversed = 0
        foundList.clear()
        averageNodesVisited = 0
        foundCount = 0
        for x in graphList:
            found = False
            discoveredList.clear()
            t0 = time.clock()
            foundList.append(depthFirstSearch(x, 'a','z'))
            totalTime += time.clock() - t0
            averageNodesVisited += len(discoveredList)
                
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
        found = False
        discoveredList.clear()
        exploredList.clear()
        index = input("enter an index (integer)")
        breadthFirstSearch(graphList[int(index)], 'a', 'z')
        menu()

    if option == '6':
        totalTime = 0
        nodesTraversed = 0
        averageNodesVisited = 0
        foundCount = 0
        exploredCount.clear()
        foundList.clear()
        
        for x in graphList:
            found = False
            discoveredList.clear()
            exploredList.clear()
            t0 = time.clock()
            breadthFirstSearch(x, 'a','z')
            totalTime += time.clock() - t0
            averageNodesVisited += len(exploredList)

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
        found = False
        discoveredList.clear()
        index = input("enter an index (integer)")
        iterativeDeepeningSearch(graphList[int(index)], 'a', 'z')
        menu()

    if option == '8':
        totalTime = 0
        nodesTraversed = 0
        averageNodesVisited = 0
        foundCount = 0
        exploredCount.clear()
        
        for x in graphList:
            found = False
            print('\n')
            discoveredList.clear()
            t0 = time.clock()
            iterativeDeepeningSearch(x, 'a','z')
            totalTime += time.clock() - t0
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
        found = False
        exploredList.clear()
        discoveredList.clear()
        index = input("enter an index (integer)")
        greedySearch(graphList[int(index)], 'a', 'z', int(index))
        menu()

    if option == '10':
        found = False
        exploredList.clear()
        discoveredList.clear()
        index = input("enter an index (integer)")
        AStarSearch(graphList[int(index)], 'a', 'z', int(index))
        menu()

    if option == '11':
        found = False
        totalTime = 0
        nodesTraversed = 0
        averageNodesVisited = 0
        foundCount = 0
        exploredCount.clear()
        exploredList.clear()
        discoveredList.clear()

        index = 0

        for x in graphList:
            found = False
            exploredList.clear()
            discoveredList.clear()
            t0 = time.clock()
            greedySearch(x, 'a','z', index)
            index += 1
            totalTime += time.clock() - t0
            averageNodesVisited += len(discoveredList)

        foundCount = 0
        
        for x in foundList:
            if x == 1:
                foundCount +=1
        output = "found the goal " + str(foundCount) + "of " + str(len(graphList)) + "times"
        print(output)
        nodesTraversed /= len(graphList)
        output = "total time to run greedy on all graphs: " + str(totalTime)
        print(output)
        output = "average nodes visited (time complexity) was " + str(nodesTraversed)
        print(output)
        output = "average space complexity (list of visted nodes) was " + str(averageNodesVisited / len(graphList))
        print(output)
        menu()


    if option == '12':
        totalTime = 0
        nodesTraversed = 0
        averageNodesVisited = 0
        foundCount = 0
        exploredCount.clear()

        index = 0
        for x in graphList:
            found = False
            exploredList.clear()
            discoveredList.clear()
            t0 = time.clock()
            AStarSearch(x, 'a','z', index)
            index += 1
            totalTime += time.clock() - t0
            averageNodesVisited += len(discoveredList)
        foundCount = 0
        
        for x in foundList:
            if x == 1:
                foundCount +=1
        output = "found the goal " + str(foundCount) + "of " + str(len(graphList)) + "times"
        print(output)
        nodesTraversed /= len(graphList)
        output = "total time to run A* on all graphs: " + str(totalTime)
        print(output)
        output = "average nodes visited (time complexity) was " + str(nodesTraversed)
        print(output)
        output = "average space complexity (list of visted nodes) was " + str(averageNodesVisited / len(graphList))
        print(output)
        menu()

    if option == '13':
        print("******  BREADTH FIRST SEARCH   ******")
        totalTime = 0
        nodesTraversed = 0
        averageNodesVisited = 0
        exploredCount.clear()
        
        for x in graphList:
            found = False
            discoveredList.clear()
            exploredList.clear()
            t0 = time.clock()
            breadthFirstSearch(x, 'a','z')
            totalTime += time.clock() - t0
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


        print("******   DEPTH FIRST SEARCH   ******")
        totalTime = 0
        nodesTraversed = 0
        foundList.clear()
        averageNodesVisited = 0
        for x in graphList:
            found = False
            discoveredList.clear()
            t0 = time.clock()
            foundList.append(depthFirstSearch(x, 'a','z'))
            totalTime += time.clock() - t0
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

        print("******* ITERATIVE DEEPENING SEARCH************")
        totalTime = 0
        nodesTraversed = 0
        averageNodesVisited = 0
        exploredCount.clear()
        foundList.clear()
        
        for x in graphList:
            found = False
            
            t0 = time.clock()
            iterativeDeepeningSearch(x, 'a','z')
            totalTime += time.clock() - t0
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

        print("****** GREEDY BEST FIRST SEARCH, TWO HEURISTICS *******")
        found = False
        totalTime = 0
        nodesTraversed = 0
        averageNodesVisited = 0
        exploredCount.clear()
        foundList.clear()
        exploredList.clear()
        discoveredList.clear()

        index = 0

        for x in graphList:
            found = False
            exploredList.clear()
            discoveredList.clear()
            t0 = time.clock()
            greedySearch(x, 'a','z', index)
            index += 1
            totalTime += time.clock() - t0
            averageNodesVisited += len(discoveredList)

        foundCount = 0
        
        for x in foundList:
            if x == 1:
                foundCount +=1
        output = "found the goal " + str(foundCount) + "of " + str(len(graphList)) + "times"
        print(output)
        nodesTraversed /= len(graphList)
        output = "total time to run greedy on all graphs: " + str(totalTime)
        print(output)
        output = "average nodes visited (time complexity) was " + str(nodesTraversed)
        print(output)
        output = "average space complexity (list of visted nodes) was " + str(averageNodesVisited / len(graphList))
        print(output)

        print("****** A* BEST FIRST SEARCH, TWO HEURISTICS ******")
        totalTime = 0
        nodesTraversed = 0
        averageNodesVisited = 0
        exploredCount.clear()
        foundList.clear()

        index = 0
        for x in graphList:
            found = False
            exploredList.clear()
            discoveredList.clear()
            t0 = time.clock()
            AStarSearch(x, 'a','z', index)
            index += 1
            totalTime += time.clock() - t0
            averageNodesVisited += len(discoveredList)
        foundCount = 0
        
        for x in foundList:
            if x == 1:
                foundCount +=1
        output = "found the goal " + str(foundCount) + "of " + str(len(graphList)) + "times"
        print(output)
        nodesTraversed /= len(graphList)
        output = "total time to run A* on all graphs: " + str(totalTime)
        print(output)
        output = "average nodes visited (time complexity) was " + str(nodesTraversed)
        print(output)
        output = "average space complexity (list of visted nodes) was " + str(averageNodesVisited / len(graphList))
        print(output)
        
       
            
menu()


        
    
    

      
