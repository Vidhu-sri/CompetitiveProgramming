
from collections import deque
t = int(input())


def bfs(neighbors):
    Q = deque([(1,0)])
    seen = set()

    while Q:


        node,dist = Q.popleft()
        if node in seen:
            continue
        seen.add(node)
        for neighbor in neighbors[node-1]:
            Q.append(neighbor)
        



for _ in range(t):
    n = int(input())
    edges = list(map(int,input().split()))

    neighbors = [[] for _ in range(n)]

    for i in range(len(edges)):
        neighbors[i+2].append(edges[i]-1)
        neighbors[edges[i]-1].append(i+2)
    

    
    


