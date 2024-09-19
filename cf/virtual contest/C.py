N = int(input())


for _ in range(N):
    n = int(input())
    nums = list(map(int,input().split()))
    add = 0
    count = 0
    check = set()
    for num in nums:
        add+=num
        check.add(num<< 1)
        if add in check:
            count+=1
    print(count)




