from collections import defaultdict
from functools import cache
N = int(input())



for _ in range(N):
    sums = defaultdict(list)
    n=int(input())
    nums = list(map(int,input().split()))
    for idx,num in enumerate(nums):
        sums[idx+num].append((idx,num))
    
    @cache
    def solve(length):
      
        if not len(sums[length]):
            return length
        res = 0
        for pair in sums[length]:
            if pair[0]:
                res = max(res,solve(pair[0]+length))
        return res
    

    if len(nums) == 1:
        print(1)
    else:
        print(solve(n))



    
    





