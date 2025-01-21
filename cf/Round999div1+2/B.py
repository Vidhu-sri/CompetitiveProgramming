from collections import Counter
from itertools import pairwise
from heapq import nlargest

N = int(input())


def solve(n,nums):
    counter = Counter(nums)

    best = nlargest(3,(x for x in nums if counter[x] >= 2))
    
    for a,b in pairwise(nums):
        delta = abs(a-b) >>1

        for c in best:
            if c<= delta:
                continue

            dec = counter[c] - (c==a) - (c==b)

            if dec>=2:
                print(*[a,b,c,c])
                
                return
            
    print(-1)

for _ in range(N):
    n = int(input())
    nums = list(map(int,input().split()))

    nums.sort()
    solve(n,nums)






