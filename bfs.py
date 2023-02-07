import networkx as nx
import matplotlib.pyplot as plt

def BFS(g, initial, goal):   
    visited = set()
    q = list()
    path = list()

    path.append(initial)
    q.append(path)
   
    while len(q):
        path = q.pop(0)
        s = path[len(path)-1]

        if s == goal:
            return path

        visited.add(s)
        for i in g[s]:
            if i not in visited:
                newpath = list(path)
                newpath.append(i)
                q.append(newpath)
    return []
                   
g = {
    '5': ['3', '8'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': ['9']
}

G = nx.DiGraph(g)
pos = nx.spring_layout(G)
nx.draw_networkx(G, pos)

initial = '5'
goal = '9'

path = BFS(g, initial, goal)

print(path)

path_edges = [[path[i], path[i+1]] for i in range(len(path)-1)]

nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2)
plt.show()


