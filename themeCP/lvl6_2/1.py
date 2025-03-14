# Round 867 div3 - A

q = int(input())


for _ in range(q):
    n,t = map(int,input().split())

    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    res = 0 if a[0] <= t else -1
    score = 0
    for i in range(n):
        if i + a[i] <=t:
            if b[i] > score:
                res = i
                score = b[i]
    print(res+1) if res != -1 else print(-1)
                
            
