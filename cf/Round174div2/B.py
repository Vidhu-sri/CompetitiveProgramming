t = int(input())


for _ in range(t):
    n,m = map(int,input().split())
    nums = [list(map(int,input().split())) for _ in range(n)]
    exists = [0]*(n*m+1)
    has_neighbor = [0]*(n*m+1)
    for i in range(n):
        for j in range(m):
            exists[nums[i][j]] = 1

            if has_neighbor[nums[i][j]]:
                continue
            if 0<=(i+1)<n and nums[i+1][j] == nums[i][j]:
                has_neighbor[nums[i][j]] = 1
            elif 0<=(j+1)<m and nums[i][j+1] == nums[i][j]:
                has_neighbor[nums[i][j]] = 1
    res = 0
    flag = 0

    for i in range(n*m+1):
        if exists[i]:
            if has_neighbor[i]:
                flag = 1
                res+=2
            else:
                res+=1
    print(res-2) if flag else print(res - 1)





            

