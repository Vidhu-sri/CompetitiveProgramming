t = int(input())


for _ in range(t):
    n = int(input())
    nums = list(map(int,input().split()))

    flag = 0
    for i in range(n-4):
        if nums[i] == nums[i+2] == 1 and nums[i+1] == 0:
            print('NO')
            flag = 1
            break
    if not flag:
        print("YES")
