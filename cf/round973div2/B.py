N = int(input())


for _ in range(N):
    n = int(input())
    
    nums = list(map(int,input().split()))
    total_sum = sum(nums[:-2])
    result = nums[-1] - nums[-2] + total_sum
    print(result)



