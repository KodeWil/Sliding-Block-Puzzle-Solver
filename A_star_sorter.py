import numpy as np
import random

#value of every position of the grid
def position(x,y):
    if(x==1):
        pos = y
    elif(x==2):
        pos = 3+y
    else:
        pos = 6+y
    return pos
#available moves from empty
def movs(grid,empty):
    moves = []
    x = empty[0]
    y = empty[1]
    print(x)
    print(y)
    if(x + 1 < 3):
        aftGrid = mov(grid,[x+1 , y],empty)
        moves.append(aftGrid)
    if(x - 1 > 0):
        aftGrid = mov(grid,[x-1 , y],empty)
        moves.append(aftGrid)
    if(y + 1 < 3):
        aftGrid = mov(grid,[x , y+1],empty)
        moves.append(aftGrid)                    
    if(y - 1 > 0):
        aftGrid = mov(grid,[x , y-1],empty)
        moves.append(aftGrid)
    return moves

# moves
def mov(grid,pos,empty):
    x = int(empty[0])
    y = int(empty[1]) 
    tempEmp = grid[x,y]
    grid[x,y] = grid[int(pos[0]),int(pos[1])]
    grid[int(pos[0]),int(pos[1])] = tempEmp
    return grid

#heuristic for distance between neighbors dots
def heurDist(grid):
    distAcum = 0
    for i in range (0,3):
        for j in range (0,3):
            distAcum = distAcum + abs(position(i,j) - grid[i,j])
            if ( i ==1 and j ==1):
                if (grid[i,j] != 1):
                    distAcum = distAcum + 3
    return distAcum
        
def calcG(current,neighbor):
    distAcum = 0
    for i in range (0,3):
        for j in range (0,3):
            distAcum = distAcum + abs(current[i,j] - neighbor[i,j])
    return distAcum

#Distance between the actual position of a point and the correct position of it
#def heurRealDist(grid,cPos,pos):
#    [xc,yc] = cPos.index
#    [xp,yp] = pos.index
#    distance = 1000
#    if((abs(xc-xp)==1 and abs(yc-yp)==1)):
#        distance = 1.15
#    else:
#        distance = math.sqrt((xc-xp)**2 + (yc-yp)**2)
#    return distance

def heurMinLevel(grid):
    val = 0
    correctPosition = []   
    print('algo')
    for j in range(0,3):
        for i in range (0,3):
            val = val+1
            if (grid[i,j] == val):
                correctPosition.append(grid[i,j])
    correctPositionWeight = calcWeight(correctPosition)
    return correctPositionWeight
    
def calcWeight(dotArray):
    weight = 0
    for i in range (0, len(dotArray)-1) :
        weight = weight + dotArray[i]
        if (dotArray[i+1]-dotArray[i] == 1 and dotArray[i] < 3):
            weight = weight - 0.3
        if (dotArray[i] == 1):
            weight = weight - 0.5
    return weight
            
def returnEmpty(grid):
    x = 14
    y = 14
    for i in range(0,3):
        for j in range(0,3):
            if(grid[i,j] == 0):
                x = i
                y = j
                break
    empty = np.zeros((2))
    empty[0] = int(x)
    empty[1] = int(y)
    return empty

def lowestF(openSet):
    lowestFs = 99999
    for grid in openSet:
        gridF = 0.8*(heurMinLevel(grid)) + 0.2*(heurDist(grid)) 
        if (lowestFs > gridF):
            lowestFs = gridF
            lGrid = grid
    return lGrid

def listIndex(lista,indice):
    temp = lista.copy()
    val = temp.pop(indice)
    return val

    

def a_Star(grid,gridFinal):
    #
    openSet = []

    #
    cameFromIndex = 0
    cameFrom = []
    cameFrom.insert(cameFromIndex,grid) 
    #gScoreIndex necesary for track the path
    gScoreIndex = 0
    gScore = []
    gScore.insert(gScoreIndex,0)
    #fScoreIndex necesary for track the path
    fScoreIndex = 0
    fScore = []
    fScore.insert(fScoreIndex,0.8*(heurMinLevel(grid)) + 0.2*(heurDist(grid))) 

    #first position of empty spot
    empty = returnEmpty(grid)
    openSet.append(movs(grid,empty))
    while (len(openSet) != 0):
        current = lowestF(openSet)
        if current == gridFinal:
            return cameFrom
        
        neighbors = []
        neighbors = movs(current,returnEmpty(grid))
        gScoreIndex = gScoreIndex + 1
        gScore[gScoreIndex] = gScore[gScoreIndex - 1] + calcG(cameFrom[cameFromIndex],current) 
        cameFromIndex = cameFromIndex + 1
        openSet.remove(current)
        minNextPath = 999999
        for move in neighbors:
            tempgScore = gScore[gScoreIndex] + calcG(current,move)
            if minNextPath > tempgScore :
                minNextPath = tempgScore
                cameFrom[cameFromIndex+1] = current
                gScore[gScoreIndex+1] = tempgScore
                fScore[fScoreIndex+1] = gScore[gScoreIndex+1]  + 0.8*(heurMinLevel(grid)) + 0.2*(heurDist(grid))
                tempNext = move
        for item in openSet:
            if (item == tempNext):
                sw = 0
        
        if sw == 0:
            openSet.append(tempNext)
            sw = 1
    return FileNotFoundError

grid = np.zeros((3,3))
count = 0
for i in range (0,3):
    for j in range (0,3):
        if count < 8:
            count = count + 1
            grid[i,j] = count 
        else:
            grid[i,j] = 0
gridFinal = grid
np.random.shuffle(grid)
print(grid)
path = a_Star(grid,gridFinal)
if(len(path) != 0):
    print('Hizo algo') 