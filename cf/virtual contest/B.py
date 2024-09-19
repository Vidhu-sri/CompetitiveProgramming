N = int(input())

for _ in range(N):
    n = int(input())
    res = 0
    ans = 0
    for i in range(2,n+1):
        k = n//i
        val = i*k*(k+1)/2
        if val>res:
            res = val
            ans = i

    print(ans)

