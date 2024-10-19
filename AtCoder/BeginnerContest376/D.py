
from collections import deque,defaultdict
N,M = tuple(map(int,input().split()))
edges = []
for _ in range(M):
    edges.append(list(map(int,input().split())))
neighbors = defaultdict(list)
seen = set()
for edge in edges:
    neighbors[edge[0]].append(edge[1])

res = float('inf')

Q = deque()
Q.append(1)
level = 1
while Q:
    new_q = []
    level+=1

    while Q:
        node = Q.pop()
        seen.add(node)
        for neighbor in neighbors[node]:
            if neighbor == 1:
                res = min(level,res)
                continue
            if neighbor not in seen:
                new_q.append(neighbor)
                seen.add(neighbor)
    Q = new_q
        

print(res-1) if res != float('inf') else print(-1)







