import sys


n,d = map(int,input().strip().split(' '))
trees = [list(map(int,line.strip().split(' '))) for line in sys.stdin ]
start = [0]+[tree[2]+2 for tree in trees]

max_height = float('-inf')

for tree in trees:
    max_height = max(max_height, tree[0]+tree[1])

grid = [[' ']*d for _ in range(max_height)]



def change(i, j, grid, val):
    
    if grid[i][j] == ' ':
        grid[i][j] = val
        return
    print('colliding')
    sys.exit()
   

def draw():

    for tree in range(n):
        a,b,c = trees[tree]

        for j in range(start[tree],c):
            change(max_height-1,j,grid,'_')
        
        for i in range(max_height-b,max_height):
            change(i,c,grid,'|')
            change(i,c+1,grid,'|')
        
        upper_part = max_height - (a + b) 
        lower_end = max_height - b 
        k = 0
        for i in range(upper_part, lower_end):
            
            leaves = '/' + ' ' * (2*k) + '\\'
            if i == lower_end - 1:
                leaves = '/' + '_' * (2*k) + '\\'

            for l, j in enumerate(range(c - k, c+k+2 )): 
                if l<len(leaves):   
                    change(i, j, grid, leaves[l])

            k += 1

    for j in range(start[-1],d):
        change(max_height-1,j,grid,'_')
draw()

grid = [''.join(line) for line in grid]
for line in grid:
    print(line)





