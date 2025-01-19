N = int(input())


for _ in range(N):
    n,m = map(int,input().split())

    res = 4*m
    first = input()
    for _ in range(n-1):
        x,y = map(int,input().split())
        res+= 4*m - 2*(2*m-x-y)
    print(res)