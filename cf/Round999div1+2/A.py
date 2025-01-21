N = int(input())

for _ in range(N):
    n = int(input())
    nums = list(map(int,input().split()))
    i,j= 0,n-1

    while j>i:
        
        while j>i and not nums[j]%2:
            j-=1
        while i<j and nums[i]%2:
            i+=1
        nums[i],nums[j] = nums[j],nums[i]
    
    nums[0],nums[n-1] = nums[n-1],nums[0]

    res =0
    s = 0
    for i in range(n):
        s+= nums[i]
        if not s%2:
            res+=1
            while s!=0 and s%2 == 0:
                s//=2
    print(res)
