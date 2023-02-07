# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 11:24:38 2022

@author: 20pw38
"""
import networkx as nx
import matplotlib.pyplot as plt

g = {
    '5': ['3', '7' ,'8'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': ['9']
}

def IDS(initial, goal, limit, start_at=0):
    
    for d in range(start_at, limit+1):
        path = list()
        visited = set()
        if(DLS(initial, goal, visited, path, 0, d)):
            return [path, True]
    return [[], False]
    

def DLS(node, goal, visited, path, depth, L):
    path.append(node)
    
    if node == goal:
        return True
    
    for i in g[node]:

        if depth<L:
            visited.add(node)
            if i not in visited:
                if DLS(i, goal, visited, path, depth+1, L):
                    return True
                else:
                    path.pop()
        else:
            return False

    return False


initial = '5'
goal = '8'

print(IDS(initial, goal, 5))
