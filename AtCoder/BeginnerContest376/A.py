

N, C = tuple(map(int, input().split()))

nums = list(map(int,input().split()))

last_received = nums[0]
res = 1

for i in range(1,N):
    if nums[i] - last_received >=C:
        res+=1
        last_received = nums[i]
print(res)