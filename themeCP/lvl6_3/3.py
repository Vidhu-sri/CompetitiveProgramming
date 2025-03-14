

t = int(input())

for _ in range(t):

    n = int(input())
    count = {i:set() for i in range(1,n+1)}

    for _ in range(n):
        nums = list(map(int,input().split()))
        for i in range(n-1):
            count[nums[i]].update(nums[:i])
    res = list(sorted(count.keys(),key=lambda x:len(count[x])))
    print(*res)