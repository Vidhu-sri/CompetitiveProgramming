from collections import defaultdict
N = int(input())


for _ in range(N):
    n = int(input())

    deg = [0]*(n+1)
    adj = defaultdict(list)

    for _ in range(n):
        u,v = map(int,input().split())
        deg[u]+=1
        deg[v]+=1
        adj[u].append(v)
        adj[v].append(u)
    if n == 2:
        print(0)
        continue
    x = max(deg[1:])
    S = [v for v in range(1,n+1) if deg[v] == x]

    if len(S) > 1:
        s0 = S[0]
        neighbors = set(adj[s0])
        flag = False

        for i in range(1,len(S)):
            v2 = S[i]
            if v2 not in neighbors and v2 != s0:
                flag = True
                break
        if flag:
            best = 2*x
        else:
            best = 2*x-1
    else:
        M = S[0]
        y = 0
        second_vertex = -1
        for v in range(1, n+1):
            if v != M and deg[v] > y:
                y = deg[v]
                second_vertex = v
        if second_vertex in set(adj[M]):
            best = x + y - 1
        else:
            best = x + y
    print(best-1)




