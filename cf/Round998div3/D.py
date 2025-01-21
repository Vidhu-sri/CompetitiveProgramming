N = int(input())

for _ in range(N):
    n = int(input())

    nums = list(map(int,input().split()))

    flag = True
    for i in range(n-1):
        if nums[i] > nums[i+1]:
            flag = False
            print('NO')
            break
        nums[i+1]-=nums[i]
    if flag:
        print('YES')


