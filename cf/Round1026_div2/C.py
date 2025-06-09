from collections import deque

def solve(n,d,L,R):

    aside = deque()
    h = 0

    for i in range(n):
        if d[i] == -1:
            aside.append(i)
        
        else:
            h+= d[i]
        
        while h<L[i]:
            if not aside:
                return [-1]
            idx = aside.popleft()
            d[idx] = 1
            h+=1
        
        while h + len(aside) > R[i]:
            if not aside:
                return [-1]
            d[aside.popleft()] = 0
        
    while aside:
        d[aside.popleft()] = 0
    
    return d


t = int(input())

for _ in range(t):
    n = int(input())
    d = list(map(int,input().split()))

    L,R = [],[]
    for _ in range(n):

        l,r = map(int,input().split())

        L.append(l)
        R.append(r)
    print(*solve(n,d,L,R))        




    





            
        


