N = int(input())


for _ in range(N):
    n,m,(i,j) = map(int,input().split())
    in_board = lambda t: 1<=t[0]<=n and 1<=t[1]<=m 

    get_neighbors = next((neighbor for neighbor in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]))

    pass