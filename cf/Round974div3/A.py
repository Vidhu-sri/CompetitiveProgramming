N = int(input())

for _ in range(N):
    n,k = tuple(map(int,input().split()))
    nums  = list(map(int,input().split()))

    res = 0
    gold = 0
    for num in nums:
        
        if num>=k:
            gold+=num
        elif not num and gold:
            gold-=1
            res+=1
       
    print(res)


