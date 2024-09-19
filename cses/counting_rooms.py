m,n = list(map(int,input().split()))

building = [list(input().strip()) for _ in range(m)]

visited = set()

def dfs(i,j):

    neighbors = [(i,j+1), (i,j-1), (i+1,j), (i-1,j)]

    for neighbor in neighbors:
        x,y = neighbor
        if 0<=x<m and 0<=y<n and (x,y) not in visited and building[i][j] == '.':
            visited.add((x,y))
            dfs(x,y)
            
count = 0
for i in range(m):
    for j in range(n):
        if (i,j) not in visited and building[i][j] == '.':
            dfs(i,j)
            visited.add((i,j))
            count+=1

print(count)
        

