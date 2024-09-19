
N = int(input())

memo = {}
def f(c):
    n = 2
    legs = [2,4]
    dp = [[0]*(c+1) for _ in range(n+1)]
    for i in range(c+1):
        dp[0][i] = float('inf')
    for i in range(c+1):
        dp[1][i] = i//legs[0] if not i%legs[0] else float('inf')
    
    for i in range(2,n+1):
        for j in range(c+1):
            if j<legs[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = min(1+dp[i][j-legs[i-1]],dp[i-1][j])
    return dp[-1][-1]

for _ in range(N):
    c = int(input())
    print(f(c))



N = int(input())

for _ in range(N):
    