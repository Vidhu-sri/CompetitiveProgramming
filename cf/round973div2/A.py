import math
N = int(input())

for _ in range(N):
    n = int(input())
    x,y = tuple(map(int,input().split()))
    divisor = min(x,y)
    print(math.ceil(n/min(x,y)))
