N = int(input())

for _ in range(N):
    x,y,z,k = list(map(int,input().split()))
        
    res = 0
    for i in range(1,min(x, k) + 1):
        if k % i != 0:
            continue
        
        for j in range(1,min(y, k) + 1):
            if not k%(i*j):
                third = k//(i*j)
                if third > z:
                    continue
                res = max(res, (x-i+1)*(y-j+1)*(z-third+1))
    print(res)

