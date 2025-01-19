
'''
Educational Codeforces Round 110 (Rated for Div. 2)
B. Array Reordering
https://codeforces.com/problemset/problem/1535/B
'''


import math


def to_swap(a,b):
    

    return math.gcd(a,2*b) == 1 and math.gcd(b,2*a) !=1


N = int(input())

for _ in range(N):
    n = int(input())
    nums = list(map(int,input().split()))

    i,j = 0,n-1
    while j>i:
        

        while j>i and nums[j]%2:
            j-=1
        while i<j and not nums[i]%2:
            i+=1
        nums[i],nums[j] = nums[j],nums[i]
    
    res = 0
    for i in range(n):
        for j in range(i+1,n):
            res+= math.gcd(nums[i],2*nums[j]) !=1
    print(res)




    
