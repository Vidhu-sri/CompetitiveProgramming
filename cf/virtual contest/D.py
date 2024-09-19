N = int(input())

def centre(i,j,n, grid):
    start = i
    end = n-1
    while grid[end][j]!='#':
        end-=1
    return (start+end)//2
    


for _ in range(N):
    n,m = list(map(int,input().split()))
    grid = [list(input()) for _ in range(n)]
    
    flag = 0
    
    for i in range(n):
       
        for j in range(m):
           
            if grid[i][j] == '#':
                end = centre(i,j,n,grid)
                print(end+1,j+1)
                flag = 1
                break
        if flag:
            break
   
            


