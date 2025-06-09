





def solveHor(array, grid):

    n = len(grid)
    dp = [[float('inf'), float('inf')] for _ in range(n)]


 

    dp[0][0],dp[0][1] = 0, array[0]

    for i in range(1,n):
        for x in range(0,2):
            for y in range(0,2):
                ok = True
                for j in range(n):
                    ok = ok and (grid[i-1][j] + y != grid[i][j]+x)
            
                if(ok):

                    if x:
                        dp[i][x] = min(dp[i][x], dp[i-1][y]+array[i])
                    else:
                        dp[i][x] = min(dp[i][x],dp[i-1][y])
    
    return(min(dp[n-1][0], dp[n-1][1]))


def transpose(matrix):

    for i in range(len(matrix)):
        for j in range(i+1,len(matrix)):
            matrix[i][j],matrix[j][i] = matrix[j][i], matrix[i][j]




t = int(input())

for _ in range(t):
    n = int(input())
    grid = []
    for _ in range(n):
        to_append = list(map(int,input().split()))
        grid.append(to_append)
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    res = 0
    res+= solveHor(a, grid)
    transpose(grid)
    res+= solveHor(b, grid)
    print(res) if res != float('inf') else print(-1)
    



