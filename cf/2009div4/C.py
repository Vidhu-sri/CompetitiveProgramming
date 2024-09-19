import math
N = int(input())

for _ in range(N):
    x,y,k = list(map(int, input().split()))


    if math.ceil(y / k)>=math.ceil(x/k):
        print(2*math.ceil(y/k))
    else:
        print(2*math.ceil(x/k)-1)

            
        
            
