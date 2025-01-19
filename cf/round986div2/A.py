
N = int(input())



def solve(n,a,b):
    x,y = 0,0
   

    
    effect = {'N':(0,1), 'S':(0,-1), 'E': (1,0), 'W':(-1,0) }

    sequence = {(0,0)}

    for dir in path:
        stepx,stepy = effect[dir]
        x,y = x+stepx,y+stepy
        sequence.add((x,y))
    if (x,y) == (0,0):
        return ( a,b) in sequence
    

    while -10<a<20 and -10<b<20:

        if (a,b) in sequence:
            return True
        
        a,b = a-x,b-y
    return False



for _ in range(N):
    n,a,b = tuple(map(int,input().split()))
    path = input()

    print('yes') if solve(n,a,b) else print('no')



        

   

    