'''
Round 998 Div3 - E

You are given two simple undirected graphs F and G with n vertices. F has m1 edges while G has m2 edges. You may perform one of the following two types of operations any number of times:

Select two integers u and v (1≤u,v≤n) such that there is an edge between u and v in F. Then, remove that edge from F. Select two integers u and v(1≤u,v≤n) such that there is no edge between u and v in F. Then, add an edge between u
 and v in F.
Determine the minimum number of operations required such that for all integers u
 and v(1≤u,v≤n), there is a path from u to v in F if and only if there is a path from u to v in G.

 https://codeforces.com/contest/2060/problem/E

'''

class UnionFind:

    def __init__(self, n):
        self.par = [*range(n+1)]
        self.rank = [0]*(n+1)

    def find(self, n1):
        res = n1
        while res != self.par[res]:
            self.par[res] = self.par[self.par[res]]
            res = self.par[res]
        
        return res

    def union(self,n1,n2):

        p1,p2 = self.find(n1), self.find(n2)

        if p1 == p2: return 0

        if self.rank[p1] >= self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1]+= self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2]+= self.rank[p1]
        return 1


t = int(input())

for _ in range(t):
    n, m1, m2 = map(int,input().split())

    F = [list(map(int,input().split())) for _ in range(m1)]
    G = [list(map(int,input().split())) for _ in range(m2)]


    res = 0

    ufG = UnionFind(n)
    for u,v in G:
        ufG.union(u,v)
    
    F = [edge for edge in F if ufG.find(edge[0]) == ufG.find(edge[1])]

    res+= m1-len(F)

    ufF = UnionFind(n)

    for u,v in F:
        ufF.union(u,v)

    for u,v in G:
        if ufF.find(u) != ufF.find(v):
            res+=1
        ufF.union(u,v)
    print(res)


    

