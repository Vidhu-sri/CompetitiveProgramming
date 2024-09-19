
N = int(input())

for _ in range(N):
    n = int(input())
    grid = [list(input()) for _ in range(n)]
    print(*[grid[n-i-1].index('#')+1 for i in range(n)])