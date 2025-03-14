import math
N = int(input())

for _ in range(N):
    a,b = map(int,input().split())

    res = abs(a-b)
    if not res:
        steps = 0
    else:
        steps = min(a%res, (res-a%res)%res)
   
    print(res,steps)
