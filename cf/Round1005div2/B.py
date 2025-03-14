from collections import Counter
 

t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    counter = Counter(nums)
 
    res = (0, -1)
    i = 0 
 
    for j in range(n):
        if counter[nums[j]] > 1:
            i = j + 1
            continue
 
        if j - i >= res[1] - res[0]:
            res = (i, j)
    
    if res[1] >= res[0]:
        print(res[0] + 1, res[1] + 1)
    else:
        print(0)
    