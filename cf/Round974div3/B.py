import math
N = int(input())

for _ in range(N):
    n,k = tuple(map(int,input().split()))

    sumparity = not (math.ceil(n/2)&1)
    kparity = not(math.ceil((n-k)/2)&1)
    #print(n,k)
    #print(sumparity,kparity)
    if k<=n:
        kparity = not(math.ceil((n-k)/2)&1)
        print('YES') if (sumparity == kparity) else print('NO')
    else:
        print('YES') if sumparity else print('NO')
    #print('-'*20)

    
    


# if math.ceil(n/2) is even the sum so far is even
#