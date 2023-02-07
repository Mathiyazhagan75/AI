goal = [[0, 1, 2] , [3, 4, 5] , [6, 7, 8]]

# start = [[7, 2, 4] , [5, 0, 6] , [8, 3, 1]]
start  = [[1, 4, 2] , [3, 7, 5] , [6, 8, 0]]

def value(state):
    dis=0
    for i in range(3):
        for j in range(3):
            n = state[i][j]
            x = n//3
            y = n%3
            dis += abs(x-i) + abs(y-j)
    return dis

def printState(state):
    print()
    for row in state:
        for n in row:
            print(n, end=" ")
        print()
    print()

def generateChildren(state):
    children = []
    for i in range(3):
        for j in range(3):
            if state[i][j]==0:
                x, y = i, j
                break
    
    for dx, dy in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
        if x+dx in range(3) and y+dy in range(3):
            newState = [list(row) for row in state]
            newState[x+dx][y+dy], newState[x][y] = newState[x][y], newState[x+dx][y+dy]
            children.append(newState)        
    return children

        
def hillclimbing(start):
    state = start
    printState(state)
    while state != goal:
        prevState = state
        for i in generateChildren(state):
            # print(value(i), value(state))
            if value(i) < value(state):
                state = i
                printState(state)
                break
        if state == prevState:
            print("local optimum reached")
            return
    print("Goal reached");


print("goal: ")
printState(goal)
print("steps: ")
hillclimbing(start)
