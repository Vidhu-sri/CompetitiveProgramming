
N = int(input())



for _ in range(N):
    n = int(input())
    nums = list(map(int,input().split()))
    res =float('inf')
    def count(i):
        x = 0
        for j in range(n):
            if (j<i and nums[j]!=nums[i] ) or (j>i and nums[j]>nums[i]):
                x+=1 
        return x   
    
    for i in range(n):
        res = min(res,count(i))
    print(res)
