

class UnionFind:
    def __init__(self,n):
        self.n = n
        self.par = [*range(n+1)]
        self.rank = [1]*(n+1)


    def find(self,x):
        p = self.par[x]
        while p!=self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p
    def union(self,x,y):
        p1,p2 = self.find(x),self.find(y)

        if p1 == p2:
            return False
        big = p1 if self.rank[p1]>self.rank[p2] else p2
        smol = p1 if self.rank[p1] <= self.rank[p2] else p2

        self.par[smol] = big
        self.rank[big] += self.rank[smol]
        return True


N = int(input())
for _ in range(N):
    n,m1,m2 = map(int,input().split())
    F = [list(map(int,input().split())) for _ in range(m1)]
    G = [list(map(int,input().split())) for _ in range(m2)]

    res = 0

    ufG = UnionFind(n+1)
    for u,v in G:
        ufG.union(u,v)
    
    F = [edge for edge in F if ufG.find(edge[0]) == ufG.find(edge[1])]
    res += m1-len(F)

    ufF = UnionFind(n+1)
    for u,v in F:
        ufF.union(u,v)
    
    for edge in G:
        if ufF.find(edge[0]) != ufF.find(edge[1]):
            res+=1
            ufF.union(edge[0],edge[1])
    print(res)



