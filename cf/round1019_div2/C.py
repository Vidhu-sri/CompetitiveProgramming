
import itertools
t = int(input())


def find_window(nums,k):

    prefix = list(itertools.accumulate(1 if num<=k else 0 for num in nums))
    l = None
    for i in range(len(nums)-2):
        if prefix[i]>= (i+1)/2:
            l=i
            break
    if l is None:
        return False
    if (    
        prefix[l+1] == prefix[l] and
        prefix[l+1]>=(l+2)/2 and
        l<len(nums)-3):
        l+=1
    
    for r in range(l+1,n-1):
        if prefix[r]-prefix[l] >= (r-l)/2 or prefix[n-1]-prefix[r] >= (n-1-r)/2:
            return True



for _ in range(t):
    n,k = map(int,input().split())
    nums = list(map(int,input().split()))

    if find_window(nums,k) or find_window(nums[::-1],k):
        print('YES')
    else:
        print('NO')





    
    
    


   

    
    
    

    


    








    

