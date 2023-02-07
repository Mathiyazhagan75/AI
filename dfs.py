import networkx as nx
import matplotlib.pyplot as plt


def DFS(g, node, visited, goal):
    path.append(node)
    if node == goal:
        return True
    visited.add(node)

    for i in g[node]:
        if i not in visited:
            if DFS(g, i, visited, goal):
                return True
            else:
                path.pop()
    return False
                   
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

path = list()
visited = set()

DFS(g, initial, visited, goal)

print(path)
   
path_edges = []

for i in range(len(path)-1):
    path_edges.append([path[i], path[i+1]])

nx.draw_networkx_edges(G,pos,edgelist=path_edges,edge_color='r',width=2)
plt.show()
