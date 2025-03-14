#round 788 div2 A

t = int(input())


for _ in range(t):
    n = int(input())
    nums = list(map(int,input().split()))

    k = len([num for num in nums if num<0])

    flag = not (any(nums[i]<nums[i+1] for i in range(k-1)) or any(nums[i]>nums[i+1] for i in range(k+1,n-1)))

    print('YES') if flag else print('NO')
    


   

    
        
        

    