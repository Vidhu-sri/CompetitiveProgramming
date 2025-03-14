t = int(input())


for _ in range(t):
    n = int(input())
    nums = list(map(int,input().split()))

    flag = True
    for i in range(1,n):
        if nums[i]%nums[0]:
            flag = False
            print('NO')
            break
    if flag:
        print('YES')
        

