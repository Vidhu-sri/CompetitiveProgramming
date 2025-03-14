N = int(input())

def manhattan(t1,t2):
    return abs(t1[0]-t2[0]) + abs(t1[1]-t2[1])


for _ in range(N):
    n,m,i,j = map(int,input().split())
    print(1,1,n,m)
    



