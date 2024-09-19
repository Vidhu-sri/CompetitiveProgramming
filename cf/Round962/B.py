N = int(input())


for _ in range(N):
    n,k = list(map(int,input().split()))
    
    grid = [list(map(int, list(input()))) for _ in range(n)]

    res = [[0]*(n//k) for _ in range(n//k)]

 

    for i in range(1,(n//k)+1):
        for j in range(1,(n//k)+1):
         
            res[i-1][j-1] = grid[k*(i-1)][k*(j-1)]
    for row in res:
        print(''.join(map(str, row)))
        