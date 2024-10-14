import math

N = int(input())

for _ in range(N):
    n, x = map(int, input().split())
    nums = list(map(int, input().split()))
    total = sum(nums)
    maxim = max(nums)
    res = max(math.ceil(total / x), maxim)
    print(res)
