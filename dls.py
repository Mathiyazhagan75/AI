import networkx as nx
import matplotlib.pyplot as plt

def DLS(g, node, visited, goal, depth, L):
    path.append(node)
    
    if node == goal:
        return True
    
    for i in g[node]:

        if depth<L:
            visited.add(node)
            if i not in visited:
                if DLS(g, i, visited, goal, depth+1, L):
                    return True
                else:
                    path.pop()
        else:
            return False

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
goal = '8'

path = list()
visited = set()

print(DLS(g, initial, visited, goal, 0, 1))

print(path)
   
path_edges = []

for i in range(len(path)-1):
    path_edges.append([path[i], path[i+1]])

nx.draw_networkx_edges(G,pos,edgelist=path_edges,edge_color='r',width=2)
plt.show()
