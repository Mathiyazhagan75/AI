"""
Spyder Editor
This is a temporary script file.
"""

# [missionary_left, cannibal_left, boat, missionary_right, cannibal_right]

s = [3, 3, 'L', 0, 0]
g = [0, 0, 'R', 3, 3]

def h(state):
    # (missionary_left + cannibal-left)/2
    return (state[0]+state[1])/2

def isSafe(state):
    return (state[0]==0 or state[0]>=state[1]) and (state[3]==0 or state[3]>=state[4])    

def generate(state):
    states= []
    ml, cl, boat, mr, cr = state
    if boat=='L':
        for i in range(1, min(2, ml)+1):
            if isSafe([ml-i, cl, 'R', mr+i, cr]):
                states.append([ml-i, cl, 'R', mr+i, cr])
        for i in range(1, min(2, cl)+1):
            if isSafe([ml, cl-i, 'R', mr, cr+i]):
                states.append([ml, cl-i, 'R', mr, cr+i])
        if ml>0 and cl>0:
            if isSafe([ml-1, cl-1, 'R', mr+1, cr+1]):
                states.append([ml-1, cl-1, 'R', mr+1, cr+1])
    else:
        for i in range(1, min(2, mr)+1):
            if isSafe([ml+i, cl, 'L', mr-i, cr]):
                states.append([ml+i, cl, 'L', mr-i, cr])
        for i in range(1, min(2, cr)+1):
            if isSafe([ml, cl+i, 'L', mr, cr-i]):
                states.append([ml, cl+i, 'L', mr, cr-i])
        if mr>0 and cr>0:
            if isSafe([ml+1, cl+1, 'L', mr-1, cr-1]):
                states.append([ml+1, cl+1, 'L', mr-1, cr-1])               
    return states


def a_star(start, goal):
    q = []
    q.append((h(start), [start], 0))
    visited = list()
    
    while q:
        q.sort()
        f = q[0][0]
        i = 0
        while i<len(q) and q[i][0]==f:
            visited.append(q[i][1][-1])
            i+=1
            
        while q and q[0][0]==f:
            f, path, g = q.pop(0)
            node = path[len(path)-1]
            
            if node==goal:
                return [path, g]
            
            for i in generate(node):
                if i not in visited:
                    new_path= list(path)
                    new_path.append(i)
                    q.append((h(i)+g+1, new_path, g+1))

def printSteps(steps):
    for step in steps:
        print(step[0], "M ", step[1], "C ", end="")
        if step[2]=='L':
            print('\____/              ', end="")
        else:
            print('             \____/ ', end="")
        print(step[3], "M ", step[4], "C")
        print("         ~~~~~~~~~~~~~~~~~~~")
        print()
        
        
steps, no_of_trips = a_star(s, g)
printSteps(steps)
print("No of trips : ", no_of_trips)


        


