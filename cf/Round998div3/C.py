from collections import Counter
N = int(input())


for _ in range(N):
    n,k = map(int,input().split())
    nums = list(map(int,input().split()))

    nums.sort()
    i,j = 0,n-1

    res = 0
    while j>i:
        a = nums[i]+nums[j]
        
        if a>k:
            j-=1
        elif a<k:
            i+=1
        else:
            res+=1
            i+=1
            j-=1
    print(res)
