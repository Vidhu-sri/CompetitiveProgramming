N = int(input())

for _ in range(N):
    n = int(input())
    nums = list(map(int,input().split(' ')))
    res = nums[0]
    for i in range(1,len(nums)):
        res &=nums[i]
    print(res)
    