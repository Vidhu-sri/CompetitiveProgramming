N = int(input())

for _ in range(N):
    n,m = map(int,input().split())
    cows = []
    for _ in range(n):
        cows.append(sum(list(map(int,input().split()))))
    if len(cows) <= 1:
        print(1)
        continue
    cows = sorted(enumerate(cows,1),key=lambda x:x[1])
    flag = True
    
    for i in range(1,n):
     
        if cows[i][1]-cows[i-1][1] != m:
            flag = False
            break
    if flag:
        print(*[i for i,_ in cows])
    else:
        print(-1)


    
