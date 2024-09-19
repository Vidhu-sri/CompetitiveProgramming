N = int(input())

for _ in range(N):

    n,k = list(map(int,input().split()))
    nums =  list(map(int,input().split()))
    nums.sort(reverse=True)
    
    A = sum([nums[i] for i in range(0,len(nums),2)])
    B = 0
    for i in range(1,len(nums),2):
        delta = min(nums[i-1]-nums[i],k)
        k-=delta
        B+= nums[i] + delta
    print(A-B)



   