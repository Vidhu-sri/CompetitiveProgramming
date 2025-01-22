from collections import defaultdict

N = int(input().strip())
for _ in range(N):
    n = int(input().strip())

    adj = defaultdict(set)
   
    for _ in range(n):
        u,v = map(int,input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    first = max(adj,lambda x:len(adj[x]))
   

    for node in adj:
        if first in adj[node]:
            adj[node].remove(first)

    second = max(adj,lambda x:len(adj[x]))

    for node in adj:
        if second in adj[node]:
            adj[node].remove(second)
    tot = 0
    edges = set()
    for node in adj:
        if adj[node]:
            tot+=1
            for neighbor in adj[node]:
                edges.add((node,neighbor))
    print(tot-len(edges))

    

    


    
    
    