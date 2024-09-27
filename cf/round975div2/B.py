from collections import defaultdict
from bisect import bisect_right, bisect_left
N = int(input())


for _ in range(N):
    n,q = tuple(map(int,input().split()))
    nums = list(map(int,input().split()))
    nums_ = set(nums)
    res = defaultdict(int)
    
    
    queries = list(map(int,input().split()))

    def in_array(x):
        right = n -bisect_right(nums,x)
        return bisect_left(nums,x)*(right+1) + right

    def not_inarray(x):
        right = n - bisect_right(nums,x)
        return bisect_left(nums,x)*right

    lo = min(queries)
    high = max(queries)
    for num in range(nums[0],nums[-1]+1):
        if num in nums_:
            res[in_array(num)]+=1
        else:
            res[not_inarray(num)]+=1
    res1 = [res[query] for query in queries]
    print(*res1)


 